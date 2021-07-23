import sqlite3
def chiper(a):
    if type(a) == str:
        chiper_a = ""
        for i in range(len(a)):
            asci = ord(a[i])
            asci = asci + 3
            chiper_a += chr(asci)
        return chiper_a
    else:
        return a

def decoder(a):
    if type(a) == str:
        decoder_a = ""
        for i in range(len(a)):
            asci = ord(a[i])
            asci = asci - 3
            decoder_a += chr(asci)
        return decoder_a
    else:
        return a

class OrderMapper:

    def __init__(self):
        self.conn = sqlite3.connect('orders.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""create table if not exists r(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        f_name text, l_name text,
        gender text, salary int)""")
        self.conn.commit()

    def create(self, get_info):
        self.cur.execute("INSERT INTO r(f_name, l_name, gender, salary) VALUES(?, ?, ?, ?)", get_info)
        self.conn.commit()

    def delete_all(self):
        self.cur.execute("DELETE FROM r")

    def delete_by_id(self, id):
        self.cur.execute("DELETE FROM r WHERE id = ?", (id,))
        self.conn.commit()

    def show(self):
        self.cur.execute('SELECT * FROM r')
        rows = self.cur.fetchall()
        return rows