import mysql.connector


def get_all_teacher_details():
    global cursor
    query = """
    SELECT 
        Users.id_number AS teacher_id,
        Users.name AS teacher_name,
        Users.email AS teacher_email,
        Users.password AS teacher_password,
        Workers.salary AS teacher_salary,
        Teachers.subject AS teacher_subject
    FROM Users
    JOIN Workers ON Users.id_number = Workers.worker_id
    JOIN Teachers ON Workers.worker_id = Teachers.teacher_id
    WHERE Users.role = 'Teacher';
    """

    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # עדכן לפי מסד הנתונים שלך
        password="Koki.2002",  # עדכן לפי מסד הנתונים שלך
        database="testdatabase"  # עדכן לפי מסד הנתונים שלך
    )

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        teachers = cursor.fetchall()
        for teacher in teachers:
            print(f"ID: {teacher['teacher_id']}, Name: {teacher['teacher_name']}, Email: {teacher['teacher_email']}, "
                  f"Password: {teacher['teacher_password']}, Salary: {teacher['teacher_salary']}, Subject: {teacher['teacher_subject']}")
    except Exception as e:
        print(f"Error fetching teacher details: {e}")
    finally:
        cursor.close()
        connection.close()

# קריאה לפונקציה
get_all_teacher_details()