import pymysql

def get_connection():

    return pymysql.connect(
        host='localhost',
        user='root',
        password='5437897543',
        database='fluire',
        cursorclass=pymysql.cursors.DictCursor
    )