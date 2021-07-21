import sqlite3
import CRUD
choice = 1
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""create table if not exists r(id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, fname text, lname text, gender text, plat int)""")
conn.commit()

while choice != 0:
    print('Ввести данные-1, Удалить данные-2, Просмотр данных-3, Выход-0')
    choice = int(input())

    if choice == 0:
        break

    if choice == 3:#Вывод
        j = 1
        Display_info = []
        rows = CRUD.OrderMapper.Show(cur)
        for row in rows:
            for j in range(5):
                d_name = CRUD.Decoder(row[j])
                Display_info.append(d_name)
            print(Display_info)
            Display_info.clear()

    if choice == 1:#Ввод
        print('Введите кол-во людей')
        n = int(input())
        while n != 0:
            print('Введите имя')
            name = input()
            name = CRUD.Chiper(name)
            print('Введите фамилию')
            s_name = input()
            s_name = CRUD.Chiper(s_name)
            print('Введите пол')
            gen = input()
            gen = CRUD.Chiper(gen)
            print('Введите зарплату')
            zar = int(input())
            get_info = (name, s_name, gen, zar)
            CRUD.OrderMapper.Create(get_info, cur)
            conn.commit()
            n = n-1

    if choice == 2:#Удаление
        print('Введите id  для удаления, для удаления всех данных введите all ')
        d = input()
        if d =="all":
            CRUD.OrderMapper.Del(cur)
        else:
            CRUD.OrderMapper.Del_by_lname(cur, d,conn)









