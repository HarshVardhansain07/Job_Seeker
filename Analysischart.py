import pandas as pd
import matplotlib.pyplot as plt
from read_csv import load_data

def chart():
    df = load_data()
    if df.empty:
        print("List is empty")
        return

    status_count = df['Status'].value_counts()
    plt.figure()
    status_count.plot(kind='pie',autopct='%1.1f%%')
    plt.title("Application Status Distribution")
    plt.ylabel("")
    plt.show()

