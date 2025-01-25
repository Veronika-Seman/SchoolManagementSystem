from data_access.data_operations import BaseDAO

class CourseDAO(BaseDAO):
    def __init__(self):
        super().__init__()

    def update_course(self, course_id, course_name=None, teacher_id=None, max_students=None, cost=None):
        query = "UPDATE Courses SET "
        params = []
        if course_name:
            query += "course_name = %s, "
            params.append(course_name)
        if teacher_id:
            query += "teacher_id = %s, "
            params.append(teacher_id)
        if max_students:
            query += "max_students = %s, "
            params.append(max_students)
        if cost:
            query += "cost = %s, "
            params.append(cost)
        query = query.rstrip(", ") + " WHERE course_id = %s"
        params.append(course_id)
        try:
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print(f"Course ID {course_id} updated successfully.")
        except Exception as e:
            print(f"Error updating course ID {course_id}: {e}")

    def delete_course(self, course_id):
        query = "DELETE FROM Courses WHERE course_id = %s"
        try:
            self.cursor.execute(query, (course_id,))
            self.connection.commit()
            print(f"Course ID {course_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting course ID {course_id}: {e}")

    def get_course_by_id(self, course_id):
        query = "SELECT * FROM Courses WHERE course_id = %s"
        try:
            self.cursor.execute(query, (course_id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching course ID {course_id}: {e}")
            return None

    def get_all_courses(self):
        query = "SELECT * FROM Courses"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all courses: {e}")
            return []

    def close(self):
        super().close()
