import mysql.connector as db
conn=db.connect(host="localhost"
                   ,username="root"
                   ,password="Python_123"
                   ,database="python")

if conn.is_connected():
    print("Connection Established!")
    cursor=conn.cursor();
    cursor.execute("show tables;") #No need for variable catcher
    tables=cursor.fetchall() #fetchall() retrieves data from last query(execute show tables), needs variable catcher
    #for table in tables:
    print(tables)
    table=input("Which table? ")
    cmd="SELECT * FROM "
    query=cmd+table
    cursor.execute(query) #No need for variable catcher
    result=cursor.fetchall() #fetchall() retrieves data from last query(execute query), needs variable catcher
    print(result)
    #for i in result:
    #    print(result)
    cursor.close()
    conn.close()
else:
    print("Connection Failed!")
