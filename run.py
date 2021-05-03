'''项目入口，主程序。
收集用例，运行用例，生成报告'''
import pytest
import os
from config import path
from datetime import datetime
#pytest收集用例
#如何放到reports
#TODO:报告+时间戳
#reports/report.html
#获取现在的时间戳
ts=datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
report_file_name='report'+ts+'.html'
print(type(ts))
#获取测试报告存储路径
report_dir=path.GetPath('reports')
#拼接文件
report_file=os.path.join(report_dir,report_file_name)
pytest.main(['--html={}'.format(report_file),'-s'])





