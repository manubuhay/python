import mysql.connector as dtb
mydb=dtb.connect(host="localhost"
                ,user="root"
                ,password="Python_123"
                ,database="python")

if mydb.is_connected():
    print("Connection Success!")
    cursordb=mydb.cursor()
    id=input("Enter ID of person to delete: ")
    cmd="DELETE FROM person where id="+id
    cursordb=mydb.cursor()
    cursordb.execute(cmd)
    mydb.commit()
else:
    print("Connected failed!Exiting...")
