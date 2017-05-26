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


def formatLetters(puzzleLetters):
    mainList = []
    for i in range(0, 100, 10):
        tempString = ''
        for j in range(10):
            tempString += (puzzleLetters[i + j])

        mainList.append(tempString)
    return mainList


'''
Steps:
    Read the letters.
    Print the list into a 10x10 matrix.
'''


def printBoard(puzzleLetters):
    letters = puzzleLetters
    lettersList = list(letters)
    print("Puzzle: \n")
    for i in range(10):
        for j in range(10):
            print(lettersList[i][j], end="")
        print()


def checkLetters(lst, words, direction, reverse):
    wordsFound = []
    wordsList = []
    masterList = []
    for i in range(10):
        for j in range(len(words)):
            if words[j] in lst[i]:
                wordDict = {
                    'word': '',
                    'row': '',
                    'col': '',
                    'dir': '',
                    'reverse': ''
                }
                xLoc = lst[i].find(words[j]) + 1
                yLoc = i + 1
                wordsFound.append(words[j])
                wordDict['word'] = words[j]
                wordDict['row'] = yLoc
                wordDict['col'] = xLoc
                wordDict['dir'] = direction
                wordDict['reverse'] = reverse
                wordsList.append(wordDict)
            else:
                pass
    masterList = [wordsFound, wordsList]
    print(masterList)

def makeRows(lst):
    masterList = []
    for i in range(10):
        newList = []
        for j in range(10):
            newList.append(lst[j][i])
        masterList.append(newList)
    return masterList

'''
For testing purposes. Delete for final rev.
'''
if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    printBoard(puzzleLetters)
    printBoard(makeRows(puzzleLetters))
    checkLetters(puzzleLetters, puzzleWords, 1, 1)
