from flask import Flask, render_template, request
from flask import redirect
import sys
import os
# allow import from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from read_csv import load_data, save_data
from Application import add_List
from Delete_data import delete_data

app = Flask(__name__)

# Home (Dashboard)
@app.route("/")
def home():
    try:
        df = load_data()
        data = df.to_dict(orient="records")
    except:
        data = []

    return render_template("home.html", data=data)


#  Add form
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        email = request.form["email"]
        status = request.form["status"]

        add_List(company, role, email, status)

        return redirect("/") 

    return render_template("add_form.html")
@app.route("/update_status", methods=["POST"])
def update_status():
    index = int(request.form["index"])
    new_status = request.form["status"]

    df = load_data()

    df.loc[index, "Status"] = new_status

    from datetime import datetime, timedelta

    if new_status in ["Applied", "No reply"]:
        follow_up = datetime.today() + timedelta(days=7)
        df.loc[index, "Last follow-up date"] = follow_up.strftime('%d-%m-%Y')
    else:
        df.loc[index, "Last follow-up date"] = "--"

    save_data(df)

    return redirect("/")
@app.route("/delete", methods=["POST"])
def delete():
    index = int(request.form["index"])

    delete_data(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)