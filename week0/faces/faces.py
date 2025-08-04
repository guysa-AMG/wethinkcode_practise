

#sad face is 128577
#happy face is 128578

def converter(input_data :str):
    return input_data.replace(":)",chr(128578)).replace(":(",chr(128577))

data = input()
converted = converter(data)

print(converted)