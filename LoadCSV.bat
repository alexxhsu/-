SET DB_USER="emprogria"
SET DB_BASE="Emprogria"
SET DB_TABLE="MRT_G"

SET PATH=D:\ArangoDB3-3.8.2_win64\usr\bin;%PATH%

SET CSV_FILE="C:\Users\user\anaconda3\Projects\data\MRT_G.csv"


arangoimport --server.username %DB_USER% --server.database %DB_BASE% --collection %DB_TABLE% --type csv --file %CSV_FILE%
#中間要有空格
