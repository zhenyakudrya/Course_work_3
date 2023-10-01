import json
from datetime import datetime
import re


def load_operations(file):
    """
    Считывание json файла, добавление операций в список
    """
    with open('../operations.json', mode='r', encoding='utf-8') as file:
        file_json = json.load(file)
    operations_list = []
    for item in file_json:
        if 'id' in item:
            operations_list.append(item)
    return operations_list


def sort_by_date(operations_list):
    """
    Сортировка списка операций по дате (от новых к старым)
    """
    sorted_operations_list = []
    sorted_operations_list = sorted(operations_list,
                                    key=lambda x: x['date'], reverse=True)
    return sorted_operations_list


def executed_operations(operations_list):
    """
    Выборка только выполненных операций
    """
    executed_operations_list = []
    for item in operations_list:
        if item['state'] == "EXECUTED":
            executed_operations_list.append(item)
    return executed_operations_list


def last_operations(operations_list, n):
    """
    Выбор n последних операций
    """
    last_operations_list = operations_list[0:n]
    return last_operations_list


def date_conversion(operations_list):
    """
    Конвертация даты в вид "дд.мм.ггг"
    """
    for item in operations_list:
        item["date"] = item["date"].replace("T", " ")
        item["date"] = datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S.%f")
        item["date"] = item["date"].strftime('%d.%m.%Y')
    return operations_list


def encryption(operations_list):
    """
    Шифровка данных карт, счетов
    """
    for item in operations_list:
        if 'from' in item:
            if len(re.findall(r'\d', item["from"])) == 16:
                item["from"] = re.sub(r'(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})',
                                      r'\1 \2** **** \5', item["from"])
            elif len(re.findall(r'\d', item["from"])) == 20:
                item["from"] = re.sub(r'(\d{16})(\d{4})', r'**\2', item["from"])
        if len(re.findall(r'\d', item["to"])) == 16:
            item["to"] = re.sub(r'(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})',
                                r'\1 \2** **** \5', item["to"])
        elif len(re.findall(r'\d', item["to"])) == 20:
            item["to"] = re.sub(r'(\d{16})(\d{4})', r'**\2', item["to"])
    return operations_list
