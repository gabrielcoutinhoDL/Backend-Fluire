import pymysql

def get_connection():

    return pymysql.connect(
        host='localhost',
        user='root',
<<<<<<< HEAD
        password='5437897543',
        database='fluire',
        cursorclass=pymysql.cursors.DictCursor
=======
        passwd='061022',
        database='fluire_system',
        cursorclass=DictCursor
>>>>>>> 02a6518e1726b3d9c2d096047484139d6d67434a
    )