import translate as t




if __name__ == "__main__":

    word = input("Enter word: ")
    if type(t.translate(word)) == list:
        for i in t.translate(word):
            print(i)
    else:
        print(t.translate(word))
