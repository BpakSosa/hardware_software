def decimalToBinary(n):
    n = int(n)
    #turns numberstring into an integer. this was the source of several hours of troubleshooting oh my god
    decimal = 0
    #starts at 0 because its the number that gets its value accumulated upwards, will be our answer
    power = 1
    #power starts at 1 and will be multiplied later by the next binary digits number
    while n>0:
        #starts the loop that ends calculations once the original number inputed is less than 1
        rem = n%2
        #this extracts and becomes the right most bit
        n = n//2
        #this variables calculation takes or slides the digits over by one removing the next smallest bit in our number
        decimal += rem*power
        #the bit extracted (0-9) gets multiplied by power which starts at 1 and increments by values of 2
        power = power*10
        #increments the power variaable for each digit it goes to the left of per while cycle
    return decimal
    #returns the number accumulated to the next time it gets called

def start():
    decimal_number = (input("This thing turns base10 into binary, put in your fav numbers and see what they look like in binary\n"))
    if decimal_number.isnumeric() == True:
        print(decimal_number, "in binary is",decimalToBinary(decimal_number))
    #this is the finalizing text indicating your result before the loop goes back to the menu
    elif decimal_number == "":
        print("gotta put somethin in there to convert\n")
        start()
    else:
        print("please put in a number next time, this poor thing cant work with text\n")
        start()
    #these lines check if letters or nothing instead of numbers were placed in the code which would usually result in a crash

start()
print("thanks for using this calculator")
#99% of this code was like scrapped from the project file
