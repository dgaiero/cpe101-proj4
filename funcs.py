# Project 4 – Word Puzzle
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05
# https://github.com/dgaiero/cpe101-proj4

 #     #                         ######
 #  #  #  ####  #####  #####     #     # #    # ###### ###### #      ######
 #  #  # #    # #    # #    #    #     # #    #     #      #  #      #
 #  #  # #    # #    # #    #    ######  #    #    #      #   #      #####
 #  #  # #    # #####  #    #    #       #    #   #      #    #      #
 #  #  # #    # #   #  #    #    #       #    #  #      #     #      #
  ## ##   ####  #    # #####     #        ####  ###### ###### ###### ######

 #######
 #       #    # #    #  ####  ##### #  ####  #    #  ####
 #       #    # ##   # #    #   #   # #    # ##   # #
 #####   #    # # #  # #        #   # #    # # #  #  ####
 #       #    # #  # # #        #   # #    # #  # #      #
 #       #    # #   ## #    #   #   # #    # #   ## #    #
 #        ####  #    #  ####    #   #  ####  #    #  ####


'''
Steps:
    Read the input file
    split the words into a list.
    Add the puzzle words and puzzle letters to a dictionary
    return dictionary with the puzzle information
Function completed by: Dominic Gaiero
'''


def readFile():
    puzzleLetters = input("")
    puzzleWords = input("")
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
Function completed by: Dominic Gaiero
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
Function completed by: Dominic Gaiero
'''


def printBoard(puzzleLetters):
    letters = puzzleLetters
    lettersList = list(letters)
    print("Puzzle:\n")
    for i in range(10):
        for j in range(10):
            print(lettersList[i][j], end="")
        print()
    print()

'''
Steps:
    Take input list
    Iterate through input list and create a temporary string
    Take the same index of each item in the list and add to temporary string
    Append each temporary string to the list
    Return the list
Function completed by: Russell Caletena
'''


def makeRows(L):
    i = 0
    tempL = []
    while i in range(len(L)):
        tempString = ''
        for item in L:
            tempString+=item[i]
        tempL.append (''.join(tempString))
        i += 1
    return tempL


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
Function completed by: Dominic Gaiero and Russell Caletena
'''


def checkLetters(lst, words, direction, reverse, masterList):
    wordsFound = masterList[0]
    wordsList = masterList[1]
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
                    if reverse == 0:
                        col = lst[i].find(words[j])
                        row = i
                    else:
                        col = lst[i].find(words[j]) + len(words[j]) -1
                        row = i
                else:
                    if reverse == 0:
                        row = lst[i].find(words[j])
                        col = i
                    else:
                        row = lst[i].find(words[j]) + len(words[j]) -1
                        col = i

                if reverse == 0:
                    wordsFound.append(words[j])
                    wordDict['word'] = words[j]
                else:
                    wordsFound.append(words[j][::-1])
                    wordDict['word'] = words[j][::-1]

                wordDict['row'] = row
                wordDict['col'] = col
                wordDict['dir'] = direction
                wordDict['reverse'] = reverse
                wordsList.append(wordDict)
            else:
                pass
    masterList = [wordsFound, wordsList]
    return masterList


'''
Steps:
    Take input string.
    Slice the string (whole thing and step by -1)
    Return reverse words
Function completed by: Dominic Gaiero
'''

def reverseWords(words):
    reverseWords = []
    for i in range(len(words)):
        reverseWords.append(words[i][::-1])
    return reverseWords
