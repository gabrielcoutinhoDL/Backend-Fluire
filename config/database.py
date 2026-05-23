import pymysql
from pymysql.cursors import DictCursor

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='a senha',
        database='o banco',
        cursorclass=DictCursor
    )