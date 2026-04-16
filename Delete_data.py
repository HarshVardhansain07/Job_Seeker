from read_csv import save_data,load_data
def delete_data(index):
    df = load_data()

    if df.empty:
        return

    df = df.drop(index)
    df = df.reset_index(drop=True)

    save_data(df)