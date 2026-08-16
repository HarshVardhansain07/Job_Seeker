# Job_Seeker

A Flask-based Job Application Tracker that helps users manage job applications, track application statuses, and visualize progress through an analytics dashboard.

The application uses **Supabase PostgreSQL** for database storage and **Supabase Auth** for user authentication.

---

## Features

* ✅ User registration and login with Supabase Auth
* ✅ Add new job applications
* 📋 View personal job applications in a centralized dashboard
* 🔄 Update application status

  * Applied
  * Interview
  * Rejected
  * No Reply
* ❌ Delete applications instantly
* 📊 Analytics dashboard with status-wise insights
* 👤 User-specific application tracking
* 🎯 Clean and responsive user interface
* 🔐 Environment-based configuration for sensitive credentials
* 🗄️ PostgreSQL database hosted on Supabase

---

## Tech Stack

### Backend

* Python
* Flask
* Supabase Python Client

### Authentication

* Supabase Auth
* Email/password authentication
* Flask sessions

### Database

* PostgreSQL
* Supabase

### Data Analysis

* Pandas

### Frontend

* HTML
* CSS
* Jinja2 Templates

### Environment Management

* python-dotenv

---

## Project Structure

```text
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
└── Frontend/
    │
    ├── templates/
    │   ├── base.html
    │   ├── Login_form.html
    │   ├── Registration_form.html
    │   ├── home.html
    │   ├── add_form.html
    │   └── analytics.html
    │
    └── static/
        ├── base.css
        ├── login_form.css
        ├── registration.css
        ├── view.css
        ├── analytics.css
        ├── add_application_form.css
        └── favicon.ico
```

---

## Database Schema

The application uses **Supabase PostgreSQL**.

### Authentication

User authentication is handled by Supabase Auth:

```text
auth.users
```

Supabase manages user credentials and passwords, so the application does not store user passwords in its own table.

### Applications

Application data is stored in:

```text
public.list
```

| Column       | Type         | Description                 |
| ------------ | ------------ | --------------------------- |
| id           | BIGINT       | Primary key                 |
| user_id      | UUID         | References `auth.users(id)` |
| company_name | VARCHAR(255) | Company name                |
| hr_email     | VARCHAR(255) | HR/recruiter email          |
| date_applied | DATE         | Application date            |
| status       | VARCHAR(100) | Application status          |
| role         | VARCHAR(255) | Job role                    |
| website_link | VARCHAR(500) | Company/job website         |

Relationship:

```text
auth.users
    │
    │ id
    ↓
public.list
    │
    └── user_id
```

Each application is associated with the user who created it.

---

## Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_PUBLISHABLE_KEY=your_supabase_publishable_key
DATABASE_URL=your_postgresql_connection_string
SECURITY_KEY=your_flask_secret_key
```

### Important

Never commit `.env` to GitHub.

Make sure `.gitignore` contains:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Job_Seeker.git
cd Job_Seeker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Supabase Setup

Create a project on Supabase.

Then configure:

1. **Authentication → Providers → Email**
2. Enable email/password authentication.
3. Configure your authentication redirect URLs.
4. Create the `public.list` table.
5. Add the foreign key from `public.list.user_id` to `auth.users.id`.

For local development, the application uses:

```text
http://127.0.0.1:5000
```

or:

```text
http://localhost:5000
```

---

## Run the Application

Start the Flask application:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## Application Flow

```text
User
 │
 ├── Register
 │      ↓
 │   Supabase Auth
 │
 ├── Login
 │      ↓
 │   Supabase Auth
 │      ↓
 │   User UUID
 │
 └── Job Application Tracker
        │
        ├── Add application
        ├── View applications
        ├── Update status
        ├── Delete application
        └── View analytics
                 │
                 ↓
          Supabase PostgreSQL
```

---

## User Data Isolation

Each application is associated with a Supabase Auth user through:

```text
user_id
```

For example:

```text
User A
 ├── Google
 ├── Microsoft
 └── Amazon

User B
 ├── Apple
 └── Meta
```

The Flask application filters application data using the authenticated user's UUID.

Row Level Security (RLS) is planned as an additional database-level security layer.

---

## Analytics

The analytics dashboard provides insights into application statuses, including:

* Applied
* Interview
* Rejected
* No Reply

Analytics are calculated based on the currently authenticated user's applications.

---

## Deployment

The application is designed to be deployed as a Flask web application using a production WSGI server such as Gunicorn.

Supabase provides:

* PostgreSQL database
* User authentication
* Cloud database hosting

The Flask application can be deployed separately to a Python-compatible hosting platform.

---

## Future Improvements

* 🔐 Row Level Security (RLS)
* 📄 Resume upload support
* 📧 Email reminders for follow-ups
* 🏢 Company-wise analytics
* 🔎 Search and filtering
* 📱 Further UI/UX improvements
* ☁️ Production deployment
* 📈 More advanced analytics

---

## Author

**Harsh Vardhan**
