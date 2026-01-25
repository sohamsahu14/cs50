def main():
    print_square(3)

def print_square(s):
    for i in range(s):
        for j in range(s):
            print("#", end="")
        print()


main()