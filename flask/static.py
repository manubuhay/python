from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home_page():
    return "This is the homepage!" + "<h1>HOME</h1>"

@app.route("/<name>") #Pass variable to function as parameter in URL
def user_page(name):
    return f"Hello {name}"

@app.route("/admin")
def admin_page():
    return redirect(url_for("home_page")) #Redirects
if __name__== "__main__":
    app.run(host="0.0.0.0")
