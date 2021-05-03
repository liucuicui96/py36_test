import os
import re

from faker import Faker
from pymysql.cursors import DictCursor
from common.db_handler import DBHandle
from common.excel_handler import ExcelHandler
from common.yaml_handler import read_yaml
from common.logger_handler import get_logger
from config import path

class MidDBHandler(DBHandle):
    def __init__(self):
        yaml_path = os.path.join(path.GetPath('config'), 'config.yaml')
        yaml_config = read_yaml(yaml_path)
        user_path = os.path.join(path.GetPath('config'), 'security.yaml')
        user_config = read_yaml(user_path)
        super().__init__(
                 host=user_config['db']['host'],
                 port=user_config['db']['port'],
                 user=user_config['db']['user'],
                 password=user_config['db']['password'],
                 charset=user_config['db']['charset'],
                 database=user_config['db']['database'],
                 cursorclass=DictCursor)

class LccHandler():
    '''任务：中间层。common和调用层,隔离代码，使得common模块更加通用，使用common里面的代码更加简单。
    使用项目的配置数据，填充common模块
    '''
    #替换数据
    #新手机号码
    new_phone=' '
    investor_member_id=''
    investor_token=' '
    admin_member_id=' '
    admin_token=' '
    loan_id=' '
    loan_token=' '

    yaml_path = os.path.join(path.GetPath('config'), 'config.yaml')
    yaml_config = read_yaml(yaml_path)
    user_path = os.path.join(path.GetPath('config'), 'security.yaml')
    user_config = read_yaml(user_path)
    #logger
    logger_file=os.path.join(path.GetPath('logs'),yaml_config['logger']['file'])
    logger=get_logger(name=yaml_config['logger']['name'],
                      file=logger_file)
    #excel对象
    excel_file = os.path.join(path.GetPath('data'), 'cekai_cases.xlsx')
    excel = ExcelHandler(excel_file)

    #辅助函数,导入模块，其实就是重命名，把helper保存到help_funcs里面作为类属性
    # help_funcs=helper

    #数据库
    # db=DBHandle(
    #     host=user_config['db']['host'],
    #     port=user_config['db']['port'],
    #     user=user_config['db']['user'],
    #     password=user_config['db']['password'],
    #     charset=user_config['db']['charset'],
    #     database=user_config['db']['database'],
    #     cursorclass=DictCursor
    # )
    db=MidDBHandler()
    # new_phone=' '
    @classmethod
    def generate_new_phone(cls):
        # '''自动生成手机号码'''
        fk = Faker(locale="zh_CN")
        while True:
            phone=fk.phone_number()
            db=DBHandle(
                host='8.129.91.152',
                port=3306,
                user='future',
                password='123456',
                charset='utf8',
                database='futureloan',
                cursorclass=DictCursor
            )
            phone_in_db=db.query('select * from member where mobile_phone={};'.format(phone))
            db.close()
            if not phone_in_db:
                cls.new_phone=phone
                return phone
    #需要动态替换#...#的数据
    username=user_config['user_register']['username']
    email=user_config['user_register']['email']
    pwd = user_config['user_register']['pwd']
    user_id = user_config['user_register']['user_id']

    @classmethod
    def replace_data(cls,string,pattern='#(.*?)#'):
        """数据动态替换"""
        #pattern='#(.*?)#'
        results=re.finditer(pattern=pattern,string=string)
        for result in results:
            old=result.group()
            key=result.group(1)
            new=str(getattr(cls,key,''))
            string=string.replace(old,new)
        return string


if __name__=='__main__':
    # LccHandler.logger.warning("可以正常使用吗？？")
    # h=LccHandler()
    # h.logger.warning("还可以吗？？")
    # print(LccHandler.help_funcs)
    # # data =LccHandler.db.query('select * from futureloan.member limit 10;', one=False)
    data = LccHandler.db.query('select count(*) from test.tb_testcases', one=False)
    print(data)
    # string = '{"mobile_phone": "#investor_phone#", "pwd": "#investor_pwd#", "mobile_phone": "#loan_phone#", "pwd": "#loan_pwd#", "mobile_phone": "#admin_phone#", "pwd": "#admin_pwd#"}'
    # string='{"url":"/member/{#investor_member_id#}/info","json":"{" ":" "}","headers":"{"X-Lemonban-Media-Type":"lemonban.v2", "Authorization": "#investor_token#"}"}'
    # a = LccHandler.replace_data(string)
    # print(a)
