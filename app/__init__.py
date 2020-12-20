from app.functions import headline


class App:

    __session: str = None

    def login(self):
        headline("Login")
        username = input("Username: ")
        password = input("Password: ")
        if username == "user" and password == "pass":
            self.__session = "loggedin"
            return self.main_menu()
        else:
            print("Kombinasi user dan password salah")

    def register(self):
        pass

    def main_menu(self):
        headline("Main Menu")
        exit()

    def command(cmd):
        pass

    def run(self):
        while True:
            if not self.__session:
                self.login()
            else:
                pass
