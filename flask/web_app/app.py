from flask import Flask, request, render_template,redirect
import os
import mysql.connector as dtb
mydb=dtb.connect(host="1.1.1.59"
                ,user="python"
                ,password="Python_123"
                ,database="socmed")

app=Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def logged_in():
    uid=request.form['utag']
    passwd=request.form['pass']

    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""SELECT usertag, passwd FROM human WHERE usertag=%s AND passwd=%s"""
        data=(uid,passwd)
        cursor.execute(query,data)
        results=cursor.fetchall()
        if len(results)==1:
            return render_template("profile.html")
        else:
            return redirect("/registration")
    else:
        return "Error connecting to database!"

@app.route("/registration", methods=["GET", "POST"])
def register_now():
    if request.method=="POST":
        uname=request.form['name']
        passwd=request.form['pass']
        usertag=request.form['utag']
        eadd=request.form['e_mail']

        if mydb.is_connected():
            cursor=mydb.cursor()
            query="""INSERT INTO human(name,passwd,email,usertag) VALUES( %s, %s, %s, %s)"""
            data=(uname,passwd,eadd,usertag)
            cursor.execute(query,data)
            mydb.commit()
            return redirect("/")
    return render_template("register.html")

if __name__=="__main__":
    app.run(host="1.1.1.2")
