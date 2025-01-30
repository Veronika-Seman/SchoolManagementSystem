def parent_menu(parentLogic):
    """
    Parent Menu - School Management System

    This module provides the interface for parents to manage their child's academic
    and financial activities within the school management system.

    ### Functionality:
    - View a child's grades and schedule.
    - Check the child's waitlist status for courses.
    - Make payments for courses and generate payment reports.
    - Enroll the child in a course.
    - Logout from the system.
    """

    while True:
        print("\n=== Parent Menu ===")
        print("1) View child's grades")
        print("2) View child's schedule")
        print("3) Check child's waitlist status")
        print("4) Pay for a course")
        print("5) Generate payment report")
        print("6) Enroll child in a course")
        print("7) Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nView Child's Grades")
            student_id = input("Enter your child's student ID: ")
            grades = parentLogic.get_child_grades(student_id)

            if grades:
                print("\nYour Child's Grades:")
                for grade in grades:
                    print(f"Course: {grade['course_name']} | Grade: {grade['grade']}")
            else:
                print("No grades found.")

        elif choice == "2":
            print("\nView Child's Schedule")
            student_id = input("Enter your child's student ID: ")
            schedule = parentLogic.get_child_schedule(student_id)

            if schedule:
                print("\nYour Child's Schedule:")
                for lesson in schedule:
                    print(
                        f"Day: {lesson['day']} | Hour: {lesson['hour']} | Course: {lesson['course_name']} | Classroom: {lesson['classroom_name']}")
            else:
                print("⚠ No schedule found.")

        elif choice == "3":
            print("\nCheck Child's Waitlist Status")
            student_id = input("Enter your child's student ID: ")
            course_id = input("Enter course ID: ")
            position = parentLogic.get_student_waitlist_position(student_id, course_id)

            if position is not None:
                print(f"Your child is in position {position} in the waitlist for course {course_id}.")
            else:
                print(f"Your child is not on the waitlist for course {course_id}.")

        elif choice == "4":
            print("\nPay for a Course")
            course_id = input("Enter course ID: ")
            amount = float(input("Enter amount to pay: "))

            try:
                parentLogic.pay_for_course(course_id, amount)
                print(f"Payment of {amount} for course {course_id} processed successfully.")
            except Exception as e:
                print(f"Payment failed: {e}")

        elif choice == "5":
            print("\nGenerate Payment Report")
            report = parentLogic.generate_payment_report(parentLogic.id_number)

            if report:
                print("\nPayment Report:")
                for payment in report:
                    print(f"Date: {payment['date']} | Course: {payment['course_name']} | Amount: {payment['amount']}")
            else:
                print("No payment data available.")

        elif choice == "6":
            print("\nEnroll Child in a Course")
            student_id = input("Enter your child's student ID: ")
            course_id = input("Enter course ID: ")

            try:
                result = parentLogic.enroll_student_in_course(student_id, course_id)
                if result["status"] == "ENROLLED":
                    print(f"{result['message']}")
                else:
                    print(f"{result['message']}")
            except Exception as e:
                print(f"Enrollment failed: {e}")

        elif choice == "7":
            print("👋 Logging out...")
            parentLogic.logout()
            break

        else:
            print("Invalid choice. Please try again.")