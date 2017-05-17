def readLetters():
    letters = input(">>> ")
    print()
    lettersList = list(letters)
    for i in range(0, 100, 10):
        for j in range(10):
            print(lettersList[i+j],end="")
        print()


if __name__ == "__main__":
    readLetters()
