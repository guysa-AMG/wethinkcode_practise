def main():
    try:
        frac=input("Fraction: ")
        int_rep = convert(frac)
        ret=gauge(int_rep)
        print(ret)
    except ValueError:
        main()
    except ZeroDivisionError:
        main()

def convert(frac :str):
    x,y = frac.split("/")
    
    x,y = int(x),int(y)
    if  y==0:
       
        raise ZeroDivisionError;
    if x > y or y<0 or x<0:
        raise ValueError;
    
    value = (x/y)*100
    return round(value)




def gauge(value :int):
    if value >98:
        return("F")
    elif value<2:
        return("E")
    else:
        return(f"{value}%")
    

if __name__ == "__main__":
    main()

