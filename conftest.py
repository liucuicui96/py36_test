import pytest
from middleware.handler import LccHandler

@pytest.fixture()
def db():
    '''管理数据库链接的夹具'''
    db_conn=LccHandler.db
    #yield之前是前置条件，yield之后是后置条件
    yield db_conn
    db_conn.close()
# if __name__=='__main__':
#     print(add_loan(loan_login["token"]))

