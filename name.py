import sys

try:
    print("hello, my name is", sys.argv[1]) #zeroth element contains the name of program
except IndexError:
    print("Too few arguments")