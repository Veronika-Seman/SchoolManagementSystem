import mysql.connector

def delete_all_teachers():
    global cursor
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # עדכן לפי מסד הנתונים שלך
        password="Koki.2002",  # עדכן לפי מסד הנתונים שלך
        database="testdatabase"  # עדכן לפי מסד הנתונים שלך
    )
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Teachers;")
        connection.commit()
        cursor.execute("""
       # DELETE FROM Workers
        #WHERE worker_id IN (SELECT id_number FROM Users WHERE role = 'Teacher');
        """)
        connection.commit()
        cursor.execute("DELETE FROM Users WHERE role = 'Teacher';")
        connection.commit()
        print("All teachers have been deleted successfully.")
    except Exception as e:
        print(f"Error deleting teachers: {e}")
    finally:
        cursor.close()
        connection.close()

delete_all_teachers()

from data_access.data_operations import BaseDAO

class MaintenanceTaskDAO(BaseDAO):
    def delete_all_tasks(self):
        query = "DELETE FROM MaintenanceTasks"
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("All records from MaintenanceTasks table have been deleted successfully.")
        except Exception as e:
            print(f"Error deleting all records from MaintenanceTasks table: {e}")
if __name__ == "__main__":
    task_dao = MaintenanceTaskDAO()
    task_dao.delete_all_tasks()
    task_dao.close()  # זכרו לסגור את החיבור למסד הנתונים
