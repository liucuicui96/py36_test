'''打开excel-选择sheet表格--获取数据
openpyxl--主要针对xlsx格式的excel进行读取
安装：pip install openpyxl -i http://morrors.aliyun.com/pypi
xlrd--从excel中读取数据。支持xls,xlsx
xlwt库:对excel进行修改操作。不支持对xlsx格式的修改
pandas:csv,数据分析'''
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
#打开excel
from pip._vendor.html5lib.treewalkers import pprint

workbook=openpyxl.open('cases.xlsx')
print(workbook)
#选择sheet表格，worksheet
#通过表格的名称取货去：类似于字典
ws:Worksheet=workbook['register']
print(ws)

#获取数据，某个单元格的数据
cell=ws.cell(row=1,column=2)
print(cell.value)
#获取表格当中的第一行
print(ws[1])
#获取所有的行
print(list(ws.rows))
#获取所有的数据
pprint(list(ws.values))
