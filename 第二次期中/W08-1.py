import pandas
import jaydebeapi
import random

_sql = [
    "CREATE TABLE IF NOT EXISTS",
    "INFO(S_ID NUMBER,G_ID NUMBER,AMOUNT NUMBER, PRICE NUMBER);"
]

sql = ' '.join(_sql)
print(sql)

dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/Users/user/anaconda3/Projects/data/H2",
    ["SA", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")

dbCursor = dbConnection.cursor()
dbCursor.execute('DROP TABLE INFO;')
dbCursor.execute(sql)
dbCursor.execute('CREATE UNIQUE INDEX ON INFO(S_ID,G_ID);')

#店家
_sql = [
    "INSERT INTO",
    "INFO(S_ID ,G_ID, AMOUNT, PRICE)",
    "VALUES(%d,%d,%d,%d);"
]
sql = ' '.join(_sql)
'''#商品
__sql = [
    "INSERT INTO",
    "INFO(G_ID)",
    "VALUES(%d);"
]
__sql = ' '.join(__sql)
'''
#刪除表中內容
dbCursor.execute('TRUNCATE TABLE INFO;')
#插入資料(店家)
for i in range(30):
    insert_sql = sql % ((i+1)%2,
                        (i)%15,
                        1000.0 * random.random(),
                        1000.0 * random.random())

    print(insert_sql)
    dbCursor.execute(insert_sql)
'''#插入資料(商品)
for i in range(100):
    insert_sql = __sql % ((i+1)%15) #店家ID

    print(insert_sql)
    dbCursor.execute(insert_sql)
'''
dbCursor.execute('SELECT * FROM INFO;')
resultSet = dbCursor.fetchall()

for row in resultSet:
    print(row)
dbCursor.close()
dbConnection.close()
