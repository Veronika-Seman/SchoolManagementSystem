import json
import random
from data_access import course_dao, studentCourses_dao
from data_access.admin_dao import AdminDAO
from data_access.class_dao import ClassDAO
from data_access.course_dao import CourseDAO
from data_access.maintenanceTasks_dao import MaintenanceTaskDAO
from data_access.parent_dao import ParentDAO
from data_access.sqlConnect import get_connection
from data_access.studentCourses_dao import StudentCoursesDAO
from data_access.student_dao import StudentDAO
from data_access.teacher_dao import TeacherDAO
from data_access.user_dao import UserDAO
from data_access.worker_dao import WorkerDAO
from data_access.maintenanceWorker_dao import MaintenanceWorkerDAO
from data_access.grades_dao import GradesDAO
from datetime import time
from data_access.data_operations import execute_query

"""
file_path = "teachers.json"

with open(file_path, "r") as json_file:
    data = json.load(json_file)
"""

"""
teacher_dao = TeacherDAO()

for teacher in data["teachers"]:
    teacher_id = teacher["teacher_id"]
    name = teacher["name"]
    email = teacher["email"]
    password = teacher["password"]
    salary = teacher["salary"]
    subject = teacher["subject"]

    if not teacher_dao.teacher_exists(teacher_id):
        try:
            teacher_dao.create_teacher(
                teacher_id=teacher_id,
                name=name,
                email=email,
                password=password,
                salary=salary,
                subject=subject
            )
        except Exception as e:
            print(f"Error adding teacher {teacher_id}: {e}")
    else:
        print(f"Teacher with ID {teacher_id} already exists. Skipping.")

teacher_dao.close()

"""
"""
maintenance_worker_dao = MaintenanceWorkerDAO()

def user_exists(cursor, id_number=None, email=None):
    if id_number:
        query_id = "SELECT 1 FROM Users WHERE id_number = %s"
        cursor.execute(query_id, (id_number,))
        if cursor.fetchone():
            return True

    if email:
        query_email = "SELECT 1 FROM Users WHERE email = %s"
        cursor.execute(query_email, (email,))
        if cursor.fetchone():
            return True

    return False

for worker in maintenance_workers_data["maintenance_workers"]:
    try:
        if user_exists(maintenance_worker_dao.cursor, id_number=worker["maintenance_worker_id"], email=worker["email"]):
            print(f"User with ID {worker['maintenance_worker_id']} or email {worker['email']} already exists. Skipping...")
            continue

        maintenance_worker_dao.create_maintenance_worker(
            maintenance_worker_id=worker["maintenance_worker_id"],
            name=worker["name"],
            email=worker["email"],
            password=worker["password"],
            salary=worker["salary"]
        )

    except Exception as e:
        print(f"Error adding Maintenance Worker {worker['maintenance_worker_id']}: {e}")
"""
"""
admin_dao = AdminDAO()

for teacher in data["teachers"]:
    course_name = f"Course of {teacher['subject']}"
    teacher_id = teacher["teacher_id"]
    max_students = 20
    cost = 300

    try:
        admin_dao.create_course(
            course_name=course_name,
            teacher_id=teacher_id,
            max_students=max_students,
            cost=cost
        )
        print(f"Course '{course_name}' successfully added to the database.")

    except Exception as e:
        print(f"Error creating course for teacher {teacher_id}: {e}")
"""
"""
admin_dao = AdminDAO()
query = "SELECT course_id, course_name FROM Courses LIMIT 20"
admin_dao.cursor.execute(query)
courses = admin_dao.cursor.fetchall()

classrooms = []
classroom_names = [f"{chr(65 + i // 5)}{i % 5 + 1}" for i in range(20)]

for i, course in enumerate(courses):
    classroom = {
        "classroom_name": classroom_names[i],
        "course_id": course["course_id"]
    }
    classrooms.append(classroom)

output_file = "classrooms.json"
with open(output_file, "w") as json_file:
    json.dump({"classrooms": classrooms}, json_file, indent=4)

print(f"Classroom data has been written to {output_file}")

admin_dao.close()
"""
"""
file_path = "classrooms.json"

try:
    with open(file_path, "r") as json_file:
        class_data = json.load(json_file)
except FileNotFoundError:
    print("The file 'classes.json' was not found.")
    exit()

class_dao = ClassDAO()
try:
    for class_entry in class_data["classrooms"]:
        course_id = class_entry["course_id"]
        classroom_name = class_entry["classroom_name"]
        class_dao.create_class(course_id, classroom_name)
finally:
    class_dao.close()
"""

