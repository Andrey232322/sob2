import pymysql
from conf import *


try:
    connection = pymysql.connect(
        host='localhost',
        port= 3306,
        user= user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('connect assept')
except Exception as e:
    print('conect return')
    print(e)