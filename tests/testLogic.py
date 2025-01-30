from business_logic.adminLogic import AdminLogic
from business_logic.classLogic import ClassLogic
from business_logic.courseLogic import CourseLogic
from business_logic.maintenanceWorkerLogic import MaintenanceWorkerLogic
from business_logic.userLogic import UserLogic
from data_access.course_dao import CourseDAO
from data_access.teacher_dao import TeacherDAO

"""
def test_maintenance_worker_logic():
    try:
        # יצירת אובייקט עובד תחזוקה חדש באמצעות UserLogic
        user_logic = UserLogic(creator_role="Admin")
        user_logic.create_user_with_role(
            id_number="MW12345",
            name="John Doe",
            email="john.doe@example.com",
            password="securepass",
            role="MaintenanceWorker",
            salary=3000
        )
        print("Maintenance worker created successfully.")

        # יצירת אובייקט לוגיקה עבור עובד תחזוקה
        maintenance_logic = MaintenanceWorkerLogic(
            creator_role="Admin",
            maintenance_worker_id="MW12345",
            name="John Doe",
            email="john.doe@example.com",
            password="securepass",
            salary=3000
        )

        # דיווח על בעיית תחזוקה
        print("Reporting a maintenance issue...")
        maintenance_logic.report_maintenance_issue("Air conditioner not working in classroom B1")

        # הקצאת המשימה החדשה לעובד התחזוקה
        print("Assigning task to maintenance worker...")
        task_id = 1  # עדכון לפי מזהה המשימה שנוצרה
        maintenance_logic.update_task_status(task_id=task_id, status="Assigned")
        print(f"Task ID {task_id} assigned to maintenance worker MW12345.")

        # אחזור המשימות המוקצות לעובד התחזוקה
        print("Fetching assigned tasks...")
        tasks = maintenance_logic.get_assigned_tasks()
        if tasks:
            print("Assigned tasks:")
            for task in tasks:
                print(f"Task ID: {task['task_id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("No tasks assigned.")

        # עדכון סטטוס של משימה
        if tasks:
            task_id = tasks[0]['task_id']  # משתמשים ב-ID של המשימה הראשונה ברשימה
            print(f"Updating status for Task ID {task_id} to 'In Progress'...")
            maintenance_logic.update_task_status(task_id=task_id, status="In Progress")
            print(f"Task ID {task_id} status updated successfully.")

        print("Test completed successfully.")

    except Exception as e:
        print(f"Test failed: {e}")

# הרצת הבדיקה
test_maintenance_worker_logic()
"""
"""
def test_view_assigned_tasks():
    try:
        # יצירת אובייקט עובד תחזוקה
        maintenance_logic = MaintenanceWorkerLogic(
            creator_role="Admin",
            maintenance_worker_id="MW12345",
            name="John Doe",
            email="john.doe@example.com",
            password="securepass",
            salary=3000
        )

        # הצגת המשימות
        print("Viewing assigned tasks...")
        tasks = maintenance_logic.get_assigned_tasks()
        if tasks:
            print("Tasks fetched successfully.")
        else:
            print("No tasks found.")

    except Exception as e:
        print(f"Test failed: {e}")

# הרצת הבדיקה
test_view_assigned_tasks()
"""
"""
from business_logic.teacherLogic import TeacherLogic

try:
    teacher_logic = TeacherLogic(
        creator_role="Admin",
        teacher_id="T345"
    )

    student_id = "156566589"
    course_id = 75
    teacher_logic.enroll_student_in_course(student_id, course_id)
    print(f"Student {student_id} enrolled in course {course_id} successfully.")
except Exception as e:
    print(f"Error during test execution: {e}")
"""
"""
from business_logic.adminLogic import AdminLogic
from data_access.teacher_dao import TeacherDAO

# יצירת אובייקט AdminLogic
admin_logic = AdminLogic(
    creator_role="Admin",
    admin_id="A00001",  # תעודת הזהות של המנהל
    name="Admin User",
    email="admin@example.com",
    password="adminpass",
    role="Admin",
    salary=10000,
    budget=50000
)

# בדיקה אם מורה קיים במערכת
teacher_dao = TeacherDAO()
teacher_id = "T12345"
if not teacher_dao.teacher_exists(teacher_id):
    print(f"Teacher with ID {teacher_id} does not exist. Please add the teacher before creating a course.")
else:
    # פרטי הקורס ליצירה
    course_name = "Advanced Mathematics"
    max_students = 3
    cost = 500

    # ניסיון ליצור קורס
    try:
        admin_logic.create_course(
            course_name=course_name,
            teacher_id=teacher_id,
            max_students=max_students,
            cost=cost
        )
        print(f"Test Passed: Course '{course_name}' created successfully.")
    except Exception as e:
        print(f"Test Failed: Error during course creation: {e}")
"""
"""
course_logic = CourseLogic()

# בדיקה אם הקורס קיים לפני המחיקה
course_id_to_delete = 81  # מזהה הקורס שאנחנו רוצים למחוק
course_dao = CourseDAO()

# בדיקה אם הקורס קיים
course = course_dao.get_course_by_id(course_id_to_delete)

if course:
    print(f"Course found: {course}. Proceeding to delete.")

    # קביעת course_id באובייקט course_logic
    course_logic.course_id = course_id_to_delete

    # ניסיון למחוק את הקורס
    try:
        course_logic.delete_course()
        print(f"Test Passed: Course with ID {course_id_to_delete} deleted successfully.")
    except Exception as e:
        print(f"Test Failed: Error during course deletion: {e}")

    # בדיקה אם הקורס נמחק בהצלחה
    course_after_deletion = course_dao.get_course_by_id(course_id_to_delete)
    if not course_after_deletion:
        print(f"Verification Passed: Course with ID {course_id_to_delete} no longer exists.")
    else:
        print(f"Verification Failed: Course with ID {course_id_to_delete} still exists.")
else:
    print(f"Test Skipped: Course with ID {course_id_to_delete} does not exist in the system.")
"""
"""
from business_logic.parentLogic import ParentLogic

# יצירת אובייקט ParentLogic
try:
    parent_logic = ParentLogic(
        parent_id="P000001",  # תעודת זהות של ההורה
        name="John Doe",
        email="john.doe@example.com",
        password="securepass"
    )

    # פרטי התשלום
    course_id = 65  # מזהה הקורס
    amount = 300  # סכום התשלום

    # ניסיון לבצע תשלום
    try:
        parent_logic.pay_for_course(course_id=course_id, amount=amount)
        print(f"Test Passed: Payment of {amount} for course {course_id} processed successfully.")
    except Exception as e:
        print(f"Test Failed: {e}")

except Exception as e:
    print(f"Error during ParentLogic object creation: {e}")
"""
from business_logic.waitlistLogic import WaitlistLogic

