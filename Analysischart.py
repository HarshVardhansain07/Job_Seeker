from database import get_connection

def stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Status, COUNT(*) FROM List GROUP BY Status")
    data = cursor.fetchall()

    conn.close()

    # Convert to dictionary
    return {row[0]: row[1] for row in data}
def date_chart():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Date_applied,COUNT(*) FROM LIST GROUP BY Date_applied')
    data = cursor.fetchall()
    conn.close()

    # Convert to dictionary
    return {row[0]: row[1] for row in data}