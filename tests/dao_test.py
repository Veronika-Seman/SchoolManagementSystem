from data_access.student_dao import StudentDAO
from data_access.teacher_dao import TeacherDAO
from data_access.user_dao import UserDAO

from data_access.user_dao import UserDAO
"""
user_dao = UserDAO()

user_id = "123456789"
user = user_dao.get_user_by_id(user_id)

if user:
    print(f"User found: ID={user['id_number']}, Name={user['name']}, Email={user['email']}, Role={user['role']}")
else:
    print(f"No user found with ID {user_id}.")

def display_student_schedule(student_id, student_dao):

    try:
        schedule = student_dao.get_schedule(student_id)
        if not schedule:
            print(f"No schedule found for student ID {student_id}.")
            return

        print(f"Schedule for Student ID {student_id}:")
        for entry in schedule:
            print(f"Day: {entry['day']}, Hour: {entry['hour']}, Course: {entry['course_name']}, Classroom: {entry['classroom_name']}")

    except Exception as e:
        print(f"Error displaying schedule for student ID {student_id}: {e}")

student_dao = StudentDAO()
student_id = "S000003"
display_student_schedule(student_id, student_dao)
"""
from data_access.admin_dao import AdminDAO

admin_dao = AdminDAO()

try:
    admin_dao.create_user_with_role(
        creator_role="Admin",
        id_number="MW00001",
        name="Jane Maintenance",
        email="jane.maintenance@example.com",
        password="securemaint123",
        role="MaintenanceWorker",
        salary=3500
    )
    print("Maintenance worker created successfully.")
except Exception as e:
    print(f"Error creating maintenance worker: {e}")




"""
    admin_dao.create_user_with_role(
        creator_role="Admin",
        id_number="T010001",
        name="Teacher User",
        email="teacher.user@example.com",
        password="teacher123",
        role="Teacher",
        salary=7000,
        subject="Mathematics"
    )
    print("Teacher created successfully.")

    admin_dao.create_user_with_role(
        creator_role="Admin",
        id_number="MW010001",
        name="Maintenance Worker",
        email="maintenance.user@example.com",
        password="maintenance123",
        role="MaintenanceWorker",
        salary=5000
    )
    print("Maintenance Worker created successfully.")
"""