"""
parent_dao = ParentDAO()
student_dao = StudentDAO()
course_dao = CourseDAO()

students = student_dao.get_all_students()
courses = course_dao.get_all_courses()

course_student_count = {course["course_id"]: 0 for course in courses}

max_students_per_course = 20

for student in students:
    student_id = student["student_id"]
    num_courses = random.randint(1, 5)
    available_courses = [course for course in courses if
                         course_student_count[course["course_id"]] < max_students_per_course]

    if not available_courses:
        print("No available courses with space left.")
        break

    selected_courses = random.sample(available_courses, min(num_courses, len(available_courses)))

    for course in selected_courses:
        course_id = course["course_id"]

        try:
            parent_dao.enroll_student_in_course(student_id=student_id, course_id=course_id)
            course_student_count[course_id] += 1
            print(f"Student {student_id} enrolled in course {course_id}.")
        except Exception as e:
            print(f"Error enrolling student {student_id} in course {course_id}: {e}")
"""
"""
file_path = "maintenance_tasks.json"
with open(file_path, "r") as json_file:
    tasks_data = json.load(json_file)

admin_dao = AdminDAO()

for task in tasks_data["maintenance_tasks"]:
    description = task["description"]
    status = task["status"]
    worker_id = task["maintenance_worker_id"]

    try:
        admin_dao.create_task(description=description, status=status, maintenance_worker_id=worker_id)
        print(f"Task '{description}' added successfully.")
    except Exception as e:
        print(f"Error adding task '{description}': {e}")
"""
"""
grades_data = {
    "grades": [
        {"student_id": "S0000001", "course_id": 61, "grade": 85.0},
        {"student_id": "S0000002", "course_id": 61, "grade": 90.0},
        {"student_id": "S0000003", "course_id": 62, "grade": 78.0},
        {"student_id": "S0000004", "course_id": 62, "grade": 88.0},
        {"student_id": "S0000005", "course_id": 63, "grade": 92.0},
        {"student_id": "S0000006", "course_id": 63, "grade": 95.0},
        {"student_id": "S0000007", "course_id": 71, "grade": 80.0},
        {"student_id": "S0000008", "course_id": 64, "grade": 85.0},
        {"student_id": "S0000009", "course_id": 65, "grade": 77.0},
        {"student_id": "S0000010", "course_id": 70, "grade": 89.0}
    ]
}

with open("grades.json", "w") as file:
    json.dump(grades_data, file, indent=4)

print("File 'grades.json' created successfully.")
"""
"""
file_path = "grades.json"
with open(file_path, "r") as json_file:
    grades_data = json.load(json_file)

teacher_dao = TeacherDAO()

for grade in grades_data["grades"]:
    student_id = grade["student_id"]
    course_id = grade["course_id"]
    grade_value = grade["grade"]

    try:
        teacher_dao.insert_student_grade(student_id=student_id, course_id=course_id, grade=grade_value)
        print(f"Grade {grade_value} for Student {student_id} in Course {course_id} added successfully.")
    except Exception as e:
        print(f"Error adding grade for Student {student_id} in Course {course_id}: {e}")
"""
"""
from decimal import Decimal
def convert_to_serializable(data):
    if isinstance(data, list):
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data

def export_courses_to_json(file_path):
    course_dao = CourseDAO()
    try:
        courses = course_dao.get_all_courses()
        if courses:
            courses_serializable = convert_to_serializable(courses)
            with open(file_path, 'w') as json_file:
                json.dump(courses_serializable, json_file, indent=4)
            print(f"Courses data exported successfully to {file_path}")
        else:
            print("No courses data found to export.")
    except Exception as e:
        print(f"Error exporting courses to JSON: {e}")
    finally:
        course_dao.close()

if __name__ == "__main__":
    file_path = "courses.json"
    export_courses_to_json(file_path)


def export_student_courses_to_json(file_path):
    student_courses_dao = StudentCoursesDAO()
    try:
        student_courses = student_courses_dao.get_all_student_courses()
        if student_courses:
            student_courses_serializable = convert_to_serializable(student_courses)
            with open(file_path, 'w') as json_file:
                json.dump(student_courses_serializable, json_file, indent=4)
            print(f"StudentCourses data exported successfully to {file_path}")
        else:
            print("No student courses data found to export.")
    except Exception as e:
        print(f"Error exporting student courses to JSON: {e}")
    finally:
        student_courses_dao.close()

if __name__ == "__main__":
    file_path = "student_courses.json"
    export_student_courses_to_json(file_path)
 """
"""
students_courses_file = "student_courses.json"
parents_file = "parents_and_students_meaningful.json"
courses_file = "courses.json"

with open(students_courses_file, "r") as sc_file:
    student_courses_data = json.load(sc_file)

with open(parents_file, "r") as parents_file:
    parents_data = json.load(parents_file)

with open(courses_file, "r") as courses_file:
    courses_data = json.load(courses_file)

parent_child_map = {
    child["id_number"]: parent["id_number"]
    for parent in parents_data["parents"]
    for child in parent["children"]
}

parent_dao = ParentDAO()

for student_course in student_courses_data:
    student_id = student_course["student_id"]
    course_id = student_course["course_id"]

    parent_id = parent_child_map.get(student_id)
    if not parent_id:
        print(f"Parent not found for student {student_id}. Skipping payment creation.")
        continue

    course = next((c for c in courses_data if c["course_id"] == course_id), None)
    if not course:
        print(f"Course {course_id} not found. Skipping payment creation for student {student_id}.")
        continue

    cost = course["cost"]
    try:
        parent_dao.pay_for_course(parent_id=parent_id, course_id=course_id, amount=cost)
        print(f"Payment for course {course_id} by parent {parent_id} created successfully.")
    except Exception as e:
        print(f"Error creating payment for parent {parent_id} and course {course_id}: {e}")

print("Payment data processing completed.")
"""

def load_schedules_to_database(file_path):

    try:
        with open(file_path, "r") as file:
            schedules_data = json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    for schedule in schedules_data:
        query = """
        INSERT INTO Schedules (course_id, class_id, course_name, student_id, day, hour)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            schedule["course_id"],
            schedule["class_id"],
            schedule["course_name"],
            schedule["student_id"],
            schedule["day"],
            schedule["hour"],
        )
        try:
            execute_query(query, params)
            print(f"Schedule added for student {schedule['student_id']} in course {schedule['course_id']}.")
        except Exception as e:
            print(f"Error adding schedule for student {schedule['student_id']}: {e}")

if __name__ == "__main__":
    file_path = "schedules.json"
    load_schedules_to_database(file_path)