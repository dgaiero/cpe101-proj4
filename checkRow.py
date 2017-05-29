# Project 4 – Word Puzzle
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05

# ========================================================
# Import libraries
# ========================================================
from funcs import *

def checkRows(lst, words):
    wordsFound = []
    for i in range(10):
        for j in range(len(words)):
            if words[j] in lst[i]:
                xLoc = lst[i].find(words[j])+1
                wordsFound.append(words[j])
                print("Found word: {}".format(words[j]))
                print("Found at: {},{}".format(xLoc,i+1))
            else:
                pass

'''
For testing purposes. Delete for final rev.
'''
if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    readLetters(puzzleLetters)
    checkRows(puzzleLetters, puzzleWords)
