import sqlite3


class Database:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    def __init__(self, query, value):
        self.query = query
        self.value = value

    def create_table(self):
        self.cursor.execute(self.query)
        self.connection.commit()

    def insert(self):
        self.cursor.executemany(self.query, self.value)
        self.connection.commit()

    def fetch_all(self) -> list:
        result = self.cursor.execute(self.query)
        return [i for i in result.fetchall()]

    def fetch(self):
        result = self.cursor.execute(self.query)
        return result.fetchone()

    def update(self):
        self.cursor.execute(self.query, self.value)
        self.connection.commit()

    def delete(self):
        self.cursor.execute(self.query, self.value)
        self.connection.commit()