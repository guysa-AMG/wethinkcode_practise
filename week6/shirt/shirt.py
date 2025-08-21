from sys import exit,argv as arg

from PIL import Image,ImageOps



def main():
    suffix=[".jpg",".jpeg",".png"]
    arglen=len(arg)

    if(arglen!=3):
        print("Too few command-line arguments") if arglen<3 else print("Too many command-line arguments")
        exit(1)
    elif not arg[2][arg[2].index("."):].lower() in suffix:
        print("Invalid output")
        exit(1)
    elif arg[2][arg[2].index("."):].lower() != arg[1][arg[1].index("."):].lower():
      
        print("Input and output have different extensions")
        exit(1)
    try:
        
        shirt = Image.open("./shirt.png")
        shirt_size=shirt.size
      
        before =Image.open(arg[1])
        before= ImageOps.fit(before,shirt_size)
        before.paste(shirt,shirt)
      
        before.save(arg[2])
        shirt.close()
        before.close()
    except FileNotFoundError:
        print(f"Input does not exist")
        exit(1)

if __name__ == "__main__":
    main()