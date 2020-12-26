from app.Database.DBconnection import Database


class RoomModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS rooms (
            id INT AUTO_INCREMENT,
            type VARCHAR(20),
            description VARCHAR(250),
            price INT,
            PRIMARY KEY(id)
        )"""
        self.execute(query)
        self.commit()

    def insert(self, type: str, description: str, price: int):
        self.execute(
            "INSERT INTO rooms (type, description, price) values (?,?,?)",
            (type, description, price),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM rooms")
        result = self.cursor.fetchall()

    def find(self, id):
        self.execute("SELECT * FROM rooms WHERE room_id = ?", (id,))
        result = self.cursor.fetchone()

    def delete(self, id):
        self.execute("DELETE FROM rooms WHERE room_id = ?", (id,))

    def drop(self):
        self.execute("DROP TABLE rooms")
        self.commit()