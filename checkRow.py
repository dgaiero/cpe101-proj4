from funcs import *

def checkRows(lst, words):
    wordsNotFound = []
    for i in range(10):
        for j in range(len(words)):
            if words[j] in lst[i]:
                xLoc = lst[i].find(words[j])+1
                print("Found word: {}".format(words[j]))
                print("Found at: {},{}".format(xLoc,i+1))
            else:
                wordsNotFound.append(words[j])
                print("{} not found".format(words[j]))
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
