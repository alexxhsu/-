import pandas
import jaydebeapi

_sql = [
  "CREATE TABLE IF NOT EXISTS",
  "STOCKINFO(STOCKID CHAR(S), STOCKDATE CHAR(10)),",
  "STOCKOPEN NUMBER, STOCKHIGH NUMBER, STOCKLOW NUMBER,",
  "STOCKCLOSE NUMBER, STOCKADJCLOSE NUMBER, STOCKVOL NUMBER);",
]

sql =" ".join(_sql)
print(sql)

dbConnection = jaydebeapi.connect(
     "org.h2.Driver",
     "jdbc:h2:/Users/justin/Desktop/Projects/DB/data/H2",
     ["SA",""],
     "/Users/justin/Desktop/Projects/h2/bin/h2-1.4.200.jar")


dbCursor = dbConnection.cursor()

dbCursor.execute('DROP TABLE STOCKINFO;')
dbCursor.execute(sql)
dbCursor.execute('CREATE UNIQUE INDEX ON STOCKINFO(STOCKID,STOCKDATE);')

dbCursor.close()
dbConnection.close()
