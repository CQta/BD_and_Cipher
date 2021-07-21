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
    def Create(get_info, cur):
        cur.execute("INSERT INTO r(fname, lname, gender, plat) VALUES(?, ?, ?, ?)", get_info)


    def Del(cur):
            cur.execute("DELETE FROM r")

    def Del_by_id(cur, d, conn):
        cur.execute("DELETE FROM r WHERE id = ?", (d,))
        conn.commit()
    def Show(cur):
            cur.execute('SELECT * FROM r')
            rows = cur.fetchall()
            return rows