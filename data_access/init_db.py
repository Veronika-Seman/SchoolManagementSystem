from data_access.data_operations import execute_query
"""
Database Schema Creation Script

This script defines and creates the necessary tables for a school management system using MySQL.
It ensures the structure is in place to support user management, courses, payments, and 
maintenance operations.

### Functionality:
- Defines multiple tables such as `Users`, `Workers`, `Teachers`, `Students`, `Courses`, `Payments`, etc.
- Uses `execute_query` to execute SQL commands and handle errors.
- Supports relationships between entities using `FOREIGN KEY` constraints.

### Table Descriptions:
- **Users**: Stores basic user information, including ID, name, email, password, and role.
- **Workers**: Extends `Users` to store salary details for employees.
- **Teachers**: Extends `Workers` to store subject expertise.
- **MaintenanceWorkers**: Extends `Workers` for maintenance staff.
- **Admins**: Extends `Workers` and includes a budget field.
- **Students**: Stores student details with optional parent references.
- **Parents**: Stores information about parents who can manage student payments.
- **Courses**: Stores course details such as name, assigned teacher, student capacity, and cost.
- **Waitlist**: Manages students waiting to enroll in courses.
- **MaintenanceTasks**: Tracks maintenance tasks assigned to maintenance workers.
- **Payments**: Records payments made by parents for courses.
- **StudentCourses**: Many-to-many relationship table linking students to their enrolled courses.
- **Classes**: Defines classrooms where courses are conducted.
- **Grades**: Stores student grades per course.
- **Schedules**: Manages the schedule of courses, including day, time, and classroom.

### Functions:
- `create_*_table()`: Creates individual tables if they do not exist.
- `create_all_tables()`: Calls all table creation functions to ensure the full schema is created.

### Execution:
When run as a standalone script, `create_all_tables()` is executed to generate all tables 
in the database.

This script ensures a structured and relational database model to support the school's operations.
"""

def create_users_table():
    query = """
    CREATE TABLE IF NOT EXISTS Users (
        id_number VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(30) NOT NULL,
        role ENUM('Student', 'Parent', 'Teacher', 'Admin', 'MaintenanceWorkers') NOT NULL
    );
    """
    execute_query(query, "Users table created successfully.")


def create_workers_table():
    query = """
    CREATE TABLE IF NOT EXISTS Workers (
        worker_id VARCHAR(20) PRIMARY KEY,      
        salary DECIMAL(10, 2) NOT NULL,         
        FOREIGN KEY (worker_id) REFERENCES Users(id_number)
    );
    """
    execute_query(query, "Workers table created successfully.")


def create_teachers_table():
    query = """
    CREATE TABLE IF NOT EXISTS Teachers (
        teacher_id VARCHAR(20) PRIMARY KEY,
        subject VARCHAR(50) NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES Workers(worker_id)
    );
    """
    execute_query(query, "Teachers table created successfully.")


def create_maintenance_workers_table():
    query = """
    CREATE TABLE IF NOT EXISTS MaintenanceWorkers (
        maintenance_worker_id VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (maintenance_worker_id) REFERENCES Workers(worker_id)
    );
    """
    execute_query(query, "Maintenance Workers table created successfully.")


def create_admins_table():
    query = """
    CREATE TABLE IF NOT EXISTS Admins (
        admin_id VARCHAR(20) PRIMARY KEY,    
        budget DECIMAL(15, 2) NOT NULL,          
        FOREIGN KEY (admin_id) REFERENCES Workers(worker_id)
    );
    """
    execute_query(query, "Admins table created successfully.")


def create_students_table():
    query = """
    CREATE TABLE IF NOT EXISTS Students (
        student_id VARCHAR(20) PRIMARY KEY,
        parent_id VARCHAR(20) NULL,
        FOREIGN KEY (student_id) REFERENCES Users(id_number),
        FOREIGN KEY (parent_id) REFERENCES Users(id_number)
    );
    """
    execute_query(query, "Students table created successfully.")


def create_parents_table():
    query = """
    CREATE TABLE IF NOT EXISTS Parents (
        parent_id VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (parent_id) REFERENCES Users(id_number)
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
        FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
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
        FOREIGN KEY (student_id) REFERENCES Students(student_id)
    );
    """
    execute_query(query, "Wait list table created successfully.")

def create_maintenance_tasks_table():
    query = """
    CREATE TABLE IF NOT EXISTS MaintenanceTasks (
        task_id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(150) NOT NULL,
        status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
        maintenance_worker_id VARCHAR(20),
        FOREIGN KEY (maintenance_worker_id) REFERENCES MaintenanceWorkers(maintenance_worker_id)
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
        FOREIGN KEY (parent_id) REFERENCES Parents(parent_id),
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
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    execute_query(query, "Student Courses table created successfully.")


def create_classes_table():
    query = """
    CREATE TABLE IF NOT EXISTS Classes (
        class_id INT AUTO_INCREMENT PRIMARY KEY,
        course_id INT NOT NULL,
        classroom_name VARCHAR(50) NOT NULL,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """
    execute_query(query, "Classes table created successfully.")


def create_grades_table():
    query = """
    CREATE TABLE IF NOT EXISTS Grades (
    student_id VARCHAR(20) NOT NULL,
    course_id INT NOT NULL,
    grade DECIMAL(5, 2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
    """
    execute_query(query, "Grades table created successfully.")
def create_schedules_table():
    query = """
    CREATE TABLE IF NOT EXISTS Schedules (
        schedule_id INT AUTO_INCREMENT PRIMARY KEY,
        course_id INT NOT NULL,
        class_id INT NOT NULL,
        course_name VARCHAR(50) NOT NULL,
        student_id VARCHAR(20) NOT NULL,
        day ENUM('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') NOT NULL,
        hour TIME NOT NULL,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id),
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (class_id) REFERENCES Classes(class_id)
    );
    """
    execute_query(query, "Schedules table created successfully.")

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
    create_grades_table()
    create_schedules_table()

if __name__ == "__main__":
    create_all_tables()
