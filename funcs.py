def readFile():
    puzzleLetters = input("")
    puzzleWords = input("")
    print()
    puzzleWords = puzzleWords.split(" ")
    puzzleInformation = {
        'puzzleWords' : puzzleWords,
        'puzzleLetters' : puzzleLetters
    }
    return puzzleInformation


def readLetters(puzzleLetters):
    letters = puzzleLetters
    lettersList = list(letters)
    print("Puzzle: \n")
    for i in range(0, 100, 10):
        for j in range(10):
            print(lettersList[i+j],end="")
        print()


'''
For testing purposes. Delete for final rev.
'''
if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    readLetters(puzzleLetters)
