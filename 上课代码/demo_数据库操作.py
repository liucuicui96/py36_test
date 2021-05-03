'''
musql,oracle,sql-server,postgres,redis,mongdb
'''
import pymysql
#建立连接，提供数据库信息
#1.建立连接,不要写成utf-8
from pymysql.cursors import DictCursor

conn=pymysql.connect(host='8.129.91.152',port=3306,
                     user='future',password='123456',charset='utf8',
                     database='futureloan',cursorclass=DictCursor)
#2.获取游标,转化为字典
cursor=conn.cursor()

#3.通过游标执行sql语句
cursor.execute('select * from futureloan.member limit 10;')

#4.通过游标获取结果
data=cursor.fetchone()
# data_all=cursor.fetchall()
print(data)
# print(len(data_all))

#关闭
cursor.close()
conn.close()


