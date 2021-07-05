import sqlite3
import numpy as np
v = 1
N = 1
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""create table if not exists r(id int primary key, fname text, lname text, gender text, plat int)""")
conn.commit()

while v != 0:
    print('Ввести данные-1, Удалить данные-2, Просмотр данных-3, Выход-0')
    v = int(input())
    if v == 0:
        break
    if v == 3:
        print('Введите фамилию или если хотите вывести все данные наберите all')
        v1 = input()
        if v1 == "all":
            cur.execute('SELECT * FROM r')
            for row in cur:
                print(row)
        else:
            cur.execute('SELECT * FROM r WHERE lname = ?', (v1,))
            row = cur.fetchall()
            print(row)
    if v == 1:
        print('Введите кол-во людей')
        n = int(input())
        while n != 0:
            print('Введите имя')
            name = input()
            print('Введите фамилию')
            s_name = input()
            print('Введите пол')
            gen = input()
            print('Введите зарплату')
            zar = int(input())
            get_info = (N, name, s_name, gen, zar)
            cur.execute("INSERT INTO r(id, fname, lname, gender, plat) VALUES(?, ?, ?, ?, ?)", get_info)
            conn.commit()
            N = N+1
            n = n-1
    if v == 2:
        print('Введите id для удаления, для удаления всех данных введите all ')
        i = input()
        if i == "all":
            cur.execute("DELETE FROM r")
        else:
            cur.execute("DELETE FROM r WHERE lname = ?", (i,))








