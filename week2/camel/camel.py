def toSnake (string):
    parsed=""
    for char in string:
        if char.isupper() :
            parsed+="_"
        parsed+=char.lower()
    return parsed
value=input("camelCase: ")
print(toSnake(value))