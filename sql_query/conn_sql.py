import mysql.connector as dtb
mydb=dtb.connect(host="1.1.1.59"
                ,user="admin"
                ,password="Pyth0n_123"
                ,database="python")

if mydb.is_connected():
    print("Connection Success!")
else:
    print("Connected failed!")

cursordb=mydb.cursor()
dbname=input("Input Database Name: ")
# newdb="CREATE DATABASE " + dbname
newdb="CREATE DATABASE %s"%(dbname)
cursordb.execute(newdb)
