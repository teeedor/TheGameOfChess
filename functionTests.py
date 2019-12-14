#this file contains tests for all the numerous functions in the functions file
#Structure of functions file
# move()
#     isGoodMove()
#         isInMoveSet()
#             isBishopMove()
#             isCastleMove()
#         maybeInTheWay()
#
#     updateBoard()
#         addPrisoner()
#
# areBothKingsAlive()
from functions import *
from PieceClasses import *

#TESTING FUNCTIONS-----------------------------------------------
# The display test function takes in tests that have been generated
#   by the respective test generator and displays the results
def displaytest(piece, testx, testy):
    stx =str(piece.x)
    sty =str(piece.y)
    sttx =str(testx)
    stty =str(testy)
    type =piece.type
    capture=False

    print(type+": FROM "+stx+", "+sty+" TO "+sttx+", "+stty)
    #Test if the move is Legal Here
    if(isInMoveSet(piece, capture, testx, testy)):
        print("Success")
    else:
        print("Failed")
    print("")
#The gen functions create moves to test every aspect of piece movement
def genPawn(p):
    pass
def genBishop(p):
    print("Testing "+p.type+": Success")
    z = 1
    while z < 8:
        #+x+y
        xfactor = yfactor = 1
        displaytest(p, p.x+(z*xfactor), p.y+(z*yfactor))
        #-x+y
        xfactor = -1
        displaytest(p, p.x+(z*xfactor), p.y+(z*yfactor))
        #+x-y
        xfactor = 1
        yfactor = -1
        displaytest(p, p.x+(z*xfactor), p.y+(z*yfactor))
        #-x-y
        xfactor = yfactor = -1
        displaytest(p, p.x+(z*xfactor), p.y+(z*yfactor))
        z += 1
    #make Failures for testing
    print("Testing "+p.type+": Failures")
def genCastle(p):
    print("Testing "+p.type+": Success")
    z=1
    while z < 8:
        displaytest(p, p.x+z, p.y)
        displaytest(p, p.x-z, p.y)
        displaytest(p, p.x, p.y+z)
        displaytest(p, p.x, p.y-z)
        z +=1
    print("Testing "+p.type+": Failures")
    displaytest(p, p.x+1, p.y+1)
def genKnight(p):
    pass
def genQueen(p):
    pass
def genKing(p):
    pass

#genTest collects all above gen functions into one switch case
# use a switch case based on the type of the input piece
#   to know what tests to generate
def genTest(p):
    type = p.type
    #Begin Switch Case
    switcher = {
        "pawn": genPawn,
        "bishop": genBishop,
        "castle": genCastle,
        "knight": genKnight,
        "queen": genQueen,
        "king": genKing
    }
    generatorFunc = switcher.get(type, "Invalid Piece Type")
    generatorFunc(p)
#This function displays the test info in a readable format
def displaytestisOnBoard(testx, testy):
    sttx =str(testx)
    stty =str(testy)
    print(sttx+", "+stty)
    if(isOnBoard(testx, testy)):
        print("Success")
    else:
        print("Failed")
    print("")
#Generate tests for checking withing board bounds
def testisOnBoard():
    print("Testing isOnBoard()")
    displaytestisOnBoard(1,1)
    displaytestisOnBoard(4,4)
    displaytestisOnBoard(8,8)
    displaytestisOnBoard(9,9)
    displaytestisOnBoard(-1,-1)
    displaytestisOnBoard(1,-1)
    displaytestisOnBoard(-1,1)


# - RUNNING TESTS -
p = piece("bishop", "white", 4, 4)
#genTest(p)
r = piece("castle", "white", 4, 4)
genTest(r)
testisOnBoard()
