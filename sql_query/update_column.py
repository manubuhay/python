import mysql.connector as db
conn=db.connect(host="localhost"
                   ,username="root"
                   ,password="Python_123"
                   ,database="python")

if conn.is_connected():
    print("Connection Established!")
    cursor=conn.cursor()
    id=input("Select ID of data to update: ")
    column=input("What column to update: ")
    value=input("Change "+column+" to: ")
    data=(value,id)

    if column == "name":
      query="UPDATE person SET name=%s WHERE id=%s"
    elif column == "sex":
      query="UPDATE person SET sex=%s WHERE id=%s"
    elif column == "address":
      query="UPDATE person SET address=%s WHERE id=%s"
    elif column == "age":
      query="UPDATE person SET age=%s WHERE id=%s"
    else:
      print("Invalid column name.")

    cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()
else:
    print("Connection Failed!")
