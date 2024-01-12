import pandas
import jaydebeapi

_sql=["ALTER TABLE STOCKINFO ADD (StockID char(5),StockNet NUMBER,StockScale NUMBER);"]
sql = ' '.join(_sql)
dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/Users/user/anaconda3/Projects/data/H2",
    ["SA", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")



dbCursor = dbConnection.cursor()
dbCursor.execute(sql)
dbCursor.close()
dbConnection.close()
