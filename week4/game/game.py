
from random import randint

lvl=10
guess=""

while guess!=lvl:
    try:
        lvl=int(input("Level: "))
        if lvl>0 :
            ans = randint(1,lvl)
            
            
            while guess != ans:
                try:
                    guess=int(input(f"guess: "))
                    if guess>0:
                        if guess> ans:
                            print("Too large!")
                        else:
                            print("Too small!")
                    
                except ValueError:
                    continue

            print("Just right!")
            break

            
    except ValueError:
        continue
    


