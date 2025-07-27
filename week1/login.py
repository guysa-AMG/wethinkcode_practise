import os
from loader import load

load()

def verify(password):
    if password.lower() == os.getenv("password").lower():
        return True
    else:
        return False

prompt="password: "
print("\nlogin to gain access\n")
value = input(prompt)
attempt =1
while(not verify(value) and (10-attempt)>0):
    print("[x] incorrect password try again {} atempts left".format(10-attempt))
    value = input("try again : ")
    attempt+=1

if (verify(value)):
    print("[ok] password correct")
    print(os.getenv("message"))
else:
    print("\n\n[X] Authentication Failed\n\n")
