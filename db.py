import sqlite3

class DB():
    def __init__(self):
        self.connection = sqlite3.connect('HomeControll.db')
        self.cursor = self.connection.cursor()
        self.InitializeTables()
    def GetCursor(self):
        return self.cursor
    def InitializeTables(self):
        sql = "CREATE TABLE IF NOT EXISTS thermometers (file_id VARCHAR(255) NOT NULL PRIMARY KEY, description VARCHAR(255))"
        self.cursor.execute(sql)