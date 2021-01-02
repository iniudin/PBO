from app.database.connection import Database


class RoomModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS `rooms` (
            `id` INT AUTO_INCREMENT,
            `code` VARCHAR(5) UNIQUE NOT NULL,
            `type` VARCHAR(20) NOT NULL,
            `description` VARCHAR(250) NOT NULL,
            `status` TINYINT(1) NOT NULL,
            `price` INT NOT NULL,
            PRIMARY KEY(id)
        )"""
        self.execute(query)
        self.commit()

    def add(self, type, description, price):
        rooms = len(self.get_rooms())
        code = f"RO-{rooms}"
        self.execute(
            """
            INSERT INTO `rooms` (
                code,
                type,
                description,
                status,
                price
            )
            VALUES (%s,%s,%s,%s,%s)
            """,
            (code, type, description, 0, price),
        )
        self.commit()

    def get_rooms(self, empty=None):
        if empty:
            self.execute("SELECT * FROM rooms WHERE status = 0")
        else:
            self.execute("SELECT * FROM rooms")
        result = self.cursor.fetchall()
        return result

    def find(self, _id):
        self.execute("SELECT * FROM rooms WHERE id = %s", (_id))
        result = self.cursor.fetchone()
        return result

    def change_status(self, _id, status):
        query = "UPDATE rooms SET status = %s WHERE id = %s"
        self.execute(query, (status, _id))
        self.commit()

    def delete(self, _id):
        self.execute("DELETE FROM rooms WHERE id = %s", (_id,))
        self.commit()

    def drop(self):
        self.execute("DROP TABLE rooms")
        self.commit()
