# 2-7 如何实现用户的历史记录功能（最多N条）

# c猜数字的游戏

from collections import deque
q=deque([],5) #创建双端队列
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
print(q)

#存储到文件中
import pickle
pickle.dump(q,open('history','wb'))
#从文件中读取
q2=pickle.load(open('history','rb'))
print(q2)