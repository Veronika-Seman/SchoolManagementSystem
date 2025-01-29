from data_access.payment_dao import PaymentsDAO


class PaymentsLogic:
    def __init__(self):
        self.payments_dao = PaymentsDAO()

    def get_payments_for_parent(self, parent_id):
        if not parent_id:
            raise ValueError("Parent ID cannot be empty.")
        try:
            payments = self.payments_dao.get_payments_by_parent(parent_id)
            if not payments:
                print(f"No payments found for parent ID {parent_id}.")
            return payments
        except Exception as e:
            print(f"Error fetching payments: {e}")
            return []

    def get_total_payments(self):
        try:
            total = self.payments_dao.get_total_payments()
            print(f"Total payments in the system: {total}")
            return total
        except Exception as e:
            print(f"Error fetching total payments: {e}")
            return 0

    def delete_payment(self, payment_id):
        if not payment_id:
            raise ValueError("Payment ID cannot be empty.")
        try:
            self.payments_dao.delete_payment(payment_id)
        except Exception as e:
            print(f"Error deleting payment: {e}")

    def close(self):
        self.payments_dao.close()
