def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s :str):
    blacklist=['.',':', ';', '<', '=', '>', '?', '@',' ']
    state=True
    #flags if the length is not in within the limit
    if len(s)<2 or len(s)>6:
        state=False
    
    #flags if the first two characters is not and alphabet
    if not s[0:2].isalpha():
        state=False

    for char in range(len(s)):
        #flags if the first number is zero
        if s[char] == "0" and s[char-1].isalpha():
            state=False
        # flags at an point where the current character is an alphabet and are numbers before it 
        if s[char].isalpha() and not s[:char+1].isalpha():
            state=False
        if s[char] in blacklist :
            state=False
        
    
    return state


main()

