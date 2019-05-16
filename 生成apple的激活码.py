'''
第 0001 题:做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''

import random
import string
import csv
import MySQLdb

def app_code():
    codes = []
    num = 0
    while num < 200:
        code = ''.join(random.sample(string.ascii_lowercase+string.digits,10))
        codes.append(code)
        num +=1
    return codes


def write_mysql():
    db = MySQLdb.connect('localhost','root','Abcd520025@','study',charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute("create table s2 (id int primary key,code varchar(40))")
    except:
        db.rollback()
    codes = app_code()
    for index,code in enumerate(codes):
        cursor.execute("insert into s2 value ('{}','{}')".format(index,code))
    #提交书记
    db.commit()
    #关闭连接
    db.close()

# 返回数据库前6条数据
db = MySQLdb.connect('localhost','root','Abcd520025@','study',charset='utf8')
cursor = db.cursor()
cursor.execute('select * from s2;')
a = cursor.fetchmany(6)
print(a)











