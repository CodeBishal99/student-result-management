import sqlite3

def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll INTEGER UNIQUE,
        marks REAL
    )
    """)

    conn.commit()
    conn.close()


def add_student(name, roll, marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students(name, roll, marks) VALUES (?, ?, ?)",
            (name, roll, marks)
        )
        conn.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Roll number already exists.")

    conn.close()


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return rows


def search_student(roll):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll=?",
        (roll,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


def delete_student(roll):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll=?",
        (roll,)
    )

    conn.commit()
    conn.close()

    print("Student deleted successfully.")