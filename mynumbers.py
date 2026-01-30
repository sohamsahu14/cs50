def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try: #to handle value error
            x = int(input("whats x? "))
            #print(f"x is {x}")
            # we can return here also
        except ValueError:
            print("x is not an integer") #here we can also use PASS
        else:
            break
    return x     #we can use it instead of break
    
main()
