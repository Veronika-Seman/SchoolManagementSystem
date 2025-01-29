from data_access.admin_dao import AdminDAO
from data_access.maintenanceWorker_dao import MaintenanceWorkerDAO
from data_access.parent_dao import ParentDAO
from data_access.sqlConnect import get_connection
from data_access.student_dao import StudentDAO
from data_access.teacher_dao import TeacherDAO
from data_access.user_dao import UserDAO
from business_logic.userLogic import UserLogic


def main():
    connection = get_connection()
    if connection is None:
        print("Unable to connect to the database. Exiting program.")
        return

    user_dao = UserDAO()
    user_logic = UserLogic(user_dao)

    while True:
        print("\n--- Welcome to Learning Center System ---")
        print("1. Login")
        print("2. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\n🔐 Login Process")

            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if user_logic.login(email, password):
                current_user = user_logic.get_current_user()
                print(
                    f"\n✅ Login successful! Welcome, {current_user['email']} (Role: {current_user['role'].capitalize()}).\n")
                break
            else:
                print("❌ Invalid credentials. Please try again.\n")

        elif choice == "2":
            print("👋 Exiting system... Goodbye!")
            return
        else:
            print("⚠ Invalid choice. Please enter 1 or 2.")

    role = current_user["role"]

    dao = None
    if role == "Admin":
        dao = AdminDAO()
    elif role == "MaintenanceWorker":
        dao = MaintenanceWorkerDAO()
    elif role == "Student":
        dao = StudentDAO()
    elif role == "Parent":
        dao = ParentDAO()
    elif role == "Teacher":
        dao = TeacherDAO()
    else:
        print("❌ Unrecognized role! Exiting system...")
        return

    user_logic.logout()
    print("👋 Logged out successfully. See you next time!")


if __name__ == "__main__":
    main()
