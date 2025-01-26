from data.load_data import data
from data_access.user_dao import UserDAO
from data_access.student_dao import StudentDAO

user_dao = UserDAO()
student_dao = StudentDAO()

for parent in data["parents"]:
    # הוספת הורה למערכת
    user_dao.create_user(
        id_number=parent["id_number"],
        name=parent["name"],
        email=parent["email"],
        password=parent["password"],
        role="Parent"
    )

    # הוספת תלמידים הקשורים להורה
    for child in parent["children"]:
        student_dao.create_student(
            student_id=child["id_number"],
            name=child["name"],
            email=child["email"],
            password=child["password"],
            parent_id=parent["id_number"]
        )
