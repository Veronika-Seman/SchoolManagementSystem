from data_access.data_operations import BaseDAO

class WaitlistDAO(BaseDAO):
    """
        WaitlistDAO class for managing the course waitlist in the database.
        Provides methods for adding students to the waitlist, removing them, retrieving their positions, and assigning them to classes.
        Methods:
            add_to_waitlist(student_id, course_id):Adds a student to the waitlist for a specific course.
            get_student_position(student_id, course_id):Retrieves the position of a student in the waitlist for a specific course.
            remove_from_waitlist(student_id, course_id): Removes a student from the waitlist and updates the positions of other students.
            get_waitlist(course_id): Retrieves the waitlist for a specific course, sorted by position.
            notify_admin_if_waitlist_exceeds(course_id, threshold=5):Checks if the waitlist size exceeds a given threshold and notifies the admin.
            assign_student_to_class(course_id, class_id):Assigns the first student in the waitlist to a class and updates the waitlist.
            close(): Closes the DAO connection and cleans up associated resources.
        """


    def __init__(self):
        super().__init__()

    def add_to_waitlist(self, student_id, course_id):
        try:
            query_position = """
            SELECT IFNULL(MAX(position), 0) + 1 AS next_position
            FROM Waitlist
            WHERE course_id = %s
            """
            self.cursor.execute(query_position, (course_id,))
            result = self.cursor.fetchone()
            next_position = result["next_position"] if result else 1

            query_insert = """
            INSERT INTO Waitlist (course_id, student_id, position)
            VALUES (%s, %s, %s)
            """
            self.cursor.execute(query_insert, (course_id, student_id, next_position))
            self.connection.commit()

            print(f"Student {student_id} added to the waitlist for course {course_id} at position {next_position}.")
            return next_position

        except Exception as e:
            print(f"Error adding student to waitlist: {e}")
            return None

    def get_student_position(self, student_id, course_id):
        query = """
        SELECT position
        FROM Waitlist
        WHERE student_id = %s AND course_id = %s
        """
        try:
            self.cursor.execute(query, (student_id, course_id))
            result = self.cursor.fetchone()
            if result:
                return result['position']
            else:
                print(f"Student {student_id} is not in the waitlist for course {course_id}.")
                return None
        except Exception as e:
            print(f"Error fetching student position: {e}")
            return None

    def remove_from_waitlist(self, student_id, course_id):
        try:
            get_position_query = """
            SELECT position FROM Waitlist WHERE student_id = %s AND course_id = %s
            """
            self.cursor.execute(get_position_query, (student_id, course_id))
            result = self.cursor.fetchone()

            if not result:
                print(f"Student {student_id} is not in the waitlist for course {course_id}.")
                return

            student_position = result['position']

            delete_query = """
            DELETE FROM Waitlist WHERE student_id = %s AND course_id = %s
            """
            self.cursor.execute(delete_query, (student_id, course_id))

            update_query = """
            UPDATE Waitlist 
            SET position = position - 1
            WHERE course_id = %s AND position > %s
            """
            self.cursor.execute(update_query, (course_id, student_position))

            self.connection.commit()
            print(f"Student {student_id} removed from the waitlist for course {course_id}.")

        except Exception as e:
            print(f"Error removing student {student_id} from waitlist for course {course_id}: {e}")

    def get_waitlist(self, course_id):
        query = """
        SELECT student_id, position
        FROM Waitlist
        WHERE course_id = %s
        ORDER BY position
        """
        try:
            self.cursor.execute(query, (course_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching waitlist for course {course_id}: {e}")
            return []

    def notify_admin_if_waitlist_exceeds(self, course_id, threshold=5):
        query = """
        SELECT COUNT(*) AS count
        FROM Waitlist
        WHERE course_id = %s
        """
        try:
            self.cursor.execute(query, (course_id,))
            result = self.cursor.fetchone()
            if result and result['count'] > threshold:
                print(f"Waitlist for course {course_id} exceeds {threshold}. Notify admin to open a new class.")
        except Exception as e:
            print(f"Error checking waitlist size for course {course_id}: {e}")

    def assign_student_to_class(self, course_id, class_id):
        select_query = """
        SELECT student_id
        FROM Waitlist
        WHERE course_id = %s
        ORDER BY position
        LIMIT 1
        """
        delete_query = """
        DELETE FROM Waitlist
        WHERE student_id = %s AND course_id = %s
        """
        try:
            self.cursor.execute(select_query, (course_id,))
            result = self.cursor.fetchone()
            if result:
                student_id = result['student_id']

                enrollment_query = """
                INSERT INTO StudentCourses (student_id, course_id)
                VALUES (%s, %s)
                """
                self.cursor.execute(enrollment_query, (student_id, course_id))
                self.connection.commit()

                self.cursor.execute(delete_query, (student_id, course_id))
                self.connection.commit()

                self.cursor.execute("""
                UPDATE Waitlist
                SET position = position - 1
                WHERE course_id = %s
                """, (course_id,))
                self.connection.commit()

                print(f"Student {student_id} assigned to class {class_id} and removed from waitlist.")
        except Exception as e:
            print(f"Error assigning student to class for course {course_id}: {e}")

    def close(self):
        super().close()
