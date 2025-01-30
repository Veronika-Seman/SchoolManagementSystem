# main.py
from business_logic.adminLogic import AdminLogic
from business_logic.parentLogic import ParentLogic
from business_logic.studentLogic import StudentLogic
from business_logic.teacherLogic import TeacherLogic
from business_logic.userLogic import UserLogic
from presentation.admin_menu import admin_menu
from presentation.parent_menu import parent_menu
from presentation.student_menu import student_menu
from presentation.teacher_menu import teacher_menu


def main():
    """
    School Management System - Main Entry Point

    This script serves as the main entry point for the School Management System.
    It handles user authentication, determines user roles, and directs users to
    their respective menus based on their role.

    ### Functionality:
    - Displays a welcome menu with login and exit options.
    - Authenticates users via email and password.
    - Retrieves the logged-in user's role and directs them to the appropriate menu.
    - Supports different user roles: Admin, Parent, Student, and Teacher.

    ### Modules Used:
    - `business_logic.*`: Handles business logic for different user types.
    - `presentation.*`: Provides user menu interactions.

    ### Roles and Their Menus:
    - **Student**: Accesses `student_menu()` using `StudentLogic`.
    - **Admin**: Accesses `admin_menu()` using `AdminLogic`.
    - **Parent**: Accesses `parent_menu()` using `ParentLogic`.
    - **Teacher**: Accesses `teacher_menu()` using `TeacherLogic`.

    ### Functions:
    - `main()`:
      - Displays the main menu.
      - Authenticates the user.
      - Retrieves user details and redirects to the correct menu.

    ### Execution:
    - If the script is run as the main module, it starts the `main()` function.

    This script serves as the core of the application, allowing different users
    to interact with the system based on their assigned roles.
    """

    user_logic = UserLogic(creator_role="Admin")

    while True:
        print("\n=== Welcome to the School Management System ===")
        print("1) Login")
        print("2) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if user_logic.login(email, password):

                current_user = user_logic.get_current_user()
                role = current_user["role"]

                if role == "Student":
                    studentLogic = StudentLogic(creator_role="Admin", student_id=current_user["id_number"], parent_id=current_user["id_number"])
                    student_menu(studentLogic)

                elif role == "Admin":
                    admin_logic = AdminLogic(creator_role="Admin", admin_id=current_user["id_number"], name="name", email=["email"], password="password", role="Admin", salary=0, budget=0)
                    admin_menu(admin_logic)

                elif role == "Parent":
                    parent_logic = ParentLogic(creator_role="Admin", parent_id=current_user["id_number"])
                    parent_menu(parent_logic)

                elif role == "Teacher":
                    print("\nAccessing Teacher Menu...")
                    teacher_logic = TeacherLogic(creator_role="Admin", teacher_id=current_user["id_number"])
                    teacher_menu(teacher_logic)


if __name__ == "__main__":
    main()
