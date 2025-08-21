from sys import exit,argv as arg
def main():
    arglen=len(arg)
    if(arglen!=2):
        print("Too few command-line arguments") if arglen<2 else print("Too many command-line arguments")
        exit(1)
    elif not arg[1].endswith(".py"):
        print("not a Python file")
        exit(1)
    try:
        with open(arg[1],"r") as file:
            lines=file.readlines()
            nw=[line for line in lines if line.lstrip(" ")!="\n" and not line.lstrip(" ").startswith("#")]
            print(len(nw))
    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()