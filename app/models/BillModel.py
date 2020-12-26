from app.database.connection import Database


class Bills(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS bills (
            id INT AUTO_INCREMENT,
            reservation_id INT,
            PRIMARY KEY(id),
            FOREIGN KEY (reservation_id) REFERENCES reservations(id),
        )"""
        self.execute(query)
        self.commit()

    def insert(
        self,
        customer_id,
        room_id,
        reservation_id,
        price,
    ):
        self.execute(
            "INSERT INTO bills (reservation_id) values (?,?,?,?)",
            (
                customer_id,
                room_id,
                reservation_id,
                price,
            ),
        )
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM bills")
        result = self.cursor.fetchall()

    def find(self, id):
        self.execute("SELECT * FROM bills WHERE id = ?", (id,))
        result = self.cursor.fetchone()

    def delete(self, id):
        self.execute("DELETE FROM bills WHERE id = ?", (id,))

    def drop(self):
        self.execute("DROP TABLE bills")
        self.commit()
