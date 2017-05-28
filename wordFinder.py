# Project 4 – Word Puzzle
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05

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
'''

if __name__ == "__main__":
    wordsFound = []
    wordsList = []
    masterList = [wordsFound, wordsList]
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    print(puzzleLetters)
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
    print(masterList)
