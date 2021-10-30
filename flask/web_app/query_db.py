import mysql.connector as dtb

mydb=dtb.connect(host="codebase"
                ,user="python"
                ,password="Python_123"
                ,database="socmed")

if mydb.is_connected():
    cursor=mydb.cursor()
    def ifexists_db(utag,pw):
            query="""SELECT usertag, passwd FROM user_data WHERE usertag=%s AND passwd=%s"""
            data=(utag,pw)
            cursor.execute(query,data)
            results=cursor.fetchone()
            return results

    def insert_db(name,passwd,eadd,utag):
            query="""INSERT INTO user_data(name,passwd,email,usertag) VALUES( %s, %s, %s, %s)"""
            data=(name,passwd,eadd,utag)
            cursor.execute(query,data)
            mydb.commit()

    def remove_db(utag):
            query="""DELETE FROM user_data WHERE usertag=%s"""
            data=(utag,)
            cursor.execute(query,data)
            mydb.commit()

    def update_db(name,passwd,eadd,utag,old_utag):
            query="""UPDATE user_data SET name=%s, passwd=%s, email=%s, usertag=%s WHERE usertag=%s"""
            data=(name,passwd,eadd,utag,old_utag)
            cursor.execute(query,data)
            mydb.commit()

    def fetchuser_db(utag):
            query="""SELECT * FROM user_data WHERE usertag=%s"""
            data=(utag,)
            cursor.execute(query,data)
            results=cursor.fetchone()
            return results

if __name__=="__main__":
    cursor.close()
