# coding:utf-8
import xlrd
import xlwt

bk = xlrd.open_workbook('2018.xlsx')
bk.sheets()
bk.sheet_names()
sh = bk.sheet_by_name('服务部百万')
sh.nrows
sh.ncols
sh.row(0)
sh.row(1)
sh.row_slice(1)
sh.row_types(1)
sh.row_slice(2)
sh.row_types(2)
sh.row_values(2)
sh.col_values(1)
sh.cell_value(12, 7)
for row_index in range(sh.nrows):
    print(sh.row_values(row_index))

book = xlwt.Workbook()
sheet = book.add_sheet('hello')
font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
bd = xlwt.Borders()
bd.left = 1
bd.right = 2
bd.top = 3
bd.bottom = 4
bd.left_colour = 4
bd.right_colour = 5
bd.top_colour = 6
bd.bottom_colour = 7
al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
s0 = xlwt.XFStyle()
s0.font = font
s0.alignment = al
s1 = xlwt.XFStyle()
s1.borders = bd
# 向第一行第2列写入值“姓名”,并设置字体和
sheet.write(0, 1, '姓名', s0)
# 将第二行到第三行的第二列合并，赋值‘张三’
sheet.write_merge(1, 2, 1, 1, '张三', s1)
book.save('test.xls')
