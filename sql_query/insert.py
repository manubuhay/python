import mysql.connector as dtb
mydb=dtb.connect(host="localhost"
                ,user="root"
                ,password="Python_123"
                ,database="python")

if mydb.is_connected():
    print("Connection Success!")
    cursordb=mydb.cursor()
    p_name=input("Enter name: ")
    p_sex=input("Enter sex: ")
    p_age=int(input("Enter age: "))
    p_address=input("Enter address: ")
    #all_val="INSERT INTO person(name,sex,age,address) VALUES('"+ p_name + "','" + p_sex + "'," + str(p_age) + ",'" + p_address + "');"
    cmd="INSERT INTO python.person(name,sex,age,address) VALUES( %s, %s, %s, %s)"
    all_val = (p_name, p_sex, p_age, p_address)
    cursordb.execute(cmd,all_val)
    mydb.commit()
    if cursordb:
        print("Values added!")
    else:
        print("Values rejected!")
    cursordb.close()
    mydb.close()
else:
    print("Connection failed!Exiting...")
