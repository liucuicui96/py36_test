'''excel操作'''
import openpyxl

class ExcelHandler:
    def __init__(self,fpath):
        self.fpath=fpath

    def read(self,sheet_name):
        '''读取数据'''
        #打开文件
        wb=openpyxl.open(self.fpath)
        print(wb)
        #获取表格
        ws=wb[sheet_name]
        data=list(ws.values)
        header=data[0]
        all_data=[]
        for row in data[1:]:
            row_dict=dict(zip(header,row))
            all_data.append(row_dict)
        return all_data
    def write(self,sheet_name,data,row,column):
        '''写入excel数据'''
        wb=openpyxl.load_workbook(self.fpath)
        #获取表格
        ws=wb[sheet_name]
        ws.cell(row=row,column=column).value=data
        #通过workbook保存和关闭
        wb.save(self.fpath)
        wb.close()



'''if...main...的作用，调试代码
别人通过导入执行类，通过模块导入的下面的代码不会执行
要使用ExcelHandler'''
# if __name__=="__main__":
#     xls=ExcelHandler('cases.xlsx')
#     excel_data=xls.read('register')
#     pprint(excel_data)






