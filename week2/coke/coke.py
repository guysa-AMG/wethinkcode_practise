due=50

def coke_machine(coin):
    global due

    whitelist=[5,10,25,50]
    amount=int(coin)
    if amount in whitelist:
        due-=amount
        if due<=0:
            print(f"Change Owed: {abs(due)}")
        else:
            print(f"Amount Due: {due}")
    else:
        print(f"Amount Due: {due}")

while due>0:
    
    coin=input("Insert Coin : ")
    coke_machine(coin)
    
    

