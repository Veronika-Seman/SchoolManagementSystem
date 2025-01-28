
from business_logic.maintenanceWorkerLogic import MaintenanceWorkerLogic
from business_logic.userLogic import UserLogic
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
from business_logic.teacherLogic import TeacherLogic
from business_logic.userLogic import UserLogic

try:

    user_logic = UserLogic(creator_role="Admin")
    user_logic.create_user_with_role(
        id_number="T12345",
        name="John Smith",
        email="john16.smith@example.com",
        password="securepass123",
        role="Teacher",
        salary=5000,
        subject="Mathematics"
    )
    print("Teacher created successfully.")

    teacher = TeacherLogic.get_teacher()
    if teacher:
        print(f"Fetched teacher: {teacher}")

    print("Updating teacher details...")
    TeacherLogic.update_teacher(
        name="John Smith Updated",
        email="john.smith.updated@example.com",
        password="newsecurepass",
        salary=5500,
        subject="Physics"
    )
    print("Teacher updated successfully.")

    # בדיקה: הוספת ציון לתלמיד
    print("Inserting student grade...")
    TeacherLogic.insert_student_grade(
        student_id="S1001",
        course_id=1,
        grade=95
    )
    print("Grade inserted successfully.")

    # בדיקה: אחזור תלמידים בקורס
    print("Fetching students in course...")
    students = TeacherLogic.get_students_in_course(
        teacher_id="T12345",
        course_id=1
    )
    if students:
        print(f"Students in course: {students}")

    # בדיקה: דיווח על בעיה בכיתה
    print("Reporting class issue...")
    TeacherLogic.report_class_issue(
        class_id=1,
        description="Projector not working"
    )
    print("Class issue reported successfully.")

    print("All tests completed successfully.")

except Exception as e:
    print(f"Error during test execution: {e}")


