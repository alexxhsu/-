import pandas
import jaydebeapi

dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/Users/user/anaconda3/Projects/data/H2",
    ["SA", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")
dbCursor = dbConnection.cursor()

_sql = [
    "CREATE TABLE IF NOT EXISTS",
    "StockInfo2(title char, score char,",
    "id char, url char, comms_number char,",
    "created char, body char, timestamp char);"
]
sql = ' '.join(_sql)
dbCursor.execute(sql)

_sql = [
    "INSERT INTO",
    "StockInfo2(title, score,",
    "id, url, comms_number,",
    "created, body, timestamp)",
    "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
]

sql = ' '.join(_sql)
dbCursor.execute('TRUNCATE TABLE StockInfo2;')

my_data_path = 'C:/Users/user/anaconda3/Projects/data'
my_data_file = 'reddit_vm.csv'
my_dataset = pandas.read_csv('%s/%s' % (my_data_path, my_data_file))

for i in range(my_dataset.shape[0]):
    row = my_dataset.iloc[i]
'''
    _sql = [
        '%04d' % i,
        "'%s'" % row[0].replace('\n', ' ').replace("'", "''"),
        '%d' % row[1],
        "'%s'" % row[2],
        "'%s'" % row[3].replace('\n', ' ').replace("'", "''"),
        '%d' % row[4],
        '%d' % row[5],
        "'%s'" % row[6].replace('\n', ' ').replace("'", "''"),
        "'%s'" % row[7],
        "'%s'" % row[8]
    ]
    r_sql = ' '.join(_sql)
    dbCursor.execute(r_sql)
'''

    insert_sql = sql % (
                        row['title'],
                        row['score'],
                        row['id'],
                        row['url'],
                        row['comms_num'],
                        row['created'],
                        row['body'],
                        row['timestamp'] )

    dbCursor.execute(insert_sql)

def output_row(row):
    print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % row)

dbCursor.execute('SELECT * FROM StockInfo2 LIMIT 5;')
resultSet = dbCursor.fetchall()

for row in resultSet:
    output_row(row)

dbCursor.execute('SELECT * FROM StockInfo2 ORDER BY timestamp LIMIT 5;')
resultSet = dbCursor.fetchall()

for row in resultSet:
    output_row(row)

dbCursor.close()
dbConnection.close()
