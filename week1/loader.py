import os 
def load():
    map={}
    data=[]
    with open(".env","r") as file:
        data = file.read().split('\n')
    for lib in data:
        ram = lib.split("=")
        os.environ[ram[0]]=ram[1]
   
    