#this file contains tests for all the numerous functions in the functions file
#Structure of functions file
# move()
#     isGoodMove()
#         isOnBoard()*
#         isInMoveSet()*
#             isBishopMove()*
#             isCastleMove()*
#         maybeInTheWay()
#
#     updateBoard()
#         addPrisoner()
#
# areBothKingsAlive()
from Model import *
from PieceClasses import *

#TESTING FUNCTIONS-----------------------------------------------
# The display test function takes in tests that have been generated
#   by the respective test generator and displays the results
def displaytest(piece, capture, testx, testy):
    stx =str(piece.x)
    sty =str(piece.y)
    sttx =str(testx)
    stty =str(testy)
    type =piece.type

    print(type+": FROM "+stx+", "+sty+" TO "+sttx+", "+stty)
    #Test if the move is Legal Here
    if(isInMoveSet(piece, capture, testx, testy)):
        print("Success")
    else:
        print("Failed")
    print("")
#All Basic Movement works
#DONE
def genPawn(p):
    capture=False
    #Get color of piece for negative movement
    if (p.color == "white"):
        yNegSwitch = 1
    else:
        yNegSwitch = -1
    #basic one space movement
    print("Testing "+p.color+" "+p.type+": Success")
    displaytest(p,capture,p.x, p.y+(1*yNegSwitch))
    #capturing movement
    print("Testing "+p.color+" "+p.type+" Capture: Success")
    capture=True
    displaytest(p,capture,p.x+1, p.y+(1*yNegSwitch))
    displaytest(p,capture,p.x-1, p.y+(1*yNegSwitch))

    capture=False
    print("Testing "+p.type+": Failures")
    displaytest(p,capture,p.x, p.y-(1*yNegSwitch))
    displaytest(p,capture,p.x, p.y)
#DONE
def genBishop(p):
    capture=False
    print("Testing "+p.type+": Success")
    z = 1
    while z < 8:
        #+x+y
        xfactor = yfactor = 1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        #-x+y
        xfactor = -1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        #+x-y
        xfactor = 1
        yfactor = -1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        #-x-y
        xfactor = yfactor = -1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        z += 1
    #make Failures for testing
    print("Testing "+p.type+": Failures")
    displaytest(p,capture,p.x, p.y)
#DONE
def genCastle(p):
    capture=False
    print("Testing "+p.type+": Success")
    z=1
    while z < 8:
        displaytest(p,capture, p.x+z, p.y)
        displaytest(p,capture, p.x-z, p.y)
        displaytest(p,capture, p.x, p.y+z)
        displaytest(p,capture, p.x, p.y-z)
        z +=1
    print("Testing "+p.type+": Failures")
    displaytest(p,capture, p.x+1, p.y+1)
    displaytest(p,capture,p.x, p.y)
#DONE
def genKnight(p):
    capture=False
    print("Testing "+p.type+": Success")
    displaytest(p, capture, p.x+1, p.y+2)
    displaytest(p, capture, p.x+2, p.y+1)
    displaytest(p, capture, p.x-1, p.y+2)
    displaytest(p, capture, p.x+2, p.y-1)
    displaytest(p, capture, p.x+1, p.y-2)
    displaytest(p, capture, p.x-2, p.y+1)
    displaytest(p, capture, p.x-1, p.y-2)
    displaytest(p, capture, p.x-2, p.y-1)
    print("Testing "+p.type+": Failures")
    displaytest(p, capture, p.x-3, p.y-1)
    displaytest(p, capture, p.x, p.y-1)
    displaytest(p, capture, p.x-2, p.y)
    displaytest(p,capture,p.x, p.y)
