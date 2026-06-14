Job_Seeker

A Flask-based Job Application Tracker that helps users manage job applications, track statuses, and visualize progress through an analytics dashboard.

⸻

Features

* ✅ Add new job applications
* 📋 View all applications in a centralized dashboard
* 🔄 Update application status
    * Applied
    * Interview
    * Rejected
    * No Reply
* ❌ Delete applications instantly
* 📊 Analytics dashboard with status-wise insights
* 🎯 Clean and responsive user interface
* 🔐 Secure database configuration using environment variables (.env)

⸻

Tech Stack

Backend

* Python
* Flask

Database

* MySQL
* MySQL Connector Python

Data Analysis

* Pandas

Frontend

* HTML
* CSS
* Jinja2 Templates

Environment Management

* python-dotenv

⸻

Project Structure

Job_Seeker/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── app.py
├── database.py
├── Analysischart.py
│
├── api/
│   └── index.py
│
└── Frontend/
    │
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── add_form.html
    │   └── analytics.html
    │
    └── static/
        ├── base.css
        ├── view.css
        ├── analytics.css
        ├── add_application_form.css
        └── favicon.ico

⸻

Database Schema

Table: List

Column	Type
Id	INT (Primary Key)
Company_Name	VARCHAR(255)
HR_Email	VARCHAR(255)
Date_applied	DATE
Status	VARCHAR(100)
Role	VARCHAR(255)
Website_link	VARCHAR(500)

⸻

Environment Variables

Create a .env file in the project root:

DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=companies_db

⸻

Installation

Clone Repository

git clone https://github.com/your-username/Job_Seeker.git
cd Job_Seeker

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

⸻

Run the Application

python app.py

Application will be available at:

http://127.0.0.1:5000

⸻

Future Improvements

* User authentication
* Resume upload support
* Email reminders for follow-ups
* Company-wise analytics
* Search and filtering options
* Cloud deployment (AWS)

⸻

Author

Harsh Vardhan