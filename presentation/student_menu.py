
def student_menu(studentLogic):


    while True:
        print("\n=== Student Menu ===")
        print("1) View My Grades")
        print("2) View My Schedule")
        print("3) Check waitlist status")
        print("4) Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            grades = studentLogic.get_grades()
            if grades:
                print("\nYour Grades:")
                for grade in grades:
                    print(f"Course: {grade['course_name']} | Grade: {grade['grade']}")
            else:
                print("No grades found.")
        elif choice == "2":
            schedule = studentLogic.get_schedule()
            if schedule:
                print("\nYour Schedule:")
                for lesson in schedule:
                    print(f"Day: {lesson['day']} | Hour: {lesson['hour']} | Course: {lesson['course_name']} | Classroom: {lesson['classroom_name']}")
            else:
                print("No schedule found.")
        elif choice == "3":
            course_id = input("Enter Course ID to check waitlist status: ")
            position = studentLogic.get_student_waitlist_position(course_id)
            if position is not None:
                print(f"You are in position {position} in the waitlist for course {course_id}.")
            else:
                print(f"You are not on the waitlist for course {course_id}.")

        elif choice == "4":
            print("👋 Logging out...")
            studentLogic.logout()
        break


