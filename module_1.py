import os


LOW = "1"
MEDIUM = "2"
HIGH = "3"
PRIORITY = {LOW: "1 - low", MEDIUM: "2 - medium", HIGH: "3 - high"}

NEW = "1"
IN_PROGRESS = "2"
COMPLETED = "3"
STATUS = {NEW: "1 - new", IN_PROGRESS: "2 - in progress", COMPLETED: "3 - completed"}


def add_new_task(tasks):
    name = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    priority = input("Задайте приоритет задачи 1 - низкий, 2 - средний, 3 - высокий: ")

    while priority not in ["1", "2", "3"]:
        print("Введите корректное значение приоритета")
        priority = input(
            "Задайте приоритет задачи 1 - низкий, 2 - средний, 3 - высокий:  "
        )

    status = input("Задайте статус задачи 1 - новая, 2 - в процессе, 3 - завершена: ")

    while status not in ["1", "2", "3"]:
        print("Введите корректное значение статуса")
        status = input(
            "Задайте статус задачи 1 - новая, 2 - в процессе, 3 - завершена: "
        )

    new_task = {
        id: {
            "Name": name,
            "Description": description,
            "Priority": PRIORITY[priority],
            "Status": STATUS[status],
        }
    }

    tasks.update(new_task)


def check_task(tasks):
    print("1 - Отобразить задачи в изначальном виде")
    print("2 - Отсортировать по статусу")
    print("3 - Отсортировать по приоритету")
    print("4 - Осуществить поиск по названию или описанию")
    choice = input("Введите номер операции: ")
    match choice:
        case "1":
            print(tasks)
        case "2":
            sorted_by_status = sorted(
                tasks.items(), key=lambda element: element[1]["Status"]
            )
            print("Отсортированный список задач по статусу:")
            print(sorted_by_status)
        case "3":
            sorted_by_priority = sorted(
                tasks.items(), key=lambda element: element[1]["Priority"]
            )
            print("Отсортированный список задач по приоритету:")
            print(sorted_by_priority)
        case "4":
            to_search = input("Введите название или описание: ")
            for key, value in tasks.items():
                if value["Description"] == to_search or value["Name"] == to_search:
                    print(key, value)
        case _:
            print("Неправильный выбор!")


def refresh_task(tasks):
    refresh_id = input("Введите id задачи, которую хотите обновить: ")
    if refresh_id.isnumeric():
        refresh_id = int(refresh_id)
        if refresh_id in tasks:
            print("1 - название")
            print("2 - описание")
            print("3 - приоритет")
            print("4 - статус")
            choice = input("Выберите какое поле обновить: ")
            match choice:
                case "1":
                    name = input("Введите новое название задачи: ")
                    tasks[refresh_id]["Name"] = name
                case "2":
                    description = input("Введите новое  описание задачи: ")
                    tasks[refresh_id]["Description"] = description
                case "3":
                    priority = input(
                        "Задайте новый приоритет задачи 1 - низкий, 2 - средний, 3 - высокий:  "
                    )
                    while priority not in ["1", "2", "3"]:
                        print("Введите корректное значение приоритета")
                        priority = input(
                            "Задайте новый приоритет задачи 1 - низкий, 2 - средний, 3 - высокий:  "
                        )

                    tasks[refresh_id]["Priority"] = priority

                    status = input(
                        "Задайте новый статус задачи 1 - новая, 2 - в процессе, 3 - завершена: "
                    )
                    while status not in ["1", "2", "3"]:
                        print("Введите корректное значение статуса")
                        status = input(
                            "Задайте новый статус задачи 1 - новая, 2 - в процессе, 3 - завершена: "
                        )
                    tasks[refresh_id]["Status"] = status
                case _:
                    print("Неправильный выбор!")
        else:
            print(f"Такого id {id} нет в списке, проверьте ввод!")
    else:
        print("Введите корректный id!")


def delete_task(tasks):
    id_to_del = input("Введите id задачи, которую хотите удалить: ")
    if id_to_del.isnumeric():
        if int(id_to_del) in tasks:
            del tasks[int(id_to_del)]
            print(f"Задача с id: {id}  удалена")
        else:
            print(f"Задачи с таким id: {id} нет в списке")
    else:
        print("Введите id корректно!")


def write_tasks_to_file(tasks):
    with open("module_1.txt", "w") as file:
        for key, value in tasks.items():
            file.write(f"{key}:{value}\n")


def read_tasks_from_file(tasks):
    if not os.path.exists("module_1.txt"):
        with open("module_1.txt", "w") as file:
            print("Файл создан")
    with open("module_1.txt", "r") as file:
        for line in file:
            element = line.strip().split(":", 1)
            key = int(element[0])
            value = element[1]
            # key, value = line.strip().split(":", 1)
            tasks.update({key: value})


tasks = {}
read_tasks_from_file(tasks)
try:
    id = list(tasks.items())[-1][0]
except IndexError:
    id = 0

while True:
    print("1 - Создать новую задачу")
    print("2 - Просмотреть задач")
    print("3 - Обновить задачу")
    print("4 - Удалить задачу")
    print("0 - Выйти из программы")
    text = input("Введите номер операции: ")
    if text == "1":
        id += 1
        add_new_task(tasks)
    elif text == "2":
        check_task(tasks)
    elif text == "3":
        refresh_task(tasks)
    elif text == "4":
        delete_task(tasks)
    elif text == "0":
        write_tasks_to_file(tasks)
        break
    else:
        print("Неверный номер операции")
