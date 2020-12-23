from app.Database.DBconnection import Database


class RoomModel(Database):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS rooms (
            room_id INTEGER PRIMARY KEY,
            type VARCHAR(10),
            details VARCHAR(250)
        )"""
        self.execute(query)
        self.commit()

    def insert(self, type, detail):
        self.execute("INSERT INTO rooms (type, details) values (?,?)", (type, detail))
        self.commit()

    def update(self, id, type=None, detail=None):
        if type:
            query = "UPDATE rooms SET type = ? WHERE room_id = ?"
            value = (type, id)
        elif detail:
            query = "UPDATE rooms SET detail = ? WHERE room_id = ?"
            value = (detail, id)
        else:
            query = "UPDATE rooms SET type = ?, detail = ? WHERE room_id = ?"
            value = (type, detail, id)
        self.execute(query, value)
        self.commit()

    def fetch_all(self):
        self.execute("SELECT * FROM rooms")
        result = self.cursor.fetchall()

    def delete(self, id):
        self.execute("DELETE FROM rooms WHERE room_id = ?", (id,))

    def drop(self):
        self.execute("DROP TABLE rooms")
        self.commit()