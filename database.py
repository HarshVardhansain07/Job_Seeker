import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt()
load_dotenv()

def get_connection():
    conn = mysql.connector.connect(
      host=os.getenv("DB_HOST"),

        user=os.getenv("DB_USER"),

        password=os.getenv("DB_PASSWORD"),

        database=os.getenv("DB_NAME")
    )
  
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `List` (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            User_Id INT NOT NULL,
            Company_Name VARCHAR(255) NOT NULL,
            HR_Email VARCHAR(255) NOT NULL,
            Date_applied DATE NOT NULL,
            Status VARCHAR(100) NOT NULL,
            Role VARCHAR(255) NOT NULL,
            Website_link VARCHAR(500) NOT NULL,
            
            FOREIGN KEY (User_Id)
                REFERENCES USERS(Id)
                ON DELETE CASCADE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def view_data(User_Id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM List

        WHERE User_Id = %s

    """, (User_Id,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def add_data(User_Id,Company_Name, HR_Email, Role, Status, Website_link, Date_applied=None):
    conn = get_connection()
    cursor = conn.cursor()

    if not Date_applied:
        Date_applied = datetime.today().strftime('%Y-%m-%d')

    cursor.execute(
        """
        INSERT INTO `List`
        (User_ID,
        Company_Name,
        HR_Email,
        Role,
        Status,
        Website_link,
        Date_applied
        )
        VALUES (%s,%s, %s, %s, %s, %s, %s)
        """,
        (User_Id,
        Company_Name,
        HR_Email,
        Role,
        Status,
        Website_link,
        Date_applied)
    )

    conn.commit()
    cursor.close()
    conn.close()


def update_status(Status, Id,User_Id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE `List` SET Status = %s WHERE Id = %s AND User_ID = %s",
        (Status, Id,User_Id)
    )

    conn.commit()
    cursor.close()
    conn.close()


def delete_data(Id,User_Id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM List WHERE Id = %s AND User_Id = %s",
        (Id,User_Id)
    )

    conn.commit()
    cursor.close()
    conn.close()   
# --------------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------* 
# User Table 

def User_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `USERS` (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            USERNAME VARCHAR(255) UNIQUE NOT NULL ,
            Mail VARCHAR(255)  UNIQUE NOT NULL,
            PASSWORD VARCHAR(500) NOT NULL
                    
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

    # Registration || Signup

def Registration(Username ,Mail, Password):     
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(

        """
        SELECT Id

        FROM USERS

        WHERE USERNAME = %s OR Mail = %s
        """,
        (Username, Mail)
    )
    existing_user = cursor.fetchone()

    if existing_user:

        cursor.close()

        conn.close()

        return "User already exists"
    if not Username or not Mail or not Password:
        cursor.close()
        conn.close()
        return "All fields are required"
    
    Passwords = bcrypt.generate_password_hash(Password).decode('utf-8')
    cursor.execute(
        """
        INSERT INTO `USERS`
        (Username,
        Mail,
        Password)
        VALUES (%s, %s, %s)
        """,
        (Username,
        Mail,
        Passwords)
    )

    conn.commit()
    cursor.close()
    conn.close()
    return "Success"

#  login 
def login(Username, Password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT Id,PASSWORD FROM USERS WHERE USERNAME = %s",
        (Username,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result is None:
        return None
    User_Id = result[0]
    stored_hash = result[1]
    
    if bcrypt.check_password_hash(stored_hash, Password):
        return User_Id
    return None

