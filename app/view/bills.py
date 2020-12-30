from app.models.BillModel import Bills
from app.functions import headline


class BillsView(Bills):
    def menu(self):
        headline("Pembayaran")
        text = ["1. Via Debit", "2. Cash", "0. Menu utama"]

        print("\n".join(text))
        choice = int(input("> "))
        if choice == 0:
            exit()
        elif choice == 1:
            pass
        elif choice == 2:
            pass
