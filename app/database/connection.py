import mysql.connector


class Database:
    connection = None

    def __init__(self):
        try:
            if not self.connection:
                self.connection = mysql.connector.connect(
                    host="85.10.205.173",
                    user="userkeren",
                    password="userkeren12",
                    database="dbpbohotel",
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