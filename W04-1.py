import pandas
import jaydebeapi

_sql = [
    "CREATE TABLE IF NOT EXISTS",
    "STOCKINFO(STOCKID CHAR(5), STOCKDATE CHAR(10),",
    "STOCKOPEN NUMBER, STOCKHIGH NUMBER, STOCKLOW NUMBER,",
    "STOCKCLOSE NUMBER, STOCKADJCLOSE NUMBER, STOCKVOL NUMBER);",
]
#用矩陣方式分段落,逗號後空格
#CHAR固定長度字串,不滿則補空格
#NUMBER開源資料庫做使用

sql = ' '.join(_sql)
print(sql)

dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/Users/user/anaconda3/Projects/data/H2",
    ["SA", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")

dbCursor = dbConnection.cursor()

#dbCursor.execute('DROP TABLE STOCKINFO;')
#第一次執行需要先drop掉

dbCursor.execute(sql)
dbCursor.execute('CREATE UNIQUE INDEX ON STOCKINFO(STOCKID, STOCKDATE);')
#建立key值
dbCursor.close()
dbConnection.close()
