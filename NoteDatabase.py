import sqlite3
import datetime

class NoteDatabase:
    def __init__(self, name: str = "notes.db"):
        self.db = self.db = sqlite3.connect(name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.db.cursor()

    def createTable(self) -> None:
        """
        Creates the notes table if the database
        """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS NOTES(TIME TIMESTAMP PRIMARY KEY, USERID INT NOT NULL, ITEM TEXT NOT NULL)
        """)
        self.db.commit()

    def insertEntry(self, userid: int, item: str) -> None:
        """
        Inserts the Discord userid and entry into the database
        """
        now = datetime.datetime.now()
        try:
            self.cursor.execute("""INSERT INTO NOTES(TIME, USERID, ITEM)
            VALUES(?, ?, ?)""", (now, userid, item))
            self.db.commit()

        except sqlite3.IntegrityError:
            print("Invalid Entry!")

    def getEntries(self, userid: int) -> list:
        """
        Returns all the items with the given userid
        """
        self.cursor.execute("""SELECT * FROM NOTES WHERE USERID={}""".format(userid))
        return self.cursor.fetchall()

    def close(self) -> None:
        """
        Closes connection to the database
        """
        self.db.commit()
        self.db.close()
