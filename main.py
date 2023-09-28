from functions import (load_operations, sort_by_date, executed_operations,
                       last_operations, date_conversion, encryption)

if __name__ == '__main__':

    # Загрузка json файла
    operations_json = load_operations('operations.json')

    # Сортировка списка операций по дате
    operations_list = sort_by_date(operations_json)

    # Выбор только выполненных операций
    operations_list = executed_operations(operations_list)

    # Выбор последних 5 операций
    operations_list = last_operations(operations_list, 5)

    # Конвертация даты в вид "дд.мм.ггг"
    operations_list = date_conversion(operations_list)

    # Шифровка данных карт, счетов
    operations_list = encryption(operations_list)

    # Вывод информации на экран
    for item in operations_list:
        if "Перевод" in item["description"]:
            print(f'{item["date"]} {item["description"]}\n'
                  f'{item["from"]} -> {item["to"]}\n'
                  f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n')
        elif "Открытие" in item["description"]:
            print(f'{item["date"]} {item["description"]}\n'
                  f'{item["to"]}\n'
                  f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n')
