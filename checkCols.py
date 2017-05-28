from funcs import *

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
    
if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    readLetters(puzzleLetters)
    checkCols(puzzleLetters)
