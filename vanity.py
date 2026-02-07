def main():
    plate = input("Plate: ")
    #print(plate[3].isalnum() and plate[3] != '0')
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
'''
1. must start with two letters
2. max 6 char min 2
3. numbers if there, at last
4. first number cannot be 0
5. no special character(. ! etc)
'''
def is_valid(s):
    if len(s)==2: 
        return ft(s)
    
    elif len(s)==3: 
        return ft(s) and s[2].isalnum() and s[2] != '0'
   
    elif len(s)== 4:
        n = 0
        for c in s :
            if c.isnumeric():
                n +=1
        if n == 0:
            for c in s:
               return c.isalpha()
        elif n==1:
            return ft(s) and s[2].isalpha() and s[3].isalnum() and s[3] !='0'
        elif n==2:
            return ft(s) and s[2].isnumeric() and s[2] !='0' and s[3].isnumeric() 
    
    elif len(s)==5:
        n = 0
        for c in s :
            if c.isnumeric():
                n +=1
        if n == 0:
            for c in s:
               return c.isalpha()
        elif n==1:
            return ft(s) and s[2].isalpha() and s[3].isalpha() and s[4].isalnum() and s[4] !='0'
        elif n==2:
            return ft(s) and s[2].isalpha() and s[3].isalnum() and s[3]!='0' and s[4].isnumeric()
        elif n==3:
            return ft(s) and s[2].isalnum() and s[2] !='0' and s[3].isalnum() and s[4].isnumeric()
    
    elif len(s)==6:
        n = 0
        for c in s :
            if c.isnumeric():
                n +=1
        if n == 0:
            for c in s:
               return c.isalpha()
        elif n==1:
            return ft(s) and s[2].isalpha() and s[3].isalpha() and s[4].isalpha() and s[5].isnumeric() and s[5]!='0'
        elif n==2:
            return ft(s) and s[2].isalpha() and s[3].isalnum() and s[4]!='0' and s[4].isnumeric() and s[5].isnumeric()
        elif n==3:
            return ft(s) and s[2].isalpha() and s[3] !='0' and s[3].isnumeric() and s[4].isnumeric() and s[5].isnumeric() 
        elif n==4:
            return ft(s) and s[2].isalnum() and s[2] !='0' and s[3].isalnum() and s[4].isnumeric() and s[5].isnumeric()
    else:
        return False
    
def ft(x):
    return x[0].isalpha() and x[1].isalpha()


main()