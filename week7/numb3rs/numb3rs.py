
import sys


def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = ip.split(".")
    if len(octet)!=4:
        return False
    for oc in range(len(octet)):
        try:
            if int(octet[oc])>255 or (oc>0 and int(octet[oc])<0) or (oc == 0 and int(octet[oc])<=0):
                return False
    
        except:
            return False
    return True





if __name__ == "__main__":
    main()
