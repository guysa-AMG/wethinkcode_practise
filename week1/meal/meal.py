def main():
    meals = {7:"breakfast time",12:"lunch time",18:"dinner time"}
    data = input("what time is it: ")
    hour =convert(data)
    try:
        if (int(hour) in meals):
            print(meals[int(hour)])
        elif hour-1 in meals:
            print(meals[hour-1])
    except:
        pass
    

def convert(time):

    hour,minute = time.split(":")
    if "pm" in time:
        hour=int(hour)+12
    hours=(int(hour)+int(minute[:2])/60)
    return hours






if __name__ == "__main__":
    main()