def teacher_menu(teacher_logic):
    """
    Teacher Menu - School Management System

    This module provides the interface for teachers to manage course enrollments,
    grades, and class-related issues.

    ### Functionality:
    - Enroll students in courses.
    - Enter and update student grades.
    - Report classroom-related issues.
    - View a list of students enrolled in a specific course.
    - Logout from the system.
    """

    while True:
        print("\n=== Teacher Menu ===")
        print("1) Enroll student in a course")
        print("2) Enter student grades")
        print("3) Report a class issue")
        print("4) View students in a course")
        print("5) Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nEnroll Student in a Course")
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            try:
                result = teacher_logic.enroll_student_in_course(student_id, course_id)
                print(f"{result['message']}")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "2":
            print("\nEnter Student Grades")
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            grade = input("Enter grade: ")
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    teacher_logic.insert_student_grade(student_id, course_id, grade)
                else:
                    print("Invalid grade. Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "3":
            print("\nReport a Class Issue")
            class_id = input("Enter class ID: ")
            description = input("Describe the issue: ")
            teacher_logic.report_class_issue(class_id, description)
            print(f"Issue reported for class {class_id}.")

        elif choice == "4":
            print("\nView Students in a Course")
            course_id = input("Enter course ID: ")
            students = teacher_logic.get_students_in_course(course_id)
            if students and len(students) > 0:
                print("\nStudents in Course:")
                for student in students:
                    print(f"ID: {student['student_id']} | Name: {student['name']} | Email: {student['email']}")
            else:
                print(f"No students found for course {course_id}.")

        elif choice == "5":
            print("\n👋 Logging out...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
