import sqlite3
def chiper(a):
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

def decoder(a):
    if type(a) == str:
        a1 = ""
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
        self.cur.execute("""create table if not exists r(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        f_name text, l_name text,
        gender text, plat int)""")
        self.conn.commit()

    def create(self, get_info):
        self.cur.execute("INSERT INTO r(f_name, l_name, gender, plat) VALUES(?, ?, ?, ?)", get_info)
        self.conn.commit()

    def delete(self):
            self.cur.execute("DELETE FROM r")

    def del_by_id(self, d):
        self.cur.execute("DELETE FROM r WHERE id = ?", (d,))
        self.conn.commit()

    def show(self):
            self.cur.execute('SELECT * FROM r')
            rows = self.cur.fetchall()
            return rows