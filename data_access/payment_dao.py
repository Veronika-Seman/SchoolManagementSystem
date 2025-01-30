from data_access.data_operations import BaseDAO

class PaymentsDAO(BaseDAO):
    """
         PaymentsDAO class for managing operations related to payments in the system.
         Provides methods for fetching payments for a parent, calculating total payments,
         and deleting payments.
         Methods:
             get_payments_by_parent(parent_id):Retrieves all payments made by a parent, including course details.
             get_total_payments():Retrieves the total amount of all payments in the system.
             delete_payment(payment_id):Deletes a payment record by its ID.
             close():Closes the DAO connection and cleans up associated resources.
         """
    def __init__(self):
        super().__init__()

    def get_payments_by_parent(self, parent_id):
        query = """
        SELECT p.payment_id, p.course_id, c.course_name, p.amount, p.payment_date
        FROM Payments p
        JOIN Courses c ON p.course_id = c.course_id
        WHERE p.parent_id = %s
        """
        try:
            self.cursor.execute(query, (parent_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching payments for parent {parent_id}: {e}")
            return []

    def get_total_payments(self):
        query = """
        SELECT SUM(amount) AS total_payments
        FROM Payments
        """
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result['total_payments'] if result else 0
        except Exception as e:
            print(f"Error calculating total payments: {e}")
            return 0

    def delete_payment(self, payment_id):
        query = """
        DELETE FROM Payments
        WHERE payment_id = %s
        """
        try:
            self.cursor.execute(query, (payment_id,))
            self.connection.commit()
            print(f"Payment with ID {payment_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting payment {payment_id}: {e}")


    def close(self):
        super().close()
