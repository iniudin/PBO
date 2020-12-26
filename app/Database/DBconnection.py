import mysql.connector


class Database:
    connection = None

    def __init__(self):
        try:
            if not self.connection:
                self.connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pbomyhotel",
                )
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(error)

    def __del__(self):
        self.connection.close()

    def execute(self, query, value=None):
        if value:
            self.cursor.execute(query, value)
        else:
            self.cursor.execute(query)

    def execute_many(self, query, values=None):
        if values:
            self.cursor.executemany(query, values)
        else:
            self.cursor.executemany(query)

    def commit(self):
        self.connection.commit()