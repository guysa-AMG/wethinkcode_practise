def shortner(string):
    parsed=""
    vowels=["a","e","i","o","u"]
    for char in string:
        if not char.lower()  in vowels:
            parsed+=char
    return parsed
value = input("Input: ")
value = shortner(value)
print(value)
