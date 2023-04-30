import pymysql
db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="test",
    port=3306,
)

cursor = db.cursor()
cursor.execute('SELECT VERSION()')
print('Database version:', cursor.fetchone())