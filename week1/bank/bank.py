
def manager(greeting):
    parsed_greeting=greeting.lower()
    if "hello" in parsed_greeting:
        return "$0"
    elif parsed_greeting[0] == "h":
        return "$20"
    else:
        return "$100"
value = input("Greeting : ")

cost = manager(value)

print(cost)