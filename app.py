import os
from flask import Flask, render_template, request, redirect,flash
from datetime import datetime
import sys
import database
import Analysischart
from flask import Flask, session
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
# allow import from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR,"Frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "Frontend","static")
)
load_dotenv()
app.secret_key = os.getenv("SECURITY_KEY")

# create table
database.User_table()
database.create_table()
# ---------------- HOME ----------------
@app.route("/",methods= ["GET","POST"])
def login():
    if request.method == "POST":
     
        Username= request.form['Username']
        Password= request.form['Password']
        User_Id = database.login(Username,Password)
        if User_Id:
            session["user_id"] = User_Id
            return redirect("/Home")
        
    
    return render_template("Login_form.html")


@app.route("/Registration_form", methods=["GET", "POST"])
def Registration():

    if request.method == "POST":

        result = database.Registration(
            request.form['Username'],
            request.form['Email'],
            request.form['Password']
        )

        if result == "User already exists":

            return render_template(
                "Registration_form.html",
                error="Username or Email already exists"
            )

        return redirect("/")

    return render_template("Registration_form.html")
    




@app.route("/Home")

def home():

    if "user_id" not in session:

        return redirect("/")

    data = database.view_data(session["user_id"])

    return render_template("home.html", data=data)

# ---------------- ADD ----------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        database.add_data(
            session["user_id"],
            request.form['Company_Name'],
            request.form['HR_Email'],
            request.form['Role'],
            request.form['Status'],
            request.form['Website_link']
        )
        return redirect("/Home")
    
    return render_template("add_form.html")


# ---------------- UPDATE STATUS ----------------
@app.route("/update", methods=["POST"])
def update():

    Id = request.form.get("Id")
    status = request.form.get("status")

    print(f"Updating Id: {Id}, Status: {status}")

    if Id and status:
        database.update_status(
            status,
            Id,
            session["user_id"]
        )

    return redirect("/Home")

# ---------------- DELETE ----------------
@app.route("/delete", methods=["POST"])
def delete():
    Id = request.form.get("Id")

    if Id:
        database.delete_data(int(Id))

    return redirect("/")


# ---------------- ANALYTICS ----------------
@app.route("/analytics")
def analytics_page():
    data = database.view_data()
    stats = Analysischart.stats()

    return render_template("analytics.html", data=data, stats=stats)
@app.route("/logout")

def logout():

    session.clear()

    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)