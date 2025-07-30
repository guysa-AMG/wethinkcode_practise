def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d :str):
    
    if d[0]=="$":
        return float(d[1:])
    else:
        raise "make sure dollar sign is included ($)"


    


def percent_to_float(p):
    if "%" in p:
        return float(p[:-1])/100
    else:
        raise "make sure percentage sign is included (%)"



main()
