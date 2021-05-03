import pymysql
from pymysql.cursors import DictCursor

class DBHandle:
    def __init__(self,
                    host='',
                    port=3306,
                    user='',
                    password='',
                    charset='utf8',
                    database='',
                    cursorclass=DictCursor):
        #配置文件port
        self.conn = pymysql.connect(host=host, port=port,
                               user=user, password=password, charset=charset,
                               database=database, cursorclass=cursorclass)

    def query_one(self, sql):
        """数据库查询"""
        # 'SELECT * FROM futureloan.member LIMIT 10;'
        self.conn.ping(reconnect=True)
        self.cursor = self.conn.cursor()
        # 事务提交
        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        self.cursor.close()
        return data

    def query_all(self, sql):
        self.conn.ping(reconnect=True)
        self.cursor = self.conn.cursor()
        # 事务提交
        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    def query(self, sql, one=True):
        # self.cursor.execute(sql)
        if one:
            return self.query_one(sql)
        return self.query_all(sql)
    # def query(self, sql,one=True):
    #     self.cursor = self.conn.cursor()
    #     # 事务提交
    #     self.conn.commit()
    #     self.cursor.execute(sql)
    #     self.cursor.close()
    #     if one:
    #         return self.cursor.fetchone()
    #     return self.cursor.fetchall()
    # def insert(self, sql):
    #     self.cursor.execute('insert')
    #     # 提交
    #     self.conn.commit()

    def close(self):
        # self.cursor.close()
        self.conn.close()
#下面if用于测试的功能
if __name__=='__main__':
    db=DBHandle(
        host='8.129.91.152',
        port=3306,
        user='future',
        password='123456',
        charset='utf8',
        database='futureloan',
        cursorclass=DictCursor
    )
    data=db.query('select * from futureloan.member limit 10;',one=False)
    print(data)
    db.close()

