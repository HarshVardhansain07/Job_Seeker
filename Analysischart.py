from database import get_connection


def stats(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM public.list
        WHERE user_id = %s
        GROUP BY status
    """, (user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {row[0]: row[1] for row in data}
def date_chart(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date_applied, COUNT(*)
        FROM public.list
        WHERE user_id = %s
        GROUP BY date_applied
        ORDER BY date_applied
    """, (user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {row[0]: row[1] for row in data}