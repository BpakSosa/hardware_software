def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input().lower().strip()
    if answer == "yes":
        print("sweet, keep goin at it")
    elif answer == "no":
        print("hope ya change yer mind")
    else:
        print("huh")
    print("cya")
def main():
    print("hey, welcome to this convo program")
    conversation()
    print("thanks for chattin with me")

if __name__ == "__main__":
    main()
