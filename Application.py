from datetime import datetime, timedelta
import pandas as pd
from read_csv import load_data, save_data

def add_List(company, role, email, status):

    df = load_data()
    today = datetime.today()

    # follow-up logic
    if status in ["Applied", "No reply"]:
        follow_up = today + timedelta(days=7)
        follow_up_date = follow_up.strftime('%d-%m-%Y')
    else:
        follow_up_date = "--"

    new_row = {
        "Company_Name": company,
        "HR_Email": email,
        "Role": role,
        "Status": status,
        "Date applied": today.strftime('%d-%m-%Y'),
        "Last follow-up date": follow_up_date
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)

    print("List Updated!")