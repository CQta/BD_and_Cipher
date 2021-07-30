from prettytable import PrettyTable
import CRUD
choice = 1
order_mapper = CRUD.OrderMapper()
while choice != 0:
    print('Ввести данные-1, Удалить данные-2, Просмотр данных-3, Выход-0')
    choice = int(input())
    if choice == 0:
        break
    if choice == 3:#Вывод
        Display_info = []
        rows = order_mapper.show()
        table_name = ('ID', 'Name', 'Surname', 'Gender', 'Salary')
        table = PrettyTable(table_name)
        for row in rows:
            for j in range(5):
                d_name = CRUD.decoder(row[j])
                Display_info.append(d_name)
            table.add_row(Display_info)
            Display_info.clear()
        print(table)

    if choice == 1:#Ввод
        print('Введите кол-во людей')
        n = int(input())
        while n != 0:
            print('Введите имя')
            f_name = input()
            f_name = CRUD.chiper(f_name)
            print('Введите фамилию')
            l_name = input()
            l_name = CRUD.chiper(l_name)
            print('Введите пол')
            gender = input()
            gender = CRUD.chiper(gender)
            print('Введите зарплату')
            salary = int(input())
            get_info = (f_name, l_name, gender, salary)
            order_mapper.create(get_info)
            n = n - 1

    if choice == 2:#Удаление
        print('Введите id  для удаления, для удаления всех данных введите all ')
        id = input()
        if id == "all":
            order_mapper.delete_all()
        else:
            order_mapper.delete_by_id(id)









