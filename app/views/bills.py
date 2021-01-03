from app.models import BillModel
from app.functions import print_table


class BillsView(BillModel):
    def mybills(self, session):
        user_id = session["id"]
        bills = self.get_bill_user(user_id)
        column = [i.title() for i in bills[0].keys()]
        rows = [list(i.values()) for i in bills]
        print_table("Daftar Tagihan", column, rows)
        print("Catatan:\nSilahkan menghubungi admin untuk mengkonfirmasi pembayaran.")
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        return
