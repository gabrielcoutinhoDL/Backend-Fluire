import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='061022',
        database='fluire_system',
        cursorclass=DictCursor
    )