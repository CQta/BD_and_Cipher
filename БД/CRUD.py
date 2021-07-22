import sqlite3
def Chiper(a):
    if type(a) == str:
        a1 = ""
        i = 0
        for i in range(len(a)):
            asci = ord(a[i])
            asci = asci + 3
            a1 += chr(asci)
        return a1
    else:
        return a
def Decoder(a):
    if type(a) == str:
        a1 = ""
        i = 0
        for i in range(len(a)):
            asci = ord(a[i])
            asci = asci - 3
            a1 += chr(asci)
        return a1
    else:
        return a
class OrderMapper:
    def __init__(self):
        self.conn = sqlite3.connect('orders.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""create table if not exists r(id  INTEGER PRIMARY KEY AUTOINCREMENT, fname text, lname text, gender text, plat int)""")
        self.conn.commit()

    def Create(self, get_info):
        self.cur.execute("INSERT INTO r(fname, lname, gender, plat) VALUES(?, ?, ?, ?)", get_info)
        self.conn.commit()

    def Del(self):
            self.cur.execute("DELETE FROM r")

    def Del_by_id(self, cur, d, conn):
        self.cur.execute("DELETE FROM r WHERE id = ?", (d,))
        self.conn.commit()
    def Show(self):
            self.cur.execute('SELECT * FROM r')
            rows = self.cur.fetchall()
            return rows