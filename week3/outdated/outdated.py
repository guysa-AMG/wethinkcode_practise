def date():
    months=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    data = input ("date: ")

    la = data.split()[0].split("/")

    try:
        if len(la) == 3:
            if int(la[1]) >31 or int(la[0])>12:
                raise ValueError
            print(f"{la[2]}-{int(la[0]):02}-{int(la[1]):02}")

            return
        elif (splat:=data.split())[0] in months:
            month = months.index(splat[0])+1
            day = splat[1][:-1]
            year = splat[2]
            if int(day) >31 or int(month)>12:
                raise ValueError
            print(f"{year.lstrip()}-{int(month):02}-{int(day):02}")
            return
        else:
            date()
    except:
        print("error raised")
        date()
date()


