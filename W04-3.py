import pandas
import jaydebeapi

def output_row(row):
    print("%s\t%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % row)

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
    "jdbc:h2:C:/User/user/anaconda3/Projects/data/H2",
    ["SA", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")

dbCursor = dbConnection.cursor()

#dbCursor.execute('TRUNCATE TABLE STOCKINFO;')

my_data_path = 'C:/Users/user/anaconda3/Projects/data/IBM-Stocks'
my_data_file = 'IBM-2017.csv'
my_dataset = pandas.read_csv('%s/%s' % (my_data_path, my_data_file))

for i in range(my_dataset.shape[0]):
    #有幾筆資料就做幾次
    row = my_dataset.iloc[i]

    insert_sql = sql % ('IBM', row['Date'],
                        row['Open'],
                        row['High'],
                        row['Low'],
                        row['Close'],
                        row['Adj Close'],
                        row['Volume'] / 1000.0)

    dbCursor.execute(insert_sql)

dbCursor.execute('SELECT * FROM STOCKINFO LIMIT 5;')
resultSet = dbCursor.fetchall()

for row in resultSet:
    output_row(row)

dbCursor.execute('SELECT * FROM STOCKINFO ORDER BY STOCKID, STOCKDATE DESC LIMIT 5;')
resultSet = dbCursor.fetchall()

for row in resultSet:
    output_row(row)

dbCursor.close()
dbConnection.close()
