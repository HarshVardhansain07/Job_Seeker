# Job_Seeker
Job Tracker with CRUD operations and analytics dashboard.

-- Features

- ✅ Add new job applications  
- 📊 View all applications in a dashboard  
- 🔄 Update application status (Applied / Interview / Rejected / No Reply)  
- ⚡ Auto-update follow-up dates  
- ❌ Delete applications instantly  
- 📈 Analytics page (status-wise insights)  
- 🎯 Clean and responsive UI  

---

- Tech Stack

- **Backend:** Flask (Python)
- **Data Handling:** Pandas
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Storage:** CSV file

---

## 📂 Project Structure
Job_Seeker/
│
├── Frontend/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── add_form.html
│   │   └── analytics.html
│   │
│   ├── static/
│   │   ├── base.css
│   │   ├── view.css
│   │   └── add_application_form.css
│
├── read_csv.py
├── Application.py
├── status.py
├── applications.csv
