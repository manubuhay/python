from flask import Flask,request,render_template,redirect,session,url_for
import os
from datetime import timedelta
import query_db as qDB

app=Flask(__name__)
app.secret_key="!@#$%"
app.permanent_session_lifetime= timedelta(hours=5)

@app.route("/", methods=["POST","GET"])
def log_in():
    err_msg=""
    if request.method=="POST":
        if all((request.form['utag'],request.form['pass'])):
            session.permanent=True # Reinforces line 8, false logs you out when exiting browser/tab
            uid=request.form['utag']
            passwd=request.form['pass']
            results=qDB.ifexists_db(uid, passwd)
            if results: # If authenticated, save session data, if declared out of this
                session['user_id']=uid # "if statement", it will save POST data and will direct you to /profile
                return redirect(url_for("user_profile",user=session['user_id'])) # even if user doesn't exist in DB
            return redirect("/registration")
        err_msg="Missing Values!"
    else:
        if "user_id" in session:
            return redirect(url_for("user_profile",user=session['user_id']))
    return render_template("index.html",error=err_msg)

@app.route("/registration", methods=["GET", "POST"])
def register_now():
    err_msg=""
    if request.method=="POST":
        uname=request.form['name']
        passwd=request.form['pass']
        usertag=request.form['utag']
        eadd=request.form['e_mail']
        if not all((uname,passwd,usertag,eadd)): #Makes sure all form inputs are not empty
            err_msg="Value/s are missing!"
        else:
            qDB.insert_db(uname,passwd,eadd,usertag) #Inserts values if none are empty
            return redirect("/")
    else:
        if "user_id" in session:
            return redirect(url_for("user_profile",user=session['user_id']))
    return render_template("register.html",error=err_msg)

@app.route("/profile/<user>")
def user_profile(user):
    if "user_id" in session:
        return render_template("profile.html",user=session["user_id"]) # Pass user as parameter to diplay in HTML
    return redirect("/")                                               # page, you can also just use session data

@app.route("/logout")
def log_out():
    session.pop("user_id",None)
    return redirect(url_for("log_in"))

@app.route("/delete")
def delete_user():
    if "user_id" in session:
        qDB.remove_db(session['user_id']) # Remove user in DB first before popping session otherwise parameter
        session.pop("user_id",None)   # in remove_db will be empty, "None" will prevent raising error
    else:                             # keyError if the key at the first parameter is not found in the session
        return "Error connecting to database!"
    return redirect("/")

@app.route("/update", methods=["POST","GET"])
def update_user(): # "usertag" will be readonly in "update_details.html", to preserve session data
    if "user_id" in session:
        results=qDB.fetchuser_db(session['user_id'])
        if request.method=="POST":
            uname=request.form['up_name']
            passwd=request.form['up_pass']
            usertag=request.form['up_utag'] # For logic to make usertag editable, edit usertag, after POST
            eadd=request.form['up_email']   # request, pop the session, redirect back to "index.html"
            if not all((uname,passwd,usertag,eadd)):
                return "Values cannot be empty!"
            else:
                qDB.update_db(uname,passwd,eadd,usertag,session['user_id'])
                results=qDB.fetchuser_db(session['user_id']) # Pass values to display on "update_details.html"
        return render_template("update_details.html",results=results)
    else:
        return redirect(url_for("log_in"))

if __name__=="__main__":
    app.run(host="0.0.0.0",port="1234",debug=True)
