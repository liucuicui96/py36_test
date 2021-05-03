'''测试注册功能
    因为使用pytest框架'''
#import只能导入模块，from...import...可以导入函数，类，变量
import json
import requests
import pytest
from jsonpath import jsonpath

from middleware.handler import LccHandler
#获取excel文件的路径
data=LccHandler.excel.read('projects')

@pytest.mark.parametrize("info",data)
def test_projects(info):
    '''注册用例'''
    #如果存在#new_phone#,生成新的手机号码赋值给类属性
    LccHandler.generate_new_phone()
    # info转化成json字符串
    info = json.dumps(info)
    # 替换
    info = LccHandler.replace_data(info)
    # 转化成字典
    info = json.loads(info)
    #访问接口
    resp=requests.request(method=info['method'],url=LccHandler.yaml_config['host']+info['url'],
                          headers=eval(info['headers']),json=eval(info['json']))
    # 将字符转转化为字典
    expected = json.loads(info["expected"])
    #多值断言
    if info['case_id'] <= 2:
        assert resp.json()["username"]==expected["username"]
    elif info['case_id'] == 3:
        assert resp.json()== expected
    elif info['case_id'] == 4:
        assert resp.json()["name"]== expected["name"]
    #设置YZHandler对应的属性。
    if info['extractor']:
        # 转化为字典
        extrators = json.loads(info['extractor'])
        #遍历字典中的键值对
        for yz_prop, jsonpath_exp in extrators.items():
            #value = 'token'
            #将投资人登录接口返回的investor_member_id的值赋值给value
            value = jsonpath(resp.json(), jsonpath_exp)[0]
            #setastr(YZHandler, "loan_token", "yfowepfpwefwoefowf"
            setattr(LccHandler, yz_prop, value)
