class strnum:
    def __init__(self,str):
        num1,op,num2=str.split()
        self.x = int(num1)
        self.z = int(num2)
        self.op = op

    def equals(self):
        operation = {"/":self.divide,"+":self.add,"*":self.multiply,"-":self.subtract}
        method = operation[self.op]
        return float(method())
            

    def add(self):
        return self.x+self.z
    
    def subtract(self):
        return self.x - self.z
    
    def multiply (self):
        return self.x * self.z
    
    def divide (self):
        return self.x / self.z

value=input("Expression: ")

data =strnum(value)

print(data.equals())