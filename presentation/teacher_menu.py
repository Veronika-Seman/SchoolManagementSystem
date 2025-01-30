def teacher_menu(teacher_logic):

    while True:
        print("\n=== Teacher Menu ===")
        print("1) Enroll student in a course") #עובד אבל לא מכניס לתור המתנה נותן שגיאה
        print("2) Enter student grades") #עובד
        print("3) Report a class issue") #עובד
        print("4) View students in a course") #לא עובד
        print("5) Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nEnroll Student in a Course")
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            result = teacher_logic.enroll_student_in_course(student_id, course_id)
            if result["status"] == "ENROLLED":
                print(f"Student {student_id} enrolled in course {course_id} successfully.")
            elif result["status"] == "WAITLIST":
                print(f"Course {course_id} is full. Student {student_id} added to waitlist at position {result['message']}.")

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
            if students:
                print(f"\nStudents in Course {course_id}:")
                for student in students:
                    print(f"{student['student_id']} - {student['name']}")
            else:
                print(f"No students found for course {course_id}.")

        elif choice == "5":
            print("\n👋 Logging out...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
