'''路径'''
'''换一个项目，path要重新写'''
#怎么求reports的目录
#动态获取路径，因为换一个项目存储时重新获取
import os
#动态获取路径
def GetPath(path_name):
    #获取当前文件父级目录路径
    config_path=os.path.dirname(os.path.abspath(__file__))
    #获取项目根目录
    root_path=os.path.dirname(config_path)
    #reports路径
    reports_path=os.path.join(root_path,path_name)
    if not os.path.exists(reports_path):
        os.mkdir(reports_path)
    return reports_path
if __name__=='__main__':
    print(GetPath('data'))

