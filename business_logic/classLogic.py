from data_access.class_dao import ClassDAO

class ClassLogic:
    def __init__(self, course_id=None, classroom_name=None):
        self._course_id = course_id
        self._classroom_name = classroom_name
        self._class_dao = ClassDAO()

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Course ID must be a positive integer.")
        self._course_id = value

    @property
    def classroom_name(self):
        return self._classroom_name

    @classroom_name.setter
    def classroom_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Classroom name must be a non-empty string.")
        self._classroom_name = value

    def create_class(self):
        if not self._course_id or not self._classroom_name:
            print("Both course ID and classroom name are required to create a class.")
            return
        try:
            self._class_dao.create_class(self._course_id, self._classroom_name)
        except Exception as e:
            print(f"Error creating class: {e}")

    def update_class(self, class_id, new_course_id=None, new_classroom_name=None):
        if not isinstance(class_id, int) or class_id <= 0:
            raise ValueError("Class ID must be a positive integer.")
        try:
            self._class_dao.update_class(class_id, course_id=new_course_id, classroom_name=new_classroom_name)
        except Exception as e:
            print(f"Error updating class ID {class_id}: {e}")

    def delete_class(self, class_id):
        if not isinstance(class_id, int) or class_id <= 0:
            raise ValueError("Class ID must be a positive integer.")
        try:
            self._class_dao.delete_class(class_id)
        except Exception as e:
            print(f"Error deleting class ID {class_id}: {e}")

    def get_class_by_id(self, class_id):
        if not isinstance(class_id, int) or class_id <= 0:
            raise ValueError("Class ID must be a positive integer.")
        try:
            return self._class_dao.get_class_by_id(class_id)
        except Exception as e:
            print(f"Error fetching class ID {class_id}: {e}")
            return None

    def get_classes_by_course(self):
        if not self._course_id:
            print("Course ID is required to fetch classes by course.")
            return []
        try:
            return self._class_dao.get_classes_by_course(self._course_id)
        except Exception as e:
            print(f"Error fetching classes for course ID {self._course_id}: {e}")
            return []

    def get_all_classes(self):
        try:
            return self._class_dao.get_all_classes()
        except Exception as e:
            print(f"Error fetching all classes: {e}")
            return []

    def get_class_by_name(self):
        if not self._classroom_name:
            print("Classroom name is required to fetch class details.")
            return None
        try:
            return self._class_dao.get_class_by_name(self._classroom_name)
        except Exception as e:
            print(f"Error fetching class by name '{self._classroom_name}': {e}")
            return None

    def close(self):
        self._class_dao.close()
