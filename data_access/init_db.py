import mysql

from data_access.sqlConnect import get_connection

def create_users_table():
    
    connection = get_connection()
    if connection is None:
        print("The table cannot be created due to a problem connecting to the database.")
        return

    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Users (
        id_number VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(30) NOT NULL,
        role ENUM('Student', 'Parent', 'Teacher', 'Admin', 'GeneralWorker') NOT NULL
    );
    """
    try:
        cursor.execute(create_table_query)
        print("Users table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        connection.close()

if __name__ == "__main__":
    create_users_table()

def create_teachers_table():

    connection = get_connection()
    if connection is None:
        print("The table cannot be created due to a problem connecting to the database.")
        return

    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Teachers (
        id_number VARCHAR(20) PRIMARY KEY,
        subject VARCHAR(50) NOT NULL,
        salary DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (id_number) REFERENCES Users(id_number)
    );
    """
    try:
        cursor.execute(create_table_query)
        print("Teachers table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        connection.close()

if __name__ == "__main__":
    create_teachers_table()

def create_courses_table():

    connection = get_connection()
    if connection is None:
        print("The table cannot be created due to a problem connecting to the database.")
        return

    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(100) NOT NULL,
        teacher_id VARCHAR(20) NOT NULL,
        max_students INT NOT NULL,
        cost DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES Teachers(id_number)
    );
    """
    try:
        cursor.execute(create_table_query)
        print("Courses table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        connection.close()

if __name__ == "__main__":
    create_courses_table()
