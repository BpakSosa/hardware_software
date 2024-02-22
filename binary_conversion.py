#Code by Benicio Sosa, this program is made to convert between binary and decimal.
print("This program was made to either convert Decimal into Binary or vice versa")
def menu():
    print("Select your conversion method")
    print("[1] Decimal to Binary")
    print("[2] Binary to Decimal")
    print("[0] exit program")
#this simply prints out the selections available along with the top most text

def decimalToBinary(n):
    n = int(n)
    decimal = 0
    power = 1
    while n>0:
        rem = n%2
        n = n//2
        decimal += rem*power
        power = power*10
    return decimal

#EXPLAINATION BELOW STARTING ON LINE 54: this code was an inversion of the code on that line which has the explaination
def option1():
    decimal_number = (input("enter a positive decimal number\n"))
    if decimal_number.isnumeric() == True:
        print(decimal_number, "in binary is",decimalToBinary(decimal_number))
        #this is the finalizing text indicating your result before the loop goes back to the menu
    elif decimal_number == "":
        print("gotta put somethin in there to convert\n")
        option1()
    else:
        print("please put in a number next time, this poor thing cant work with text\n")
        option1()
        #these lines check if letters or nothing instead of numbers were placed in the code which would usually result in a crash
def is_binary(binary_number):
    for digit in binary_number:
        if digit not in ["1", "0"]:
            return False
        return True
            #this checks
#verify if it is binary
def option2():
    binary_number = (input("enter a binary number to convert to decimal \n"))
    if is_binary(binary_number) == False:
            print("the numbers you used aint in the binary list")
    elif binary_number == "":
        print("gotta put somethin in there to convert\n")
        option2()
    elif binary_number.isnumeric() != True:
        print("this still wont work out with text, put in a binary number and try again\n")
        option2()
    else:
        converted_decimal = binaryTodecimal(binary_number)
        print(binary_number," in decimal is", converted_decimal)

def binaryTodecimal(n):
    n = int(n)
    #turns numberstring into an integer. this was the source of several hours of troubleshooting oh my god
    decimal = 0
    #starts at 0 because its the number that gets its value accumulated upwards, will be our answer
    power = 1
    #power starts at 1 and will be multiplied later by the next binary digits number
    while n>0:
        #starts the loop that ends calculations once the original number inputed is less than 1
        rem = n%10
        #this extracts and becomes the right most bit
        n = n//10
            #this variables calculation takes or slides the digits over by one removing the next smallest bit in our number
        decimal += rem*power
        #the bit extracted (either one or zero) gets multiplied by power which starts at 1 and increments by values of 2
        power = power*2
        #increments the power variaable for each digit it goes to the left of per while cycle

    return decimal

menu()
option = int(input("select option:  "))

while option !=0:
    if option == 1:
        print("Decimal to Binary selected\n")
        option1()
        #this calls function for option 1 which is decimal to binary
    elif option == 2:
        print("Binary to Decimal selected\n")
        option2()
        #this calls function for option 2 which is binary to decimal
    else:
         print("invalid selection")
         #this will allow the menu to have its selection input
 #"while" being set to "while not equal" to 0 allows for it to skip to the end if 0 condition is met

    menu()
    option = int(input("select option:  "))

print("thanks for using this calculator")
