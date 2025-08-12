import json


def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data


print(read_json("/Users/rybin/PycharmProjects/homework_oop/data/products.json"))
