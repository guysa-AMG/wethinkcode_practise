


def something():
    data=input("Fraction: ")
    try:
        x,y=data.split("/")
        if int(x)<=int(y) and not int(x)<0 and not int(y)<0:
            value=(int(x)/int(y))*100
            
            if value >98:
                print("F")
            elif value<2:
                print("E")
            else:
                print(f"{round(value)}%")
        else:
            something()
            

    except :
        something()

something()

