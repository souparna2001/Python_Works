# 3. Write a program to handling missing keys

given_keys = {"department": "cs","college":"sahrdaya","semester": 8}

missing_keys = ["college","subjects","fee","department"]


for key in missing_keys:
    value = given_keys.get(key, "missing key")
    print(f"The value for key '{key}' is: {value}")
