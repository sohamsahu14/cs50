def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
'''
1. must start with two letters
2. max 6 char min 2
3. numbers if there at last
4. no special character(. ! etc)
'''
def is_valid(s):   
    if 2<=len(s)<=6:
        if len(s)==2 and s[0].isalpha() and s[1].isalpha():
            return True
        elif len(s)==3 and s[0].isalpha() and s[1].isalpha() and s[2].isalnum():
            return True
        elif len(s)==4 and s[0].isalpha() and s[1].isalpha() and s[2].isalnum() and s[3].isalnum:
            return True
        elif len(s)==5 and s[0].isalpha() and s[1].isalpha() and s[2].isalnum() and s[3].isalnum and s[4].isalnum:
            return True
        elif len(s)==6 and s[0].isalpha() and s[1].isalpha() and s[2].isalnum() and s[3].isalnum and s[4].isalnum and s[5].isalnum:
            return True
        else:
            return False

    
    
    else:
        return False


main()