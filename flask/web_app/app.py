from flask import Flask,request,render_template,redirect,session,url_for
import os
import mysql.connector as dtb
from datetime import timedelta

mydb=dtb.connect(host="1.1.1.59"
                ,user="python"
                ,password="Python_123"
                ,database="socmed")

app=Flask(__name__)
app.secret_key="!@#$%"
app.permanent_session_lifetime= timedelta(hours=5)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def log_in():
    session.permanent=True # Reinforces line 13, false logs you out when exiting browser/tab
    uid=request.form['utag']
    passwd=request.form['pass']
    session['user_id']=uid

    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""SELECT usertag, passwd FROM human WHERE usertag=%s AND passwd=%s"""
        data=(uid,passwd)
        cursor.execute(query,data)
        results=cursor.fetchall()
        if len(results)==1:
            #return redirect(url_for("user_profile"))
            return render_template("profile.html")
        else:
            if "user_id" in session:
                return redirect(url_for("/profile"))
            return redirect("/registration")
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
            cursor.close()
            mydb.close()
            return redirect("/")
    return render_template("register.html")

@app.route("/profile")
def user_profile():
    if  "user_id" in session:
        user=session["user"]
        #return "Welcome "+ f"<h1>{user}!</h1>"
        return render_template("profile.html")
    return redirect("/")

@app.route("/logout")
def log_out():
    session.pop("user_id",None)
    return redirect(url_for("log_in"))

if __name__=="__main__":
    app.run(host="0.0.0.0",port="1234",debug=True)
