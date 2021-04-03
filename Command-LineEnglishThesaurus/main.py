import translate as t

if __name__ == "__main__":
    while(input("Would you like to continue?  Enter Y if yes, or press anything to endy: ").lower() == "y"):
        word = input("Enter word: ")
        if type(t.translate(word)) == list:
            for i in t.translate(word):
                print(i)
        else:
            print(t.translate(word))
