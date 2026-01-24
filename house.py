name = input("Whats your name ? ")

match name:
    case "harry" | "hermoine" | "ron":
        print("gryffindor")
    case "draco":
        print ("slythrin")
    case _:
        print("who ?")
