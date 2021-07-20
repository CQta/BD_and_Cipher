import sqlite3

import numpy as np
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
def Create(n):
    cur.execute("SELECT COUNT(*) from r")
    rows = cur.fetchall()
    for row in rows:
        N = row[0]
    while n != 0:
        print('Введите имя')
        name = input()
        name = Chiper(name)
        print('Введите фамилию')
        s_name = input()
        s_name = Chiper(s_name)
        print('Введите пол')
        gen = input()
        gen = Chiper(gen)
        print('Введите зарплату')
        zar = int(input())
        N = N + 1
        get_info = (N, name, s_name, gen, zar)
        cur.execute("INSERT INTO r(id, fname, lname, gender, plat) VALUES(?, ?, ?, ?, ?)", get_info)
        conn.commit()
        n = n - 1

def Del(d):
    if d == "all":
        cur.execute("DELETE FROM r")
    else:
        cur.execute("DELETE FROM r WHERE lname = ?", (d,))

def Show(v1):
    j = 0
    Display_info = []
    if v1 == "all":
        cur.execute('SELECT * FROM r')
        rows = cur.fetchall()
        for row in rows:
            for j in range(5):
                d_name = Decoder(row[j])
                Display_info.append(d_name)
            print(Display_info)
            Display_info.clear()

    else:
        cur.execute('SELECT * FROM r WHERE lname = ?', (v1,))
        row = cur.fetchall()
        row = Decoder(row)
        print(row)


choice = 1
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""create table if not exists r(id int primary key, fname text, lname text, gender text, plat int)""")
conn.commit()

while choice != 0:
    print('Ввести данные-1, Удалить данные-2, Просмотр данных-3, Выход-0')
    choice = int(input())

    if choice == 0:
        break

    if choice == 3:
        print('Введите фамилию или если хотите вывести все данные наберите all')
        v1 = input()
        Show(v1)

    if choice == 1:
        print('Введите кол-во людей')
        n = int(input())
        Create(n)

    if choice == 2:
        print('Введите id для удаления, для удаления всех данных введите all ')
        d = input()
        Del(d)








