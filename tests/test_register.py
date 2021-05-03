'''测试注册功能
    因为使用pytest框架'''
#import只能导入模块，from...import...可以导入函数，类，变量
import json
import requests
import pytest
from middleware.handler import LccHandler
#获取excel文件的路径
data=LccHandler.excel.read('user_register')

@pytest.mark.parametrize("info",data)
def test_register(info):
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
    if info['case_id']<=5:
        try:
            assert resp.json()==expected
        except AssertionError as e:
            LccHandler.logger.error("用例失败:{}",format(e))
            raise e
    else:
        try:
            assert resp.json()["username"]==expected["username"]
        except AssertionError as e:
            LccHandler.logger.error("用例失败:{}",format(e))
            raise e
    #写入Excel
    # finally:
    #     excel=ExcelHandler(excel_file)
    #     excel.write('register',str(resp_body),
    #                 row=int(info['case_id'])+1,
    #                 column=9)
# if __name__=='__main__':
#     print(test_register("info"))

#数据驱动 DONE
#Excel存储用例 DONE
#封装logger DONE
#配合文件的编写 UNDONE
#报告 DONE
#程序入口 DONE

#夹具 UNDONE
#结果发送钉钉
#手机号码动态变化
#调试的两种方法：1.切片 2.except
