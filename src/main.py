from functions import *

if __name__ == '__main__':

    # Загрузка json файла, сортировка списка операций по дате
    operations_list = sort_by_date(load_operations('operations.json'))

    # Выбор только выполненных последних 5 операций
    operations_list = last_operations(executed_operations(operations_list), 5)

    # Конвертация даты в вид "дд.мм.ггг", шифровка данных карт, счетов
    operations_list = encryption(date_conversion(operations_list))

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
