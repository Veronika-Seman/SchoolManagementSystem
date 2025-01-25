from data_access.data_operations import BaseDAO

class PaymentsDAO(BaseDAO):
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
