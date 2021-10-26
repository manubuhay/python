from flask import Flask,request,render_template,redirect,session,url_for
import os
import mysql.connector as dtb
from datetime import timedelta

mydb=dtb.connect(host="codebase"
                ,user="python"
                ,password="Python_123"
                ,database="socmed")

app=Flask(__name__)
app.secret_key="!@#$%"
app.permanent_session_lifetime= timedelta(hours=5)

################################################################################
def ifexists_db(utag,pw):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""SELECT usertag, passwd FROM user_data WHERE usertag=%s AND passwd=%s"""
        data=(utag,pw)
        cursor.execute(query,data)
        #results=cursor.fetchall()
        results=cursor.fetchone()
        cursor.close()
        return results

def insert_db(name,passwd,eadd,utag):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""INSERT INTO user_data(name,passwd,email,usertag) VALUES( %s, %s, %s, %s)"""
        data=(name,passwd,eadd,utag)
        cursor.execute(query,data)
        mydb.commit()
        cursor.close()

def remove_db(utag):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""DELETE FROM user_data WHERE usertag=%s"""
        data=(utag,)
        cursor.execute(query,data)
        mydb.commit()
        cursor.close()

def update_db(name,passwd,eadd,utag,old_utag):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""UPDATE user_data SET name=%s, passwd=%s, email=%s, usertag=%s WHERE usertag=%s"""
        data=(name,passwd,eadd,utag,old_utag)
        cursor.execute(query,data)
        mydb.commit()
        cursor.close()

def fetchuser_db(utag):
    if mydb.is_connected():
        cursor=mydb.cursor()
        query="""SELECT * FROM user_data WHERE usertag=%s"""
        data=(utag,)
        cursor.execute(query,data)
        results=cursor.fetchone()
        return results
################################################################################

@app.route("/", methods=["POST","GET"])
def log_in():
    if request.method=="POST":
        if all((request.form['utag'],request.form['pass'])):
        #if request.form['utag'] and request.form['pass']:
            session.permanent=True # Reinforces line 13, false logs you out when exiting browser/tab
            uid=request.form['utag']
            passwd=request.form['pass']
            results=ifexists_db(uid, passwd)
            #if len(results)==1:
            if results:
                session['user_id']=uid    # If authenticated, save session data, if declared out of this
                session['is_logged']=True # "if statement", it will save POST data and will direct you to /profile
                return redirect(url_for("user_profile",user=session['user_id'])) # even if user doesn't exist in DB
            return redirect("/registration")
        return "Missing Value/s!"
    else:
        if "user_id" in session:
            return redirect(url_for("user_profile",user=session['user_id']))
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
            return redirect(url_for("user_profile",user=session['user_id']))
    return render_template("register.html")

@app.route("/profile/<user>")
def user_profile(user):
    if "user_id" in session:
        user=session["user_id"]
        #return "Welcome "+ f"<h1>{user}!</h1>"
        return render_template("profile.html",user=session['user_id']) # Pass user as parameter to diplay in HTML
    return redirect("/")                                               # page, you can also just use session data

@app.route("/logout")
def log_out():
    session.pop("user_id",None)
    return redirect(url_for("log_in"))

@app.route("/delete")
def delete_user():
    if "user_id" in session:
        remove_db(session['user_id']) # Remove user in DB first before popping session otherwise parameter
        session.pop("user_id",None)   # in remove_db will be empty, "None" will prevent raising error
    else:                             # keyError if the key at the first parameter is not found in the session
        return "Error connecting to database!"
    return redirect("/")

@app.route("/update", methods=["POST","GET"])
def update_user(): # "usertag" will be readonly in "update_details.html", to preserve session data
    if "user_id" in session:
        results=fetchuser_db(session['user_id'])
        if request.method=="POST":
            uname=request.form['up_name']
            passwd=request.form['up_pass']
            usertag=request.form['up_utag'] # For logic to make usertag editable, edit usertag, after POST
            eadd=request.form['up_email']   # request, pop the session, redirect back to "index.html"
            if not all((uname,passwd,usertag,eadd)):
                return "Values cannot be empty!"
            else:
                update_db(uname,passwd,eadd,usertag,session['user_id'])
                results=fetchuser_db(session['user_id']) # Pass values to display on "update_details.html"
        return render_template("update_details.html",results=results)
    else:
        return redirect(url_for("log_in"))

if __name__=="__main__":
    app.run(host="0.0.0.0",port="1234",debug=True)
