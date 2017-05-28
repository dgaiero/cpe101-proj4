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
    return dictionary with the puzzle information
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
    Required args: input string
    breaks string into groups of ten
    returns a list with ten items.
'''


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


'''
Steps:
    Required args:
        1. list of letters
        2. list of words
        3. direction [horiz(1) or vertical(2)]
        4. if the words are in reverse(1) or not(0).
    Checks if words are in the list.
    Returns a list with two items
        1. Words Found
        2. List with dictionaries of all required information.
'''


def checkLetters(lst, words, direction, reverse, masterList):
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
                if direction == 1:
                    xLoc = lst[i].find(words[j])
                    yLoc = i
                else:
                    xLoc = lst[i].find(words[j]) + 1
                    yLoc = i + 1
                if reverse == 0:
                    wordsFound.append(words[j])
                    wordDict['word'] = words[j]
                else:
                    wordsFound.append(words[j][::-1])
                    wordDict['word'] = words[j][::-1]

                wordDict['row'] = yLoc
                wordDict['col'] = xLoc
                wordDict['dir'] = direction
                wordDict['reverse'] = reverse
                wordsList.append(wordDict)
            else:
                pass
    masterList = [wordsFound, wordsList]
    return masterList

def reverseWords(words):
    reverseWords = []
    for i in range(len(words)):
        reverseWords.append(words[i][::-1])
    return reverseWords


'''
For testing purposes. Delete for final rev.

Declare wordsFound, wordsList, and the masterList.
Run readFile to request user input on the puzzle parameters
Declare puzzleWords and puzzleLetters from the output dictionary of readFile
Format the puzzle letters in formatLetters.
Reverse the words through reverseWords
Format the list of letters through makeRows
Run through masterList for:
    1. Horiz and normal
    2. Horix and reverse
    3. Vert and normal
    4. Vert and reverse

'''
if __name__ == "__main__":
    wordsFound = []
    wordsList = []
    masterList = []
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    puzzleLettersRow = makeRows(puzzleLetters)
    print(puzzleLettersRow)
    printBoard(puzzleLetters)
    puzzleWordsReversed = reverseWords(puzzleWords)
    # Horiz and normal
    masterList = checkLetters(puzzleLetters, puzzleWords, 1, 0, masterList)
    # Horiz and reverse
    masterList = checkLetters(
        puzzleLetters, puzzleWordsReversed, 1, 1, masterList)
    # Vert and normal
    masterList = checkLetters(puzzleLettersRow, puzzleWords, 2, 0, masterList)
    # Vert and reverse
    masterList = checkLetters(
        puzzleLettersRow, puzzleWordsReversed, 2, 1, masterList)
    print(masterList)
