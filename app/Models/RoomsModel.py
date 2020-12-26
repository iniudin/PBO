from app.Database.DBconnection import Database


class Rooms(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS rooms (
            id INT AUTO_INCREMENT,
            code VARCHAR(10) NOT NULL UNIQUE,
            type VARCHAR(20) NOT NULL,
            description VARCHAR(250) NOT NULL,
            price INT NOT NULL,
            PRIMARY KEY(id)
        )"""
        self.execute(query)
        self.commit()

    def insert(self, code, type, description, price):
        self.execute(
            "INSERT INTO rooms (code, type, description, price) values (?,?,?,?)",
            (code, type, description, price),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM rooms")
        result = self.cursor.fetchall()

    def find(self, id):
        self.execute("SELECT * FROM rooms WHERE id = ?", (id,))
        result = self.cursor.fetchone()

    def delete(self, id):
        self.execute("DELETE FROM rooms WHERE id = ?", (id,))

    def drop(self):
        self.execute("DROP TABLE rooms")
        self.commit()