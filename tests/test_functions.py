from src.functions import *
import pytest
import json


@pytest.fixture
def list_fixture():
    with open('src/operations.json', mode='r', encoding='utf-8') as file:
        file_json = json.load(file)
    operations_list = []
    for item in file_json:
        if 'id' in item:
            operations_list.append(item)
    return operations_list


def test_sort_by_date(list_fixture):
    for i in range(0, len(list_fixture) - 1):
        assert sort_by_date(list_fixture)[i]['date'] > sort_by_date(list_fixture)[i + 1]['date']


def test_executed_operations(list_fixture):
    for item in executed_operations(list_fixture):
        assert item["state"] == "EXECUTED"


def test_last_operations(list_fixture):
    assert len(last_operations(list_fixture, 5)) == 5


def test_date_conversion(list_fixture):
    assert date_conversion(list_fixture)[0]['date'] == '26.08.2019'


def test_encryption(list_fixture):
    assert encryption(list_fixture)[0]['from'] == 'Maestro 1596 83** **** 5199'


def test_load_operations(list_fixture):
    assert len(load_operations(list_fixture)) == 100
