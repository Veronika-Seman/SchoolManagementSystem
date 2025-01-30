
def admin_menu(adminLogic):

    while True:
        print("\n=== Admin Menu ===")
        print("1) Create User")
        print("2) Create new course")
        print("3) Assign teacher to course")
        print("4) Manage financial reports")
        print("5) Manage waitlists")
        print("6) Manage employee tasks")
        print("7) Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCreate New User")
            id_number = input("Enter user ID: ")
            name = input("Enter user name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            role = input("Enter role (Admin, Teacher, Student, Parent, MaintenanceWorker): ")

            adminLogic.create_user_with_role(id_number, name, email, password, role)
            #עבד אבל אי אפשר ליצור את היוזר כי חייב תז הורה

        elif choice == "2":
            print("\nCreate New Course")
            course_name = input("Enter course name: ")
            teacher_id = input("Enter teacher ID: ")
            max_students = int(input("Enter max students allowed: "))
            cost = float(input("Enter course cost: "))

            adminLogic.create_course(course_name, teacher_id, max_students, cost)


        elif choice == "3":
            print("\nAssign Teacher to Course")
            teacher_id = input("Enter teacher ID: ")
            course_id = input("Enter course ID: ")
            adminLogic.assign_teacher_to_course(teacher_id, course_id)
            break

        elif choice == "4":
            print("\nManage Financial Reports")
            report = adminLogic.generate_financial_report()
            if report:
                print("\nFinancial Report:")
                for entry in report:
                    print(f"Category: {entry['category']} | Total: {entry['total']}")
            else:
                print("No financial data available.")

        elif choice == "5":
            print("\nManage Waitlists")
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            action = input("Enter action (Add/Remove): ")
            adminLogic.manage_waitlist(student_id, course_id, action)

        elif choice == "6":
            print("\nManage Employee Tasks")
            description = input("Enter task description: ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            worker_id = input("Enter maintenance worker ID (optional): ")
            adminLogic.create_task(description, status, worker_id if worker_id else None)

        elif choice == "7":
            print("👋 Logging out...")
            adminLogic.logout()
            break

        else:
            print("Invalid choice. Please try again.")
