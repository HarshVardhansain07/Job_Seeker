import pandas as pd 
file_path = "/Users/harshvardhan/Desktop/Job_Seeker/Company_list.csv"
def load_data():
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
         return pd.DataFrame(columns=[
             "Company_Name", 
             "Date applied",
             "Status", 
             "Role"
             "HR_Email",
             "Last follow-up"
            ])

def save_data(df):
    df.to_csv(file_path, index=False)