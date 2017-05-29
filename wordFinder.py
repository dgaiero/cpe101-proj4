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

'''
Import libraries
'''
from funcs import *

'''
Step:
    1. Iterate through the origional words
    2. Iterate through the words found
    3. If the origional word is in the list of words found, then print the information
    4. If it is not in the found list, then print that the word was not found.
Function completed by:
'''


def printOutput(puzzleWords, masterList):
    for i in range(len(puzzleWords)):
        for j in range(len(masterList[0])):
            if puzzleWords[i] in masterList[1][j]["word"]:
                if masterList[1][j]["dir"] == 1 and masterList[1][j]["reverse"] == 0:
                    print("{0}: (FORWARD) row: {1} column: {2}".format(
                        masterList[1][j]['word'], masterList[1][j]['row'], masterList[1][j]['col']))
                elif masterList[1][j]["dir"] == 1 and masterList[1][j]["reverse"] == 1:
                    print("{0}: (BACKWARD) row: {1} column: {2}".format(
                        masterList[1][j]['word'], masterList[1][j]['row'], masterList[1][j]['col']))
                elif masterList[1][j]["dir"] == 2 and masterList[1][j]["reverse"] == 0:
                    print("{0}: (DOWN) row: {1} column: {2}".format(
                        masterList[1][j]['word'], masterList[1][j]['row'], masterList[1][j]['col']))
                elif masterList[1][j]["dir"] == 2 and masterList[1][j]["reverse"] == 1:
                    print("{0}: (UP) row: {1} column: {2}".format(
                        masterList[1][j]['word'], masterList[1][j]['row'], masterList[1][j]['col']))
            elif puzzleWords[i] not in masterList[0]:
                print("{0}: word not found".format(puzzleWords[i]))
                break


'''
Declare wordsFound, wordsList, and the masterList.
Run readFile to request user input on the puzzle parameters
Declare puzzleWords and puzzleLetters from the output dictionary of readFile
Format the puzzle letters in formatLetters.
Reverse the words through reverseWords
Format the list of letters through makeRows
Run through masterList for:
    1. Horiz and normal
    2. Horiz and reverse
    3. Vert and normal
    4. Vert and reverse
Function completed by:
'''


def main():
    wordsFound = []
    wordsList = []
    masterList = [wordsFound, wordsList]
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    puzzleLettersRow = makeRows(puzzleLetters)
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
    printOutput(puzzleWords, masterList)


'''
Run main Function
'''
if __name__ == "__main__":
    main()
