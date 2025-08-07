

names=[]
def parsed():
    global names
    parsed="Adieu, adieu, to"
    l_count=len(names)
    for name_index in range(l_count):
        if name_index>0 and name_index==(l_count-1):
            if l_count >2:
                parsed+=f", and {names[name_index]}"
            else:
                parsed+=f" and {names[name_index]}"
            break
        elif name_index>0:
            parsed+=f", {names[name_index]}"
        else:
            parsed+=f" {names[name_index]}"
    return parsed

while True:
    try:
        name=input("Name: ")
        names.append(name)

    except EOFError:
        print(parsed())
        break