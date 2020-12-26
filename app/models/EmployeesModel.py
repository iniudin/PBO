from app.database.connection import Database


class Employees(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            email VARCHAR(30) UNIQUE NOT NULL,
            username VARCHAR(20) UNIQUE NOT NULL,
            password VARCHAR(20) NOT NULL,
            phone VARCHAR(15) NOT NULL,
            address VARCHAR(50) NOT NULL,
            gender ENUM('L', 'P') NOT NULL,
            is_admin TINYINT(1) NOT NULL,
            register_date DATETIME DEFAULT CURRENT_TIMESTAMP,,
            PRIMARY KEY(id)
        )
        """
        self.execute(query)
        self.commit()

    def insert(
        self,
        first_name,
        last_name,
        username,
        password,
        email,
        phone,
        address,
        gender,
        is_admin,
    ):
        timeNow = pendulum.now("Europe/London")
        self.execute(
            "INSERT INTO employees (first_name, last_name, username, password, email, phone, address, gender, is_admin) values (?,?,?,?,?,?,?,?,?)",
            (
                first_name,
                last_name,
                username,
                password,
                email,
                phone,
                address,
                gender,
                is_admin,
            ),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM employees")
        result = self.cursor.fetchall()

    def find(self, id):
        self.execute("SELECT * FROM employees WHERE room_id = ?", (id,))
        result = self.cursor.fetchone()

    def delete(self, id):
        self.execute("DELETE FROM employees WHERE id = ?", (id))

    def drop(self):
        self.execute("DROP TABLE employees")
        self.commit()