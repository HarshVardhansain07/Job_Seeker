from read_csv import load_data, save_data
from datetime import datetime, timedelta

def update_status(index, selected_status):
    df = load_data()

    df.loc[index, "Status"] = selected_status

    if selected_status in ["Applied", "No reply"]:
        follow_up = datetime.today() + timedelta(days=7)
        df.loc[index, "Last follow-up date"] = follow_up.strftime('%d-%m-%Y')
    else:
        df.loc[index, "Last follow-up date"] = "--"

    save_data(df)