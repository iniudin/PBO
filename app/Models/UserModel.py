from app.Database.DBconnection import Database


class Users(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            email VARCHAR(30) NOT NULL,
            phone VARCHAR(15) NOT NULL,
            address VARCHAR(50) NOT NULL,
            gender ENUM('M', 'F') NOT NULL,
            level ENUM('0', '1', '2') NOT NULL,
            PRIMARY KEY(id)
        )
        """
        self.execute(query)
        self.commit()

    def insert(
        self,
        first_name: str,
        last_name: str,
        password: str,
        email: str,
        phone: str,
        address: str,
        gender: str,
        level: str,
    ):
        self.execute(
            "INSERT INTO users (first_name, last_name, password, email, phone, address, gender, type) values (?,?,?,?,?,?,?,?)",
            (first_name, last_name, password, email, phone, address, gender, level),
        )
        self.commit()

    def change_password(self, id, password):
        self.execute(
            "UPDATE users SET password = ? WHERE id = ?",
            (password, id),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM users")
        result = self.cursor.fetchall()

    def find(self, id):
        self.execute("SELECT * FROM users WHERE room_id = ?", (id,))
        result = self.cursor.fetchone()

    def delete(self, id):
        self.execute("DELETE FROM users WHERE id = ?", (id))

    def drop(self):
        self.execute("DROP TABLE users")
        self.commit()