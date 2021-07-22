import sqlite3
import CRUD
choice = 1
order_mapper = CRUD.OrderMapper()
while choice != 0:
    print('Ввести данные-1, Удалить данные-2, Просмотр данных-3, Выход-0')
    choice = int(input())

    if choice == 0:
        break

    if choice == 3:#Вывод
        j = 1
        Display_info = []
        rows = order_mapper.Show()
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
            order_mapper.Create(get_info)
            n = n-1

    if choice == 2:#Удаление
        print('Введите id  для удаления, для удаления всех данных введите all ')
        d = input()
        if d =="all":
            order_mapper.Del()
        else:
            order_mapper.Del_by_lname(d)









