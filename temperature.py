
def celsius_to_fahr(temp):
    temp = 9/5 * temp + 32
    return ("The Freezing point of water in rahrenheit is: " + str(temp))

def kelvin_to_celcius(temp_kelvins):
    temp = temp_kelvins - 273.15
    return ("The absolute freezing point of water in Celsius is: " + str(temp))

def main():
    freezing_point = celsius_to_fahr (0)
    print (freezing_point)

    temp = 0

    absolute_zero = kelvin_to_celcius(temp)
    print (absolute_zero)

    if __name__ == "__main__":
        main()
