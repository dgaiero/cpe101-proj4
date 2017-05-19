# Project 4 – Word Puzzle
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05


'''
Steps:
    Read the input file
    split the words into a list.
    Add the puzzle words and puzzle letters to a dictionary
    return dictionary
'''


def readFile():
    puzzleLetters = input("")
    puzzleWords = input("")
    print()
    puzzleWords = puzzleWords.split(" ")
    puzzleInformation = {
        'puzzleWords': puzzleWords,
        'puzzleLetters': puzzleLetters
    }
    return puzzleInformation


'''
Steps:
    Read the letters.
    Print the list into a 10x10 matrix.
'''


def readLetters(puzzleLetters):
    letters = puzzleLetters
    lettersList = list(letters)
    print("Puzzle: \n")
    for i in range(0, 100, 10):
        for j in range(10):
            print(lettersList[i + j], end="")
        print()


'''
For testing purposes. Delete for final rev.
'''
if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    readLetters(puzzleLetters)
