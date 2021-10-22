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

################################################################################
def if_exists(utag,pw):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""SELECT usertag, passwd FROM human WHERE usertag=%s AND passwd=%s"""
        data=(utag,pw)
        cursor.execute(query,data)
        #results=cursor.fetchall()
        results=cursor.fetchone()
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

def remove_db(utag):
    if mydb.is_connected():
        query="""DELETE FROM human WHERE usertag=%s"""
        data=(utag,)
        cursor=mydb.cursor()
        cursor.execute(query,data)
        mydb.commit()
        cursor.close()
################################################################################

@app.route("/", methods=["POST","GET"])
def log_in():
    if request.method=="POST":
        if all((request.form['utag'],request.form['pass'])):
        #if request.form['utag'] and request.form['pass']:
            session.permanent=True # Reinforces line 13, false logs you out when exiting browser/tab
            uid=request.form['utag']
            passwd=request.form['pass']
            results=if_exists(uid, passwd)
            #if len(results)==1:
            if results:
                session['user_id']=uid # If authenticated, save session data, if declared out of this
                session['pwd']=passwd  # "if statement", it will save POST data and will direct you to /profile
                return redirect(url_for("user_profile")) # even if user doesn't exist in DB
            return redirect("/registration")
        return "Missing Value/s!"
    else:
        if "user_id" in session:
            return redirect("/profile")
    return render_template("index.html")

@app.route("/registration", methods=["GET", "POST"])
def register_now():
    if request.method=="POST":
        uname=request.form['name']
        passwd=request.form['pass']
        usertag=request.form['utag']
        eadd=request.form['e_mail']
        if not all((uname,passwd,usertag,eadd)): #Makes sure all form inputs are not empty
            return "Missing Values!"
        insert_db(uname,passwd,eadd,usertag) #Inserts values if none are empty
        return redirect("/")
    else:
        if "user_id" in session:
            return redirect(url_for("user_profile"))
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
        remove_db(session['user_id']) # Remove user in DB first before popping session
        session.pop("user_id",None)   # otherwise parameter in remove_db will be empty
    else:
        return "Error connecting to database!"
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0",port="1234",debug=True)
