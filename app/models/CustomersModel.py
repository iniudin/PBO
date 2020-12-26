from app.database.connection import Database


class Customers(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            email VARCHAR(30) NOT NULL,
            phone VARCHAR(15) NOT NULL,
            address VARCHAR(50) NOT NULL,
            gender ENUM('L', 'P') NOT NULL,
            PRIMARY KEY(id)
        )
        """
        self.execute(query)
        self.commit()

    def insert(
        self,
        first_name,
        last_name,
        password,
        email,
        phone,
        address,
        gender,
    ):
        self.execute(
            "INSERT INTO customers (first_name, last_name, email, phone, address, gender) values (?,?,?,?,?,?,?,?)",
            (first_name, last_name, email, phone, address, gender),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM customers")
        result = self.cursor.fetchall()

    def find(self, id):
        self.execute("SELECT * FROM customers WHERE id = ?", (id,))
        result = self.cursor.fetchone()

    def delete(self, id):
        self.execute("DELETE FROM customers WHERE id = ?", (id))

    def drop(self):
        self.execute("DROP TABLE customers")
        self.commit()