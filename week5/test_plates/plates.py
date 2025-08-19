def main():
    messeage = input("plates: ")
    valid = is_valid(messeage)
    if valid:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    state= True
    str_len=len(s)
    blacklist = [".","!","@","#","$","%","*"]
    #check if the input is inbetween 2 to 6 characters
    #check if the first two char is Alphabet
    #make sure that the first number in the char in plate is not a 0
    #make sure the numbers don't appear in the middle
    if s[:2].isalpha() and str_len>=2 and str_len<=6:
        
        for index in range(str_len):
            
            if  (index+1 <str_len-1 and s[index].isnumeric()) and s[index+1].isalpha():
            
                state=False
            elif  (index !=0 and index+1 < str_len-1) and s[index].isalpha() and s[index+1].isnumeric() and s[index+1] =="0":
                    state=False
            elif s[index] in blacklist:
            
                state=False
          
                
    else:
      \
        state =False
    return state

if __name__ == "__main__":
    main()

            
            

                

            