import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def set_users(self, user_id, name, age, height, weight, date):
        ins = 'INSERT INTO reg (user_id, name, age, height, weight, date) VALUES(?, ?, ?, ?, ?, ?)'
        with self.connection:
            return self.cursor.execute(ins, (user_id, name, age, height, weight, date))

    def update_weight(self, user_id, weight, date):
        with self.connection:
            ins = "UPDATE reg SET weight = ?, date = ? WHERE (user_id = ?)"
            result = self.cursor.execute(ins, (weight, date, user_id))
            return result

    def exists(self):
        with self.connection:
            ins = "SELECT*FROM reg"
            result = self.cursor.execute(ins).fetchall()
            return result

   