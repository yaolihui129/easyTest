# 使用第三方库 xlrd 和xlwt 这两个库分别用于excel读和写


import xlrd

# book = xlrd.open_workbook('score.xlsx')
# book.sheet()

# sheet = book.sheet_by_index(0)
# print(sheet.nrows)  # 行数
# print(sheet.ncols)  # 列数
#
# cell = sheet.cell(0, 0)  # 单元格
# print(cell.ctype)  # 单元格类型
#
# print(cell.value)
# cell = sheet.cell(1, 1)
# print(cell.value)
# print(cell.ctype)
#
# print(sheet.row(1))
# print(sheet.row_values(1))
# print(sheet.row_values(1, 1))

# 写excel
import xlwt

# wbook = xlwt.Workbook()
# wsheet = wbook.add_sheet('sheet1')
# wbook.save('output1.xls')


# #一个例子
# rbook = xlrd.open_workbook('score.xlsx')
# rsheet = rbook.sheet_by_index(0)
# nc = rsheet.ncols
# rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, '总分', None)  # 给单元格赋值
# for row in range(1, rsheet.nrows):
# 	t = sum(rsheet.row_values(row, 1, 3))
# 	rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)
#
# wbook = xlwt.Workbook()
# wsheet=wbook.add_sheet(rsheet.name)
# # style = xlwt.easyxf('align:vertical center,horizontal center')  # 样式
# for r in range(rsheet.nrows):
# 	for c in range(rsheet.ncols):
# 		wsheet.write(r, c, rsheet.cell_value(r, c))
# wbook.save('output.xlsx')

rbook =xlrd.open_workbook('output.xlsx')
rsheet= rbook.sheet_by_index(0)
print(rsheet.row_values(0))