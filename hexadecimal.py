def check_selection(numbers): #verify if it is a hexidecimal
    hex_list = ["A", "B", "C", "D", "E", "F", "0", "1",
                "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() in hex_list: # check if the nubmer is now in the hex list along with uppercasing any possible letters for the base16 characters
            return(True)
            #this simple logic flip allows for the code to instead return false on a number that isnt in the list it returns true if it is
        else:
            print("nuh uh thats not a hexadeimal number")
            return(False)
        return(True)

def main():
    good_selection = False
    while not good_selection:
        selection = input("type a hexademial number:")
        good_selection = check_selection(selection)
        #i wouldnt recommend only using good_selection as it removes an entire variable out of control and could make checking more difficult and disorganized
    print("nice one", selection, "is a hexadeimal number")

if __name__ == "__main__":
    main()
