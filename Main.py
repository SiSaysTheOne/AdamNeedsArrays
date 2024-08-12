# https://medium.com/@gbemiadekoya/importing-python-libraries-in-vs-code-e9e7806586a7
from graphics import *

""" CONSTANTS """
LetterArray = ['a','b','c','d','e','f','g','h']
NumberArray = ['1','2','3','4','5','6','7','8']
unitLength = 100

""" FUNCTIONS """
def tileCombo(i, j):
    return Rectangle(Point(unitLength*i, unitLength*j), Point(unitLength*(i+1), unitLength*(j+1)))
    #return LetterArray[i]+NumberArray[j]

def createTable(numTiles):
    # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    returnList = [[tileCombo(i, j) for i in range(0, numTiles)] for j in range(0, numTiles)]
    print(returnList)
    print(returnList[0][0])
    return returnList

""" MAIN """
def Main():
    numTiles = 10
    createTable(numTiles)
    epicTable = createTable(numTiles)
    win = GraphWin("Chess Board", unitLength*numTiles, unitLength*numTiles)
    # https://www.w3schools.com/python/python_for_loops.asp
    for i in range(0, numTiles):
        for j in range(0, numTiles):
            epicTable[i][j].draw(win)
    while True:
        i = 0

Main()