import sqlite3
from datetime import datetime
def get_connection():
    conn = sqlite3.connect('companies_list.db')
    return conn
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
             CREATE TABLE IF NOT EXISTS List
                 (Id INTEGER PRIMARY KEY,
                 Company_Name TEXT NOT NULL,
                 HR_Email TEXT NOT NULL,
                 Date_applied TEXT NOT NULL,
                 Status TEXT NOT NULL,
                 Role TEXT NOT NULL,
                 Website_link TEXT NOT NULL)
                 ''')
    conn.commit()
    conn.close()
def view_data():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM List")
        data = cursor.fetchall()
        conn.close()
        return data
    
    

def add_data(Company_Name,HR_Email,Role,Status,Website_link,Date_applied = None):
    conn = get_connection()
    cursor = conn.cursor()
    if not Date_applied:
        Date_applied = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO List(Company_Name,HR_Email,Role,Status,Website_link,Date_applied) VALUES (?,?,?,?,?,?)",(Company_Name,HR_Email,Role,Status,Website_link,Date_applied))
    conn.commit()
    conn.close()

def update_status(Status,Id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE List SET status = ? WHERE Id = ?",(Status,Id))
    conn.commit()
    conn.close()


def delete_data(Id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM List WHERE Id = ?",(Id,)) 
    conn.commit()
    conn.close()
