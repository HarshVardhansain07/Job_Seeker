import os
from flask import Flask, render_template, request, redirect
from datetime import datetime
import sys

# allow import from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import database
import Analysischart

# ✅ FIX: Correct template & static paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# create table
database.create_table()


# ---------------- HOME ----------------
@app.route("/")
def home():
    data = database.view_data()
    return render_template("home.html", data=data)


# ---------------- ADD ----------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        database.add_data(
            request.form['Company_Name'],
            request.form['HR_Email'],
            request.form['Role'],
            request.form['Status'],
            request.form['Website_link']
        )
        return redirect("/")
    
    return render_template("add_form.html")


# ---------------- UPDATE STATUS ----------------
@app.route("/update", methods=["POST"])
def update():
    Id = request.form.get("Id")
    status = request.form.get("status")

    print(f"Updating Id: {Id}, Status: {status}")  # Debug

    if Id and status:
        database.update_status(status, Id)

    return redirect("/")


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


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)