import mysql.connector as db
conn=db.connect(host="1.1.1.59"
                   ,username="python"
                   ,password="Python_123"
                   ,database="socmed")

# if conn.is_connected():
#     print("Connection Established!")
#     cursor=conn.cursor();
#     while True:
#         id=input("Enter ID: ")
#         cmd="SELECT * FROM human WHERE id=%s"
#         idquery=(id,)
#         cursor.execute(cmd,idquery) #No need for variable catcher
#         result=cursor.fetchone() #fetchall() retrieves data from last query(execute query), needs variable catcher
#         if result:
#             print(result[0])
#             print(result[1])
#             print(result[2])
#             print(result[3])
#         else:
#             print("Does not exist!")
#     # cursor.close()
#     conn.close()
# else:
#     print("Connection Failed!")

if conn.is_connected():
    cursor=conn.cursor()
    utag=input("Enter username: ")
    pw=input("Enter Password: ")
    #query="""SELECT usertag,passwd FROM human WHERE usertag=%s AND passwd=%s"""
    query="""SELECT * FROM human WHERE usertag=%s AND passwd=%s"""
    data=(utag,pw)
    cursor.execute(query,data)
    result=cursor.fetchone()
    cursor.execute(query,data)
    results=cursor.fetchall()
    cursor.close()
    # if result:
    print("--------------------")
    print("fetchone is "+str(len(result)))
    print("fetchall is "+str(len(results)))
    print("fetchone result is: "+str(result))
    print("fetchall result is: "+str(results))
    # print(result[0])
    # print(result[1])
    # print(result[2])
    # print(result[3])
    print("--------------------")
# else:
    print(len(result))
