from scrapy.http import HtmlResponse, Request, Response
from scrapy.exceptions import IgnoreRequest
from multiprocessing import Process, Pipe
from ghost import Ghost

class GhostAction:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def do(self, session):
        return self.action(session, *self.args, **self.kwargs)

    def action(self, session, *args, **kwargs):
        raise NotImplementedError

class DefaultOpenAction(GhostAction):
    def action(self, session, request):
        page, extra_resources = \
                    session.open(request.url, headers=request.headers)

        if request.action:
            request.action.do(session)
            page_, extra_resources_ = session.wait_for_page_loaded() 
            if page_:
                page, extra_resources = page_, extra_resources_
        
        return page

class GhostRequest(Request):
    def __init__(self, url=None, action=None, \
                    session=None, isLast=False, *args, **kwargs):
        if not url:
            assert session
            url = session.currentUrl

        super(GhostRequest, self).__init__(url, *args, dont_filter=True, **kwargs)

        self._action = action
        self._isLast = isLast
        self._session = session

    @property
    def session(self):
        return self._session

    @property
    def action(self):
        return self._action

    @property
    def isLast(self):
        return self._isLast

class GhostResponse(HtmlResponse):
    def __init__(self, request, session):
        self.request = request
        self.session = session

    def waitForInit(self):
        res = self.session.waitForResult()
        if res:
            super(GhostResponse, self).__init__(request=self.request, **res)

class GhostMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        return GhostMiddleware()

    def process_request(self, request, spider):
        if isinstance(request, GhostRequest):
            if request.session:
                session = request.session
                action = request.action
            else:
                session = GhostSession()
                action = DefaultOpenAction(request)
            session.commitAction(action, wait=False)

            if request.isLast:
                session.exit()

            return GhostResponse(request, session)

    def process_response(self, request, response, spider):
        if isinstance(response, GhostResponse):
            response.waitForInit()
        return response

class GhostSession:
    def __init__(self):
        # for the request without url
        self._currentUrl = None

        self.pipe, pipe = Pipe()
        self.startGhostProcess(pipe)

    def startGhostProcess(self, pipe):
        GhostProcess(pipe).start()

    def commitAction(self, action, wait=True):
        self.pipe.send(action)

        if wait:
            self.wait()

    def waitForResult(self):
        res = self.pipe.recv()
        self._currentUrl = res['url']
        return res
    
    def exit(self):
        self.commitAction(None, False)

    @property
    def currentUrl(self):
        return self._currentUrl

class GhostProcess(Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe
        self.currentPage = None

    def sendResult(self, session, page):
        res = {
            'url': page.url, 
            'status': page.http_status, 
            'headers': page.headers, 
            'body': session.content.encode('utf-8'),
        }
        self.pipe.send(res)

    def updatePage(self, session, page):
        if not page:
            page, extra_resources = session.wait_for_page_loaded() 

        if page:
            self.currentPage = page

    def run(self):
        ghost = Ghost()
        with ghost.start(download_images=False) as session:
            while True:
                action = self.pipe.recv()
                if action is None:
                    break

                page = action.do(session)
                self.updatePage(session, page)
                self.sendResult(session, self.currentPage)
