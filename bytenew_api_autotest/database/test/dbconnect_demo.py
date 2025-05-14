# -*- coding: UTF-8 -*-
import MySQLdb
import psycopg2


#诺客测试环境（banniu_book）
db = MySQLdb.connect('101.126.55.217','nktest','BNuokeBE_IxIAjTesT','banniu_book',charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s "%data)

sql = "SELECT * FROM ems.temp_deal_status WHERE problem_id = %s"%(3166)
cursor.execute(sql)
data2 = cursor.fetchall()
print(data2)
db.close()

#快递神器测试环境（artifact）
conn = psycopg2.connect(database="artifact",user="logistics",password="lg123456",host="101.126.55.217",port="54321")
cur = conn.cursor()
cur.execute("SELECT VERSION()")
pg_version = cursor.fetchone()
print("Database version : %s "%data)

sql2 = "select * from intercept_order.intercept_order_1896837922267267074 WHERE  trade_id ='313124342135' order by id desc"
cur = conn.cursor()
cur.execute(sql2)
res = cur.fetchall()
print(res)
conn.close()