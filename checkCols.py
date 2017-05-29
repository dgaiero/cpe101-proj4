# Project 4 – Word Puzzle
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05

# ========================================================
# Import libraries
# ========================================================
from funcs3 import *

def checkCols(L):
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
For testing purposes. Delete for final rev.
'''
if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    readLetters(puzzleLetters)
    checkCols(puzzleLetters)