try:
    waitlist_logic = WaitlistLogic()

    course_id = 101

    max_students = 3

    total_students = 10

    print("\n📌 התחלת בדיקה: הוספת סטודנטים לקורס ובדיקת רשימת ההמתנה.\n")

    # הוספת סטודנטים עד המקסימום
    for student_id in range(1, max_students + 1):
        position = waitlist_logic.add_student_to_waitlist(student_id, course_id)
        print(f"✅ סטודנט {student_id} נוסף לקורס (מיקום: {position})")

    print("\n📌 הוספת סטודנטים נוספים מעבר למקסימום והכנסתם לרשימת המתנה.\n")

    # הוספת סטודנטים לרשימת המתנה
    for student_id in range(max_students + 1, total_students + 1):
        position = waitlist_logic.add_student_to_waitlist(student_id, course_id)
        print(f"⚠ סטודנט {student_id} נכנס לרשימת ההמתנה (מיקום: {position})")

    print("\n📌 בדיקת שליחת הודעה למנהל אם התור עולה על 5 סטודנטים.\n")

    # בדיקת שליחת הודעה למנהל
    waitlist_logic.check_waitlist_threshold(course_id, threshold=5)

    print("\n✅ כל הבדיקות הושלמו בהצלחה!")

except Exception as e:
    print(f"\n❌ שגיאה במהלך הבדיקה: {e}")

