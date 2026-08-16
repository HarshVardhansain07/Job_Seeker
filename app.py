import os
from flask import Flask, render_template, request, redirect,flash
from datetime import datetime
import sys
import database
import Analysischart
from flask import Flask, session
from dotenv import load_dotenv
from supabase import create_client, Client
# allow import from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv()
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR,"Frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "Frontend","static")
)
app.secret_key = os.getenv("SECURITY_KEY")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# create table
database.create_table()
# ----------------Login ----------------
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            user = response.user
            auth_session = response.session

            if user and auth_session:
                session["user_id"] = user.id
                session["access_token"] = auth_session.access_token

                return redirect("/Home")

            flash("Invalid email or password")

        except Exception as e:
            print("Login error:", e)
            flash("Invalid email or password")

    return render_template("Login_form.html")

@app.route("/Registration_form", methods=["GET", "POST"])
def Registration():

    if request.method == "POST":

        email = request.form.get("Email")
        password = request.form.get("Password")

        if not email or not password:
            return render_template(
                "Registration_form.html",
                error="Email and password are required"
            )

        try:
            response = supabase.auth.sign_up({
                "email": email,
                "password": password
            })

            # If signup succeeds
            if response.user:
                return redirect("/")

            return render_template(
                "Registration_form.html",
                error="Registration failed"
            )

        except Exception as e:
            print("Registration error:", e)

            return render_template(
                "Registration_form.html",
                error="Email may already be registered"
            )

    return render_template("Registration_form.html")



# ----------------home----------------
@app.route("/Home")

def home():

    if "user_id" not in session:

        return redirect("/")

    data = database.view_data(session["user_id"])

    return render_template("home.html", data=data)

# ---------------- ADD ----------------
@app.route("/add", methods=["GET", "POST"])
def add():

    if "user_id" not in session:
        return redirect("/")

    if request.method == "POST":

        database.add_data(
            session["user_id"],
            request.form["Company_Name"],
            request.form["HR_Email"],
            request.form["Role"],
            request.form["Status"],
            request.form["Website_link"]
        )

        return redirect("/Home")

    return render_template("add_form.html")


# ---------------- UPDATE STATUS ----------------
@app.route("/update", methods=["POST"])
def update():

    if "user_id" not in session:
        return redirect("/")

    Id = request.form.get("Id")
    status = request.form.get("status")

    if Id and status:

        database.update_status(
            status,
            int(Id),
            session["user_id"]
        )

    return redirect("/Home")

# ---------------- DELETE ----------------
@app.route("/delete", methods=["POST"])
def delete():

    if "user_id" not in session:
        return redirect("/")

    Id = request.form.get("Id")
    User_Id = session.get("user_id")

    if Id and User_Id:
        database.delete_data(
            int(Id),
            User_Id
        )

    return redirect("/Home")


# ---------------- ANALYTICS ----------------
@app.route("/analytics")
def analytics_page():

    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]

    data = database.view_data(user_id)
    stats = Analysischart.stats(user_id)

    return render_template(
        "analytics.html",
        data=data,
        stats=stats
    )
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)