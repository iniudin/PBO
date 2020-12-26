from app.models.EmployeesModel import Employees
from app.functions import headline

class EmployeesView(Employees):
    def menu(self):
        headline("Main Menu")
        text = ["1. Biodata", "2.Jadwal Kerja", "3. Info Gaji", "0. Menu utama"]

        print("\n".join(text))
        choice = int(input("> "))
        if choice == 0:
            exit()
        elif choice == 1:
            self.execute("SELECT * FROM employees WHERE id = ?", (id,))
            result = self.cursor.fetchone()
        elif choice == 2:
            #belom tau
            pass
        elif choice == 3:
            #belom tau 
            pass

    def Registrasi(self):
        headline("Registrasi")
        first_name=input("First Name : ")
        last_name=input("Last Name : ")
        password=input("Password : ")
        email=input("Email : ")
        phone=input("Phone: ")
        address=input("Address: ")
        gender=input("Gender : ")
