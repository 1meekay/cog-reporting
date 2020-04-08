import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('cogdb.db')
        self.cursor = self.conn.cursor()


    def close(self):
        self.conn.close()


class ResponsesDB(Database):
    def __init__(self):
        super().__init__()
        self.response_values = {}
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS responses (
            revivals INTEGER,
            visits INTEGER,
            special_services INTEGER,
            sermons INTEGER,
            personal_evangelism_meetings INTEGER,
            lectures INTEGER,
            worker_classes INTEGER,
            counseling_hours INTEGER,
            choir_meetings INTEGER,
            msg_time DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')))"""
        )


    def insert_into_db(self):
        self.cursor.execute(
            f"INSERT INTO responses {tuple(self.response_values.keys())} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (list(self.response_values.values()))
        )
        self.conn.commit()
        self.close()