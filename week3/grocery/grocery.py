
class notes:
    def __init__(self):
        self.groceries={}
 

    def add (self,item):
        item=item.lower()

        if item in self.groceries:
            self.groceries[item]+=1
        else:
            self.groceries[item]=1

    def show(self):
        lst = [item for item in self.groceries]
        lst.sort()
        for key in lst:
            
            print(f"{self.groceries[key]} {key.upper()}")



g_list = notes()
while True:
    try:
        item = input()
    except EOFError:
        g_list.show()
        break
    else:
        g_list.add(item)