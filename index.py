from gc import get_stats
import json
def ShowMainMenu():
    menu = """\n
---------------------------------
1. Вывести все записи
2. Вывести запись по полю
3. Добавить запись
4. Удалить запись по полю
5. Выйти из программы 
---------------------------------
"""
    return menu
def showInfo(data, stars_id=0):
    for stars in data:
        if stars_id == 0:
            print(f"""
            Номер записи: {stars["id"]},
            Название: {stars["name"]},
            Название созвездия: {stars["constellation"]},
            Видна ли без телескопа: {f"да" if stars["is_visible_stars"]  else "нет"},
            Радиус звезды: {stars["radius"]}
            """)
        else:
             if stars_id == stars.get("id"):
               print(f"""
                Номер записи: {stars["id"]}
                Название: {stars["name"]}
                Название созвездия: {stars["constellation"]}
                Видна ли без телескопа: {f"да" if stars["is_visible_stars"] else "нет"}
                Радиус звезды: {stars["radius"]}""")
def InputAndCheck():
    def ErrorMessage(value):
        print(f"""
              Введено недопустимое значение {value},
              Повторите попытку:\n""")
    def is_string(input_str):
            if isinstance(input_str, str) and (not input_str.isdigit()):
                return True
            ErrorMessage(input_str)
            return False
    def checkAnswer(answer):
            is_string(answer)
            if (answer.lower() == "да") or (answer.lower() == "нет"):
                return True
            else:
                ErrorMessage(answer)
                return False
    def turnToFloat(input_num):
        try:
            return True, float(input_num)
        except (ValueError, TypeError):
            ErrorMessage(input_num)
            return False, float("NaN")
    current_step = 1
    new_data = []
    while current_step < 5:
        if current_step == 1:
            new_name = input("Введите название новой звезды: ")
            new_data.append(new_name)
        elif current_step == 2:
            new_constellation_name = input("Введите название созвездия в котором находится новая звезда: ")
            new_data.append(new_constellation_name)
        elif current_step == 3:
            new_is_visible_stars = input("Можно увидеть без телескопа(да/нет): ")
            if not checkAnswer(new_is_visible_stars):
                continue
            new_data.append(new_is_visible_stars)
        elif current_step == 4:
            is_float, new_radius = turnToFloat(input("Введите радиус новой звезды: "))
            if not is_float:
                continue
            new_data.append(new_radius)
        current_step += 1
    return new_data
def createNewStar(id, name, constellation, visible, price):
    new_stars={
        "id":id,
        "name":name,
        "constellation":constellation,
        "is_visible_stars":True if visible.lower()=="да" else False,
        "price":price
    }
    return new_stars
def addNewStar(data, new_stars):
    data.append(new_stars)

def deleteStar(data, id, flag):
    for stars in data:
        if id == stars.get("id", 0):
            data.remove(stars)
            flag = True
            break
    return flag
def outprint(count, actions_list, actions_count):
    print(f"""
    Действия завершены
    Количество операций: {count}\n""")
    count=1
    print("Выполненные операции: ")
    for act in actions_list:
        print(f"""
        {act}: {actions_count[count]}""")
        count+=1
    return None
def checkId(id):
    while not id.isdigit():
        print("""Введено некорректное значение
              Повторите попытку:\n""")
        id = input("Введите номер желаемой записи: ")
    return id
with open("flowers.json", 'r', encoding = 'utf-8') as file:
    data = json.load(file)
count = 0
actions_list = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
while True:
    print(ShowMainMenu())
    num = int(input("Введите желаемый номер пункта: "))
    find = False
    if num ==1:
        showInfo(data)
        count+=1
        actions_count[1]+=1
    elif num ==2:
        id = input("Введите номер записи: ")
        id = checkId(id)
        for stars in data:
            if id == stars.get("id",0):
                showInfo(data, id)
                find =True
                break
        count+=1
        actions_count[2]+=1
        if not find:
            print("Такой записи не существует!")
    elif num ==3:
        find = False
        last_id = int(data[-1].get("id")) +1
        last_id = str(last_id)
        new_name, new_constellation_name, new_is_visible_stars, new_radius = InputAndCheck()
        new_stars = createNewStar(last_id, new_name, new_constellation_name, new_is_visible_stars, new_radius)
        addNewStar(data,new_stars )
        with open("stars.json", 'w', encoding = 'utf-8') as outfile:
            json.dump(data, outfile)
        print("Новая запись успешно добавлена! :D")
        count+=1
        actions_count[3]+=1
    elif num ==4:
        id = input("Введите номер записи: ")
        id = checkId(id)
        find=False
        find=deleteStar(data, id, find)
        if not find:
            print("Такой записи не существует")
        else:
            with open("flowers.json", 'w', encoding = 'utf-8') as outfile:
                json.dump(data, outfile)
            print("Запись успешно удалена")
        count+=1
        actions_count[4]+=1
    elif num == 5:
        count+=1
        actions_count[5]+=1
        outprint(count, actions_list, actions_count)
        break
    else:
        print("Такого номера нет!")