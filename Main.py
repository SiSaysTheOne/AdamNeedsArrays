from graphics import *

LetterArray = ['a','b','c','d','e','f','g','h']
NumberArray = ['1','2','3','4','5','6','7','8']

def tileCombo(i, j):
    unitLength = 100
    return Rectangle(Point(unitLength*i, unitLength*j), Point(unitLength*(i+1), unitLength*(j+1)))
    #return LetterArray[i]+NumberArray[j]

def createTable(numTiles):
    returnList = [[tileCombo(i, j) for i in range(0, numTiles)] for j in range(0, numTiles)]
    print(returnList)
    print(returnList[0][0])
    return returnList

def Main():
    numTiles = 10
    createTable(numTiles)
    epicTable = createTable(numTiles)
    win = GraphWin("Chess Board", 800, 800)
    for i in range(0, numTiles):
        for j in range(0, numTiles):
            epicTable[i][j].draw(win)
    while True:
        i = 0


Main()