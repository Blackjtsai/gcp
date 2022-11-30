import json

# 基本
file = open("data1.txt", mode="w", encoding="UTF-8")
file.write("Hello file\n222\n測試測試測試測試測試2")
file.close()

# 儲存

# 使用with讀取
with open("data1.txt", mode='r') as file:
    for str in file:
        print(str)


# 使用with讀取json
with open("data1_json.json", mode='r') as file:
    data = json.load(file)
    print(data)
    print(data["name"])

data["name"] = "ellin"
with open("data1_json.json", mode='w') as file:
    json.dump(data, file)
