
import datetime
import sys

def cprint(message,fg="w",bg="B",end="\033[0m\n"):
    colour_fg_map={"B":"\033[30m", "r":"\033[31m", "g":"\033[32m", "y":"\033[33m", "b":"\033[34m", "m":"\033[35m", "c":"\033[36m", "w":"\033[37m"}
    colour_bg_map={"B":"\033[40m", "r":"\033[41m", "g":"\033[42m", "y":"\033[43m", "b":"\033[44m", "m":"\033[45m", "c":"\033[46m", "w":"\033[47m"}
    control=colour_fg_map[fg]+colour_bg_map[bg]
    return f"{control}{message}"

def printer(message,fg="w",bg="B",end="\033[0m\n"):
    print(cprint(message,fg,bg),end=end)

def log(message,level="verbose"):
    cc={"verbose":"w","success":"g","warning":"y","error":"r"}
    with open("logFile.log","a")as file:
        print(cprint(f"[{level}] ",fg= cc[level])+cprint(message),)
        print(f"[{level}] {message}",file=file)

