from data_access.sqlConnect import get_connection

class AdminDAO:
    def __init__(self):
        self.connection = get_connection()
        if self.connection:
            self.cursor = self.connection.cursor(dictionary=True)

    def create_user(self, id_number, name, email, password, role):
        query = """
        INSERT INTO Users (id_number, name, email, password, role)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (id_number, name, email, password, role))
            self.connection.commit()
        except Exception as e:
            print(f"Error creating user: {e}")

    def create_course(self, course_name, teacher_id, max_students, cost):
        query = """
        INSERT INTO Courses (course_name, teacher_id, max_students, cost)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (course_name, teacher_id, max_students, cost))
            self.connection.commit()
        except Exception as e:
            print(f"Error creating course: {e}")

    def assign_teacher_to_course(self, teacher_id, course_id):
        query = """
        UPDATE Courses
        SET teacher_id = %s
        WHERE course_id = %s
        """
        try:
            self.cursor.execute(query, (teacher_id, course_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error assigning teacher to course: {e}")

    def manage_waitlist(self, student_id, course_id, action):

        if action == 'add':
            query = """
            INSERT INTO Waitlist (student_id, course_id, position)
            VALUES (%s, %s, 
            (SELECT IFNULL(MAX(position), 0) + 1 FROM Waitlist WHERE course_id = %s))
            """
            try:
                self.cursor.execute(query, (student_id, course_id, course_id))
                self.connection.commit()
            except Exception as e:
                print(f"Error adding student to waitlist: {e}")
        elif action == 'remove':
            query = """
            DELETE FROM Waitlist
            WHERE student_id = %s AND course_id = %s
            """
            try:
                self.cursor.execute(query, (student_id, course_id))
                self.connection.commit()
            except Exception as e:
                print(f"Error removing student from waitlist: {e}")

    def assign_task_to_worker(self, description, worker_id):
        query = """
        INSERT INTO MaintenanceTasks (description, status, assigned_worker_id)
        VALUES (%s, 'Pending', %s)
        """
        try:
            self.cursor.execute(query, (description, worker_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error assigning task to worker: {e}")

    def update_task_status(self, task_id, status):
        query = """
        UPDATE MaintenanceTasks
        SET status = %s
        WHERE task_id = %s
        """
        try:
            self.cursor.execute(query, (status, task_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error updating task status: {e}")

    def generate_financial_report(self):
        query = """
        SELECT 'Payments' AS category, SUM(amount) AS total
        FROM Payments
        UNION ALL
        SELECT 'Salaries', SUM(Workers.salary)
        FROM Workers
        JOIN Users ON Workers.id_number = Users.id_number
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating financial report: {e}")
            return []


    def close(self):

        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
