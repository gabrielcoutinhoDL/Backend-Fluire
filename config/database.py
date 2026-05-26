import pymysql

def get_connection():

    return pymysql.connect(
        host='localhost',
        user='root',

        password='5437897543',
        database='fluire',
        cursorclass=pymysql.cursors.DictCursor

        passwd='061022',
        database='fluire_system',
        cursorclass=DictCursor
    )