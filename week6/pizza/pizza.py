from sys import exit,argv as arg
from tabulate import tabulate


def display(data):
    splited = data.split("\n")
    maxct=40
    parsed =[line.split(",") for line in splited if line !="" ]
    lengthx=len(parsed[0])
    lengthy =len(parsed)
    print(tabulate(parsed[1:],headers=parsed[:1][0],tablefmt="grid"))



            


    


def main():
    arglen=len(arg)
    if(arglen!=2):
        print("Too few command-line arguments") if arglen<2 else print("Too many command-line arguments")
        exit(1)
    elif not arg[1].endswith(".csv"):
        print("not a CSV file")
        exit(1)
    try:
        with open(arg[1],"r") as file:
            display(file.read())
    except FileNotFoundError:
        print("File does not exist")
        exit(1)

if __name__ == "__main__":
    main()