#DONE
def genQueen(p):
    capture=False
    print("Testing "+p.type+": Success")
    #Bishop Movement
    z = 1
    while z < 8:
        #+x+y
        xfactor = yfactor = 1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        #-x+y
        xfactor = -1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        #+x-y
        xfactor = 1
        yfactor = -1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        #-x-y
        xfactor = yfactor = -1
        displaytest(p,capture,p.x+(z*xfactor), p.y+(z*yfactor))
        z += 1
    #Castle Movement
    z=1
    while z < 8:
        displaytest(p,capture, p.x+z, p.y)
        displaytest(p,capture, p.x-z, p.y)
        displaytest(p,capture, p.x, p.y+z)
        displaytest(p,capture, p.x, p.y-z)
        z +=1
    print("Testing "+p.type+": Failures")
    displaytest(p,capture, p.x+2, p.y+1)
    displaytest(p,capture, p.x+2, p.y-1)
    displaytest(p,capture,p.x, p.y)
#DONE
def genKing(p):
    capture=False
    print("Testing "+p.type+": Success")
    displaytest(p,capture,p.x+1, p.y)
    displaytest(p,capture,p.x-1, p.y)
    displaytest(p,capture,p.x, p.y+1)
    displaytest(p,capture,p.x, p.y-1)
    displaytest(p,capture,p.x+1, p.y+1)
    displaytest(p,capture,p.x-1, p.y+1)
    displaytest(p,capture,p.x-1, p.y-1)
    displaytest(p,capture,p.x+1, p.y-1)

    print("Testing "+p.type+": Failures")
    displaytest(p,capture,p.x, p.y)
    displaytest(p,capture,p.x+2, p.y+1)
    displaytest(p,capture,p.x-2, p.y+1)

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

#-------------------------------------------------------------
#between Tests
def betweendisplaytest(board, piece, testx, testy):
    stx =str(piece.x)
    sty =str(piece.y)
    sttx =str(testx)
    stty =str(testy)
    type =piece.type

    print(type+": FROM "+stx+", "+sty+" TO "+sttx+", "+stty)
    #Test if the move is Legal Here
    value = maybeInTheWay(board, piece, testx, testy)
    if(value ==1):
        print("1: Nothing in the way")
    elif(value ==2):
        print("2: Capturing piece, opposite color piece in ending location")
    elif(value ==3):
        print("3: Failed, team piece in ending location")
    elif(value ==4):
        print("4: Failed, Piece in between starting and ending location")
    print("")

def betweenGenBishop(board, p):
    print("Testing "+p.color+" "+p.type+" between test: 1")
    betweendisplaytest(board, p, 3, 5)
    print("Testing "+p.color+" "+p.type+" between test: 2")
    betweendisplaytest(board, p, 5, 3)
    print("Testing "+p.color+" "+p.type+" between test: 3")
    betweendisplaytest(board, p, 1, 7)
    print("Testing "+p.color+" "+p.type+" between test: 4")
    betweendisplaytest(board, p, 7, 7)
    betweendisplaytest(board, p, 6, 2)



def betweenGenCastle(board, p):
    pass
def betweenGenQueen(board, p):
    pass
#betweenGenTest takes in a board congfiguration and a piece and creates between
#   tests for the type of piece that it is
def betweenGenTest(board, p):
    type = p.type
    #Begin Switch Case
    switcher = {
        "bishop": betweenGenBishop,
        "castle": betweenGenCastle,
        "queen": betweenGenQueen
    }
    generatorFunc = switcher.get(type, "Invalid Piece Type")
    generatorFunc(board, p)

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
#testisOnBoard()


#genTest(b)
c = piece("castle", "white", 4, 4)
#genTest(c)
p = piece("pawn", "black", 2, 6)
#genTest(p)
n = piece("knight", "white", 5, 4)
#genTest(n)
q = piece("queen", "black", 5, 4)
#genTest(q)
k = piece("king", "white", 3,3)
#genTest(k)

#board for testing
b = piece("bishop", "white", 4, 4)
p1 = piece("pawn", "black", 3,3)
p2 = piece("pawn", "black", 5,3)
p3 = piece("pawn", "black", 6,6)
p4 = piece("pawn", "white", 1,7)
bd =[p1,p2,p3,p4]
betweenGenTest(bd, b)
