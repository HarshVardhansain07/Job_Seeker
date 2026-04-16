import pandas as pd
from read_csv import load_data
def view_data():
    df = load_data()
    if df.empty:
        print("No data Found.")
    else:
        print("Your Applications are :")
        print(df.to_string(index=False))