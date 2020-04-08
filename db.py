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


    # def insert(self, row, value):
    #     self.response_values[row] = value


    def insert_into_db(self):
        self.cursor.execute(
            f"INSERT INTO responses {tuple(self.response_values.keys())} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (list(self.response_values.values()))
        )
        self.conn.commit()
        self.close()


# # need this?
# class MessagesDB(Database):
#     def __init__(self):
#         self.cursor.execute(
#             f"""CREATE TABLE IF NOT EXISTS responses (
#             revivals INTEGER,
#             visits INTEGER,
#             special_services INTEGER,
#             sermons INTEGER,
#             personal_evangelism_meetings INTEGER,
#             lectures INTEGER,
#             worker_classes INTEGER,
#             counseling_hours INTEGER,
#             choir_meetings INTEGER,
#             msg_time DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')))"""
#         )



# if __name__ == '__main__':
#     db1 = ResponsesDB()
#     db1.insert('revivals', 1)
#     db1.insert('visits', 2)
#     db1.insert('special_services', 3)
#     db1.insert('sermons', 4)
#     db1.insert('personal_evangelism_meetings', 5)
#     db1.insert('lectures', 1)
#     db1.insert('worker_classes', 2)
#     db1.insert('counseling_hours', 3)
#     db1.insert('choir_meetings', 4)
#     db1.insert_into_db()
#     db1.close()
#
#     print(db1.response_values)