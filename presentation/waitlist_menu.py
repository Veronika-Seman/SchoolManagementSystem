from business_logic.waitlistLogic import WaitlistLogic
from business_logic.enrollmentLogic import EnrollmentLogic

def manage_waitlist(course_id, adminLogic, course_logic):
    """
    Waitlist Management - School Management System

    This module provides an interface for managing student waitlists for courses.
    It allows administrators or authorized users to assign students to classes,
    remove students from the waitlist, and view waitlist details.

    ### Functionality:
    - Retrieves and displays the waitlist for a given course.
    - Assigns students from the waitlist to an available course spot.
    - Removes students from the waitlist upon request.
    - Handles error scenarios such as invalid course IDs or empty waitlists.
    """

    try:
        waitlist_logic = WaitlistLogic()
        enrollment_logic = EnrollmentLogic()


        course_name = course_logic.get_course_name(course_id)
        if not course_name:
            print(f"Course {course_id} not found.")
            return

        waitlist_students = waitlist_logic.get_waitlist(course_id)

        if not waitlist_students:
            print(f"No students in the waitlist for {course_name} ({course_id}).")
            return

        print(f"\n--- Waitlist for Course: {course_name} ({course_id}) ---")
        for index, student in enumerate(waitlist_students, start=1):
            print(f"{index}. Student ID: {student['student_id']} | Position: {student['position']}")

        while True:
            print("\nOptions:")
            print("1) Assign student to class")
            print("2) Remove student from waitlist")
            print("3) Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                student_index = int(input("Enter student number to assign: ")) - 1
                if 0 <= student_index < len(waitlist_students):
                    student_id = waitlist_students[student_index]['student_id']

                    result = enrollment_logic.enroll_student_in_course(student_id, course_id)

                    if result["status"] == "ENROLLED":
                        waitlist_logic.remove_student_from_waitlist(student_id, course_id)
                        print(f"Student {student_id} has been assigned to the course successfully.")
                    else:
                        print(f"Unable to enroll student {student_id}: {result['message']}")
                else:
                    print("Invalid selection.")

            elif choice == "2":
                student_index = int(input("Enter student number to remove: ")) - 1
                if 0 <= student_index < len(waitlist_students):
                    student_id = waitlist_students[student_index]['student_id']
                    waitlist_logic.remove_student_from_waitlist(student_id, course_id)
                    print(f"Student {student_id} has been removed from the waitlist.")
                else:
                    print("Invalid selection.")

            elif choice == "3":
                print("Exiting waitlist management...")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    except Exception as e:
        print(f"Error managing waitlist for course {course_id}: {e}")
