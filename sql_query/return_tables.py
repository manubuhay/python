import mysql.connector as db
conn=db.connect(host="localhost"
                   ,username="admin"
                   ,password="Pyth0n_123"
                   ,database="python")

if conn.is_connected():
    print("Connection Established!")
    cursor=conn.cursor();
    cursor.execute("show tables;") #No need for variable catcher
    tables=cursor.fetchall() #fetchall() retrieves data from last query(execute show tables), needs variable catcher
    for i in tables: #Iterate over the list and display each values in new line
        print(i)
    table=input("Which table? ")
    cmd="SELECT * FROM %s"%(table)
    # query=cmd+table
    # cursor.execute(query) #No need for variable catcher
    cursor.execute(cmd)
    result=cursor.fetchall() #fetchall() retrieves data from last query(execute query), needs variable catcher
    #print(result) #Does not iterate, displays data with no new line
    for i in result: #Iterate over the list and display each values in new line
        print(i)
    cursor.close()
    conn.close()
else:
    print("Connection Failed!")
