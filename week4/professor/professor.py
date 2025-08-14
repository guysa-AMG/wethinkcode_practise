from random import randint,randrange,seed


def professor():
    lvl=input("LVL: ")
    while not lvl.isalnum():
        lvl=input("LVL: ")
    max = 10**int(lvl)
    x,y=(randrange(0,max),randrange(0,max))
    tries=0
    
    

        

def main():

    lvl = get_level()
    points=0
    for _ in range(10):
        tries=0
        x,y = [generate_integer(lvl),generate_integer(lvl)]
        ans = input(f"{x} + {y} = ")
        condition = int(ans) == sum([x,y])
        if condition:
            points+=1
        else:
            print("EEE")
            for n in range(2):
                ans = input(f"{x} + {y} = ")
                condition = int(ans) == sum([x,y])
                if condition:
                    points+=1
                    break
               

                elif n==1:
                    print("EEE")
                    print(f"{x} + {y} = {sum([x,y])}")
                else:
                    print("EEE")
                    
    print(f"Score: {points}")




def get_level():
    while True:
        try:
            levels=[i for i in range(1,4)]
            lvl = input("Level: ")

            while not( lvl.isalnum() and int(lvl) in levels):
                lvl = input("Level: ")
            break
        except ValueError:
            continue
    return int(lvl)




def generate_integer(level):
    maxl = 10**int(level)-1
    minl =  10**(int(level)-1) if level!=1 else 0

    return randint(minl,maxl)


if __name__ == "__main__":
    main()




    
        