import random
import jaydebeapi

_sql = [
    "INSERT INTO",
    "STOCKINFO(STOCKID, STOCKDATE,",
    "STOCKOPEN, STOCKHIGH, STOCKLOW,",
    "STOCKCLOSE, STOCKADJCLOSE, STOCKVOL)",
    "VALUES('%s', '%s', %f, %f, %f, %f, %f, %f);"
]

sql = ' '.join(_sql)

dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/Users/user/anaconda3/Projects/data/H2",
    ["SA", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")

dbCursor = dbConnection.cursor()

dbCursor.execute('TRUNCATE TABLE STOCKINFO;')

insert_sql = sql % ('IBM', '2020-10-07',
                    100.0 * random.random(),
                    100.0 * random.random(),
                    100.0 * random.random(),
                    100.0 * random.random(),
                    100.0 * random.random(),
                    1000.0 * random.random())

print(insert_sql)
dbCursor.execute(insert_sql)

dbCursor.execute('SELECT * FROM STOCKINFO;')
resultSet = dbCursor.fetchall()

for row in resultSet:
    print(row)

dbCursor.close()
dbConnection.close()
