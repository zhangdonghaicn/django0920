#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='itcast',
        db ='class',
        )
cur = conn.cursor()

#获得表中有多少条数据
aa=cur.execute("select * from student")
print aa

#打印表中的多少数据
info = cur.fetchmany(aa)
for ii in info:
    print ii
cur.close()
conn.commit()
conn.close()
