import mysql.connector
from datetime import datetime

def get_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="harshME@855",
        database="companies_db"
    )
    print("Connected to companies_db")
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    print("Connected to MySQL")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `List` (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Company_Name VARCHAR(255) NOT NULL,
            HR_Email VARCHAR(255) NOT NULL,
            Date_applied DATE NOT NULL,
            Status VARCHAR(100) NOT NULL,
            Role VARCHAR(255) NOT NULL,
            Website_link VARCHAR(500) NOT NULL
        )
    """)

    conn.commit()
    print("Table creation query executed")
    cursor.close()
    conn.close()


def view_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `List`")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def add_data(Company_Name, HR_Email, Role, Status, Website_link, Date_applied=None):
    conn = get_connection()
    cursor = conn.cursor()

    if not Date_applied:
        Date_applied = datetime.today().strftime('%Y-%m-%d')

    cursor.execute(
        """
        INSERT INTO `List`
        (Company_Name, HR_Email, Role, Status, Website_link, Date_applied)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (Company_Name, HR_Email, Role, Status, Website_link, Date_applied)
    )

    conn.commit()
    cursor.close()
    conn.close()


def update_status(Status, Id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE `List` SET Status = %s WHERE Id = %s",
        (Status, Id)
    )

    conn.commit()
    cursor.close()
    conn.close()


def delete_data(Id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM `List` WHERE Id = %s",
        (Id,)
    )

    conn.commit()
    cursor.close()
    conn.close()