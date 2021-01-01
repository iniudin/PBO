from app.models.bills import BillsModel
from app.functions import headline, print_table 


class BillsView(BillsModel):
    def main_menu(self):
        text_menu = (
            ["1", "Daftar pembayaran"],
            ["2", "Cash"],
            ["3", "Debbit card"]
        )
        print_table("Menu pembayaran", ["No", "Deskripsi"], text_menu)
        choice = int(input("> "))
        if choice == 0:
            return 
        elif choice == 1:
            Cash()
        elif choice == 3:
            DebbitCard()
        else:
            print("Perintah tidak ditemukan")

    def Cash(self):
        print("Jika Anda memilih pembayaran secara langsung")
        print("Silahkan menuju ke tempat kasir untuk melakukan pembayaran")
        print("Terima Kasih")
        Riwayat()

    def DebbitCard(self):
        print("Jika Anda memilih pembayaran secara Debbit card")
        print("Anda harus memasukkan PIN Anda")
        print("Jika sudah selesai maka akan ada kalimat: ")
        print("Transaksi Anda sukses")
        Riwayat()

    def Riwayat(self):
        #Intinya disinituh aku pengen kalau milih pembyaran cash akan ada fungsi riwayat yang menuju ke pembyaran cash
        #Sedangkan kalau lewat debbit card maka juga akan menuju ke riwayat debbit card 
        if Cash():
            print("Riwayat Pembayaran")
        else:
            print("Riwayat Pembayaran")
        self.BackToMenu()

    @property
    def BackToMenu(self):
        input("Tekan Enter untuk kembali ke Menu")
        self.main_menu
