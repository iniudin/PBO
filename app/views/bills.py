from app.models import BillModel


class BillsView(BillModel):
    def count_bill(self, user_id):
        pass

    def mybills(self, session):
        user_id = session["id"]
        print(self.get_bill_user(user_id))
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        return
