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

# @app.route("/")
# def index_page():
#     if "user_id" in session:
#         return redirect(url_for("user_profile")) #Redirect user to profile page if session exists
#     return render_template("index.html")

def if_exists(tag,pw):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""SELECT usertag, passwd FROM human WHERE usertag=%s AND passwd=%s"""
        data=(tag,pw)
        cursor.execute(query,data)
        results=cursor.fetchall()
        cursor.close()
        return results

def insert_db(name,passwd,eadd,utag):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""INSERT INTO human(name,passwd,email,usertag) VALUES( %s, %s, %s, %s)"""
        data=(name,passwd,eadd,utag)
        cursor.execute(query,data)
        mydb.commit()
        cursor.close()

@app.route("/", methods=["POST","GET"])
def log_in():
    if request.method=="POST":
        session.permanent=True # Reinforces line 13, false logs you out when exiting browser/tab
        uid=request.form['utag']
        passwd=request.form['pass']
        session['user_id']=uid
        session['pwd']=passwd
        results=if_exists(uid, passwd)
        if len(results)==1:
            return redirect(url_for("user_profile"))
        else:
            return redirect("/registration")
    else:
         return render_template("index.html")

@app.route("/registration", methods=["GET", "POST"])
def register_now():
    if request.method=="POST":
        uname=request.form['name']
        passwd=request.form['pass']
        usertag=request.form['utag']
        eadd=request.form['e_mail']
        insert_db(uname,passwd,eadd,usertag)
        return redirect("/")
    return render_template("register.html")

@app.route("/profile")
def user_profile():
    if "user_id" in session:
        user=session["user_id"]
        #return "Welcome "+ f"<h1>{user}!</h1>"
        return render_template("profile.html")
    return redirect("/")

@app.route("/logout")
def log_out():
    session.pop("user_id",None)
    return redirect(url_for("log_in"))

@app.route("/delete")
def delete_user():
    if "user_id" in session:
        if mydb.is_connected():
            query="""DELETE FROM human WHERE usertag=%s"""
            data=(session['user_id'],)
            cursor=mydb.cursor()
            cursor.execute(query,data)
            mydb.commit()
            cursor.close()
        else:
            return "Error connecting to database!"
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0",port="1234",debug=True)
