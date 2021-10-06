import mysql.connector as dtb
mydb=dtb.connect(host="localhost"
                ,user="root"
                ,password="Python_123"
                ,database="python")

if mydb.is_connected():
    print("Connection Success!")
else:
    print("Connected failed!")

cursordb=mydb.cursor()
dbname=input("Input Database Name: ")
newdb="CREATE DATABASE " + dbname
#print(newdb)
cursordb.execute(newdb)
