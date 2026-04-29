from flask import Flask, render_template, request
from flask import redirect
from datetime import datetime
import sys
import os
# allow import from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import database
import Analysischart

app = Flask(__name__)
database.create_table()
# Home (Dashboard)
@app.route("/")
def home():
 data = database.view_data()
 return render_template("home.html", data=data)


#  Add form
@app.route("/add", methods=["GET", "POST"])
def add():
        if request.method ==  'POST':
            database.add_data(
            request.form['Company_Name'],
            request.form['HR_Email'],
            request.form['Role'],
            request.form['Status'],
            request.form['Website_link']

            )
            return redirect("/") 
        return render_template("add_form.html")


@app.route("/update", methods=["POST"])

def update():

    Id = request.form.get("Id")
    status = request.form.get("status")
    print(f"Updating Id: {Id}, Status: {status}")  # Debugging log
    database.update_status(status, Id)

    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    Id = request.form.get("Id")  
    
    database.delete_data(int(Id))  
    return redirect("/")

@app.route("/analytics")
def analytics_page():
    data = database.view_data()
    stats = Analysischart.stats()
    date_a = Analysischart.date_chart()
    

    return render_template("analytics.html", data=data, stats=stats)


if __name__ == "__main__":
    app.run(debug=True)