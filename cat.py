def main():
    x = get_number()
    meow(x)

def get_number():
    while True:
        n = int(input("whats n? "))
        if n > 0:
            break
    return n
    
def meow(y):    
    for _ in range(y):
        print("meow")

main()