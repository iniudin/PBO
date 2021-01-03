from app.models import BillModel
from app.functions import print_table, headline


class BillsView(BillModel):
    def mybills(self, session):
        user_id = session["id"]
        bills = self.get_bill_user(user_id)
        column = [i.title() for i in bills[0].keys()]
        rows = [list(i.values()) for i in bills]
        print_table("Daftar Tagihan", column, rows)
        print("Catatan:\nSilahkan menghubungi admin untuk mengkonfirmasi pembayaran.")
        self.back_to_menu

    def admin_view(self):
        try:
            bills = self.get_bills(approved=0)
            column = [i.title() for i in bills[0].keys()]
            rows = [list(i.values()) for i in bills]
            print_table("Catatan Transaksi", column, rows)
            headline("Konfirmasi pembayaran")
            resi_id = input("Masukkan Id Resi: ")
            agree = input(
                "Apakah anda yakin untuk mengkonfirmasi pembayaran tersebut? (Y/N)"
            )
            if agree.lower() == "y":
                self.change_status(resi_id)
                print("Pembayaran telah dikonfirmasi, terimakasih!")
            else:
                print("Konfirmasi pembayaran dibatalkan!")
        except Exception:
            print("Transaksi kosong")
        self.back_to_menu

    def owner_view(self):
        try:
            bills = self.get_bills(approved=2)
            column = [i.title() for i in bills[0].keys()]
            rows = [list(i.values()) for i in bills]
            print_table("Catatan Transaksi", column, rows)
        except Exception:
            print("Transaksi kosong")
        self.back_to_menu

    @property
    def back_to_menu(self):
        input("Tekan Enter untuk kembali ke Menu")
        return
