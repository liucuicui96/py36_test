import json
import pytest
import requests
from jsonpath import jsonpath

from middleware.handler import LccHandler

data=LccHandler.excel.read('login')
@pytest.mark.parametrize('info',data)
def test_login(info):
    #生成新的手机号码赋值给类属性
    LccHandler.generate_new_phone()
    # info转化成json字符串
    info = json.dumps(info)
    #替换
    info = LccHandler.replace_data(info)
    #转化成字典
    info = json.loads(info)
    #发送接口请求
    resp=requests.request(method=info['method'],
                          url=LccHandler.yaml_config['host']+info['url'],
                          headers=eval(info['headers']),
                          json=eval(info['json']))
    #将字符转转化为字典
    expected = json.loads(info["expected"])
    #多值断言
    if info['case_id']==3:
        assert resp.json()["username"] == expected["username"]
    elif info['case_id']<=2:
        assert resp.json()==expected
    else:
        assert resp.json()["user_id"]== expected["user_id"]
        assert resp.json()["username"] == expected["username"]
    # 设置YZHandler对应的属性。
    if info['extractor']:
        # 转化为字典
        extrators = json.loads(info['extractor'])
        # 遍历字典中的键值对
        for yz_prop, jsonpath_exp in extrators.items():
            # value = 'token'
            # 将投资人登录接口返回的investor_member_id的值赋值给value
            value = jsonpath(resp.json(), jsonpath_exp)[0]
            # setastr(YZHandler, "loan_token", "yfowepfpwefwoefowf"
            setattr(LccHandler, yz_prop, value)

