
from helper.tools import *



class Person:
    def __init__(self,name,surname,age,job):
        self.name=name
        self.surname=surname
        self.age=age
        self.job=job
    def __repr__(self):
        return "name:{}\nage:{}\njob:{}".format(self.name,self.age,self.job)
        

me=Person("Guysa","Ahmed",34,"Engineer")
print(me.name)
printer(parsed_args.args,fg="g",bg="w")
log(me,level="error")