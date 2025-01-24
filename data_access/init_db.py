from data_access.data_operations import execute_query

def create_users_table():
    query = """
    CREATE TABLE IF NOT EXISTS Users (
        id_number VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(30) NOT NULL,
        role ENUM('Student', 'Parent', 'Teacher', 'Admin', 'GeneralWorker') NOT NULL
    );
    """
    execute_query(query, "Users table created successfully.")

def create_workers_table():
    query = """
    CREATE TABLE IF NOT EXISTS Workers (
        id_number VARCHAR(20) PRIMARY KEY,      
        salary DECIMAL(10, 2) NOT NULL,         
        FOREIGN KEY (id_number) REFERENCES Users(id_number) 
    );
    """
    execute_query(query, "Workers table created successfully.")

def create_teachers_table():
    query = """
    CREATE TABLE IF NOT EXISTS Teachers (
        id_number VARCHAR(20) PRIMARY KEY,
        subject VARCHAR(50) NOT NULL,
        FOREIGN KEY (id_number) REFERENCES Workers(id_number)
    );
    """
    execute_query(query, "Teachers table created successfully.")

def create_maintenance_workers_table():
    query = """
    CREATE TABLE IF NOT EXISTS MaintenanceWorkers (
        id_number VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (id_number) REFERENCES Workers(id_number)
    );
    """
    execute_query(query, "Maintenance Workers table created successfully.")

def create_admins_table():
    query = """
        CREATE TABLE IF NOT EXISTS Admins (
            id_number VARCHAR(20) PRIMARY KEY,    
            budget DECIMAL(15, 2) NOT NULL,          
            FOREIGN KEY (id_number) REFERENCES Workers(id_number) 
        );
        """
    execute_query(query, "Admins table created successfully.")

def create_students_table():
    query = """
    CREATE TABLE IF NOT EXISTS Students (
        id_number VARCHAR(20) PRIMARY KEY,
        parent_id VARCHAR(20) NOT NULL,
        class_id VARCHAR(20) NOT NULL, #למחוק
        FOREIGN KEY (id_number) REFERENCES Users(id_number),
        FOREIGN KEY (parent_id) REFERENCES Users(id_number)
    );
    """
    execute_query(query, "Students table created successfully.")

def create_parents_table():
    query = """
    CREATE TABLE IF NOT EXISTS Parents (
        id_number VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (id_number) REFERENCES Users(id_number)
    );
    """
    execute_query(query, "Parents table created successfully.")


def create_courses_table():
    query = """
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(50) NOT NULL,
        teacher_id VARCHAR(20) NOT NULL,
        max_students INT NOT NULL,
        cost DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES Teachers(id_number)
    );
    """
    execute_query(query, "Courses table created successfully.")

def create_waitlist_table():
    query = """
    CREATE TABLE IF NOT EXISTS Waitlist (
        waitlist_id INT AUTO_INCREMENT PRIMARY KEY,
        course_id INT NOT NULL,
        student_id VARCHAR(20) NOT NULL,
        position INT NOT NULL,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id),
        FOREIGN KEY (student_id) REFERENCES Students(id_number)
    );
    """
    execute_query(query, "Wait list table created successfully.")

def create_maintenance_tasks_table():
    query = """
    CREATE TABLE IF NOT EXISTS MaintenanceTasks (
        task_id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(150) NOT NULL,
        status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
        worker_id VARCHAR(20),
        FOREIGN KEY (worker_id) REFERENCES MaintenanceWorkers(id_number)
    );
    """
    execute_query(query, "Maintenance Tasks table created successfully.")

def create_payments_table():
    query = """
    CREATE TABLE IF NOT EXISTS Payments (
        payment_id INT AUTO_INCREMENT PRIMARY KEY,
        parent_id VARCHAR(20) NOT NULL,
        course_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        payment_date DATE NOT NULL,
        FOREIGN KEY (parent_id) REFERENCES Parents(id_number),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    execute_query(query, "Payments table created successfully.")

def create_student_courses_table():
    query = """
    CREATE TABLE IF NOT EXISTS StudentCourses (
        student_id VARCHAR(20) NOT NULL,
        course_id INT NOT NULL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES Students(id_number),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    execute_query(query, "Student Courses table created successfully.")

def create_classes_table():
    query = """
    CREATE TABLE IF NOT EXISTS Classes (
        class_id VARCHAR(20) PRIMARY KEY,
        course_id INT NOT NULL,
        classroom_name VARCHAR(50) NOT NULL,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    execute_query(query, "Classes table created successfully.")

def create_all_tables():
    create_users_table()
    create_workers_table()
    create_teachers_table()
    create_courses_table()
    create_admins_table()
    create_maintenance_workers_table()
    create_students_table()
    create_parents_table()
    create_waitlist_table()
    create_maintenance_tasks_table()
    create_payments_table()
    create_student_courses_table()
    create_classes_table()

if __name__ == "__main__":
    create_all_tables()
