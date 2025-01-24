import mysql.connector

def get_connection():
    """
    Creates a connection to the database
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )











def create_classes_table():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS Classes (
        class_id INT AUTO_INCREMENT PRIMARY KEY,
        course_id INT NOT NULL,
        classroom_name VARCHAR(50) NOT NULL,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    cursor.execute(query)
    print("Classes table created successfully.")
    connection.close()

if __name__ == "__main__":
    create_maintenance_workers_table()
    create_students_table()
    create_parents_table()
    create_waitlist_table()
    create_maintenance_tasks_table()
    create_payments_table()
    create_student_courses_table()
    create_classes_table()
