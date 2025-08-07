from pyfiglet import Figlet
import sys

fig = Figlet()

if len(sys.argv)  >1:
    if not sys.argv[1] in ["-f","--font"]:
        sys.exit("Invalid usage") 
    if '-f' in sys.argv or "--font" in sys.argv:
        fig.setFont(font=sys.argv[2])

data=input("input: ")
print(fig.renderText(data))