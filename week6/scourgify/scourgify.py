from sys import exit,argv as arg
from tabulate import tabulate

def remove_quot(data):
    rd=""
    for char in data:
        if char != '"' and char != " ":
            rd+=char
    return rd
def format_csv(data):
    splited = data.split("\n")
    maxct=40
    parsed =[remove_quot(line).split(",") for line in splited if line !="" ]
  
    formated=[["first","last","house"]]
    lengthy =len(parsed)
    [formated.append([parsed[index][1],parsed[index][0],parsed[index][2]]) for index in range(1,lengthy)]
    return formated
    


            
def writeCsv(data,fileName):
   
    outfile = open(fileName,"w")
    for line in data:
        print(",".join(line),file=outfile)
    outfile.close()

    


def main():
    arglen=len(arg)
    if(arglen!=3):
        print("Too few command-line arguments") if arglen<3 else print("Too many command-line arguments")
        exit(1)
    elif not arg[1].endswith(".csv"):
        print("not a CSV file")
        exit(1)
    try:
        with open(arg[1],"r") as file:
            data=format_csv(file.read())
            writeCsv(data,arg[2])
    except FileNotFoundError:
        print(f"Could not read {arg[1]}")
        exit(1)

if __name__ == "__main__":
    main()