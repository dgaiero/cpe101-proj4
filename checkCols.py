from funcs import *

def checkCols(L):
    tempL = []
    print (tempL.append(L[0][0]))
    print (tempL.append(L[1][0]))
    for i in range(10):
        tempString = ''
        tempString += L[i] #       tempL.append(x)
    print (tempL)
    '''
    newL.append(newCol0 = [WCALPOLYXU])
    newL.append(newCol1 = [ABZDOEGCVU])
    newL.append(newCol2 = [QMXWNDQSDI])
    newL.append(newCol3 = [HIWLDSCLMU])
    newL.append(newCol4 = [GVKFTOKOGN])
    newL.append(newCol5 = [TQWXMYGASI])
    newL.append(newCol6 = [TQIPVQMCXX])
    newL.append(newCol7 = [WEIIAGMVCF])
    newL.append(newCol8 = [ELIPMOCZYN])
    newL.append(newCol9 = [ESLUNBTMZU])
    print (newL)
    return newL
    '''

if __name__ == "__main__":
    fileInfo = readFile()
    puzzleWords = fileInfo['puzzleWords']
    puzzleLetters = fileInfo['puzzleLetters']
    puzzleLetters = formatLetters(puzzleLetters)
    readLetters(puzzleLetters)
    checkCols(puzzleLetters)
