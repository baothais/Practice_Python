import json

def practice_json(data):
    with open("file_json/Exercise1.json", "w") as f:
        json.dump(data, f, indent=2)

def practice_json1():
    with open("file_json/Exercise1.json", "r") as f:
        data = json.load(f)
    return data

def practice_json2(sampleJson):
    data = json.loads(sampleJson)
    print(json.dumps(data, indent=2))
    print(data["key2"])

def practice_json3(sampleJson):
    print(json.dumps(sampleJson, indent=2, separators=(",", " = ")))

def sort_json_keys1(sampleJson):
    data = json.dumps(sampleJson, indent=2, sort_keys=True)
    print(type(data))
    print(data)

def practice_json4(sampleJson):
    data = json.loads(sampleJson)
    # print(json.dumps(data, indent=2))
    print(data["company"]["employee"]["payble"]["salary"])

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def convert_class_to_json(p):
    return p.__dict__

def convert_json_to_class():
    with open("file_json/Exercise1.json", "r") as f:
        data = json.load(f)
    return data

if __name__=="__main__":
    # data = {"key1" : "value1", "key2" : "value2"}
    # sampleJson = """{"key1": "value1", "key2": "value2"}"""
    # sampleJson = {"key1": "value1", "key2": "value2", "key3" : "value3"}
    # sampleJson = {"id": 1, "name": "value2", "age": 29}
    # sampleJson = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'
    # sampleJson = """{
    #     "company": {
    #         "employee": {
    #             "name": "emma",
    #             "payble": {
    #                 "salary": 7000,
    #                 "bonus": 800
    #             }
    #         }
    #     }
    # }"""
    # practice_json(data)
    # print(practice_json1())
    # practice_json2(sampleJson)
    # practice_json3(sampleJson)
    # sort_json_keys1(sampleJson)
    # practice_json4(sampleJson)
    # p = Vehicle("Toyota Rav4", "2.5L", 32000)
    # print(json.dumps(convert_class_to_json(p), indent=2))
    # convert_class_to_json()
    # print(convert_json_to_class())
    # convert_json_to_class(sampleJson)
    p = Vehicle(**convert_json_to_class())
    print(p.price)