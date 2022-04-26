import sqlite3
import datetime

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'reg' ('user_id') VALUES (?)", ([user_id]))
    def exists(self):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM reg").fetchone()
            return result[0]

    def update_weight(self, user_id, weight, date):
        with self.connection:
            ins = "UPDATE reg SET weight = ?, date = ? WHERE (user_id = ?)"
            result = self.cursor.execute(ins, (weight, date, user_id))
            


db = Database('dietbase.db')
a = db.update_weight(***************, 82.0, datetime.date.today())


