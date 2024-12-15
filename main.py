import json # импорт модуля json для работы с json-файлами
# открытие файла flowers.json в режиме чтения с кодировкой utf-8
with open("stars.json", 'r', encoding = 'utf-8') as file:  
    data = json.load(file) # загрузка данных из файла в переменную data
count = 0
actions_list = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы",
    ] 
               
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
while True:
    print("""
    1: Вывести все записи
    2: Вывести запись по полю
    3: Добавить запись
    4: Удалить запись по полю
    5: Выйти из программы
""")
    num = int(input("Введите номер выбранного пункта: "))
    if num == 1:
        for stars in data:
            print(f"""
            Номер записи: {stars["id"]}
            Название: {stars["name"]}
            Название созвездия в котором находится данная звезда: {stars["constellation"]}
            Возможно ли увидеть эту звезду невооруженным взглядом,без телескопа: {"да" if stars["is_visible_star"] == True else "нет"}
            Радиус данной звезды: {stars["radius"]}
        """)
        count += 1
        actions_count[1] +=1 
    elif num == 2:
        find = False
        id = input("Введите номер записи: ").strip()
        while not id.isdigit:
            print("Введено некорреткное значение")
            id = input("\nВведите номер записи: ")
        for stars in data:
            if id == stars.get("id",0):
                print(f"""
                    Номер записи: {stars["id"]}
                    Название: {stars["name"]}
                    Название созвездия в котором находится данная звезда: {stars["constellation"]}
                   Возможно ли увидеть эту звезду невооруженным взглядом,без телескопа: {"да" if stars["is_visible_star"] == True else "нет"}
                    Радиус данной звезды: {stars["radius"]}          
                """)
                find = True
                break
        count += 1
        actions_count[2]+=1
    elif num == 3:
        find = False
        id = input("Введите новый номер записи: ").strip()
        while not id.isdigit:
            print("Введено некорректное значение. Повторите попытку: ")
            id = int(input("Введите новый номер записи: "))
        for stars in data:
            if stars.get("id",0) == id:
                find = True
                break
        if find:
             print("Такой номер уже существует")
             find = True
             break
        else:
            new_name = input("Введите название: ")
            new_constellation_name = input("Введите название созвездия в котором находится данная звезда или '-': ")
            new_is_visible_stars = input("Возможно увидеть без телескопа(да/нет): ")
            flag = False 
            if new_is_visible_stars.isdigit:
                flag = True
            while new_is_visible_stars not in ["да", "нет"] or find:
                print("Введены неверные данные, повторите попытку")
                new_is_visible_stars = input("Возможно увидеть без телескопа: ")
                if new_is_visible_stars.isdigit:
                    flag = True
                    continue
                new_is_visible_stars = new_is_visible_stars.lower().strip()
                flag = False
            new_radius = input("Введите радиус данной звезды: ")
            if not new_radius.isdigit():
                while not new_radius.isdigit():
                    print("Введено неверное значение!")
                    print("\nПовторите попытку!")
                    new_radius = input("Введите радиус данной звезды: ")
                new_radius = float(new_radius)
            new_stars = {
                "id": id,
                "name": new_name,
                "constellation":new_constellation_name,
                "is_visible_stars": True if new_is_visible_stars.lower() == "да" else False,
                "radius": new_radius
            }
            data.append(new_stars)
            with open("stars.json", 'w', encoding = 'utf-8') as out_file:
                json.dump(data, out_file)
            print("\nНовая запись успешно добавлена :)")
        count+=1
        actions_count[3]+=1
    elif num == 4:
        id = input("Введите номер записи, которую желаете удалить: ")
        while not id.isdigit:
            print("Введено неверное значение!")
            input("Введите номер записи ещё раз: ")
        find = False
        for stars in data:
            if stars.get("id", 0) == id:
                data.remove(stars)
                find = True
                break
        if not find:
            print("Запись не найдена.")
        with open("stars.json", 'w', encoding = 'utf-8') as out_file:
            json.dump(data, out_file)
            print("\nЗапись успешно удалена.")
        count+=1
        actions_count[4]+=1
    elif num == 5:
        count+=1
        actions_count[5]+=1
        print(f"""\nПрограмма завершена. 
              \nОбщее количество выполненных операций: {count}""")
        print("\nСводка информации о каждом действии: ")
        count = 1
        for action in actions_list:
            print(f"""
                  {action}: {actions_count[count]}""")
            count +=1
        break
    else: 
        print("Такого номера нет.")