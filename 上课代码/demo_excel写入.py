import openpyxl

#打开文件
#openpyxl.open()
#不要在pycharm当中建立excel文件
wb=openpyxl.load_workbook('demo.xlsx')
#获取表格
ws=wb['Sheet1']
#active ,默认的表格
ws=wb.active
#写入数据
ws.cell(row=1,column=2).value="haha"
#保存
wb.save('demo.xlsx')
#退出
ws.close()


