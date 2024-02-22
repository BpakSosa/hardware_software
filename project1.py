def intro_msg():
    print("i can reverse a string")
    print("if you give me an 'apple' i will return 'elppa'")
    print("i can even do an entire sentence")
    return input("Type something and see:")

def reverse_word(characters):
    reverse_string = ''
    i = len(characters) - 1
    #len function lets the loop keep subtracting from the string(s internal value? like the amount of characters in it)
    while i >= 0:
        #this waits for thestring to be less than 0 to stop
        reverse_string += characters[i]
        i -= 1
        #these line is responsible for reversing the string by rewriting it by retrieving thestring in order from last character to first
    print('your phrase:{}\nwhen flipped is:{}'.format(characters, reverse_string))
#this line above prints both the original characters and the reversed string afterwards
def main():
    word = intro_msg()
    word = reverse_word(word)
    while True:
        word = input("try again by typing another phrase or type 'quit' to exit\n")
        if word == 'quit':
            print("babai")
            exit()
            #this quits when you type quit
        else:
            reversed_word = reverse_word(word)
            #this calls on the function from ealier to do its reversing and outputting

if __name__ == "__main__":
    main()
