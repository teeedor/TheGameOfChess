#Turning these sections into functions to write less code for writing the queen function
def isBishopMove(piece, endx, endy):
    for z in range(1,9):
        if (((z+piece.x)==endx) and ((z+piece.y)==endy)) or (((z-piece.x)==endx) and ((z+piece.y)==endy)) or (((z+piece.x)==endx) and ((z-piece.y)==endy)) or (((z-piece.x)==endx) and ((z-piece.y)==endy)):
            piece.queenmove = "bishop"
            return True
    #if we drop out of the loop, then it will never be completed
    return False

def isCastleMove(piece, endx, endy):
    if (piece.y == endy) or (piece.x == endx):
        piece.queenmove = "castle"
        return True
    else:
        return False


#def bishopCollision(board, piece, endx, endy):

#def castleCollision(board, piece, endx, endy):

#NEED TO WORK ON
def isInTheWay(board, piece, endx, endy):
#in the way is on the location or in the way
    type = piece.type
    if type ==("bishop") or ("castle") or ("queen"):
        #check the path
        if (piece.x-endx==0) or (piece.y-endy==0): #castle style movement
            if (piece.x-endx==0):
                #Make sure the range on this for loop is correct
                #for z in range(piece.x, endx):
                    #if
                return True #placeholder
            else:
                return False
        #bishop Style Movement
        #if ()
    for p in board: #check final Location for all pieces
        if (p.x == endx) and (p.y == endy):
            if piece.color == p.color:
                return True #piece is in the way
            else:
                return False #allow capture


#NOT TESTED
def isInMoveSet(piece, capture, endx, endy):
    #checks to see what color the piece is to allow for both color pawns to work
    if (piece.color == "white"):
        yNegSwitch = 1
    else:
        yNegSwitch = -1
    #pawn - Not Tested But Completed
    if piece.type =="pawn":
        #check for white and black pawns
        #white
        if (
            ((endx == piece.x) and (endy == piece.y+(1*yNegSwitch))) or
            ((piece.movecount==0) and (endx == piece.x) and (endy == piece.y+(2*yNegSwitch))) or
            (capture and (endy == piece.y+(1*yNegSwitch)) and ((endx == piece.x-1)or(endx == piece.x+1)))
            ):
            if isInTheWay(board, piece, endx, endy):
                return False
            else:
                return True
        else:
            return False

    #bishop - Not Tested But Completed
    if piece.type =="bishop":
        #need to take account of the 4 different move directions
            if isBishopMove(piece, endx, endy):
                if isInTheWay(board, piece, endx ,endy):
                    return False
                else:
                    return True
            else:
                False

    #castle - Not Tested But Completed
    if piece.type == "castle":
        if isCastleMove(piece, endx, endy):
            #as long as the y value doesn't change
            if isInTheWay(board, piece, endx, endy):
                return False
            else:
                return True
        else:
            return False
    #knight - Not Tested But Completed
    if piece.type == "knight":
        if (
            ((piece.x+1==endx) and (piece.y+2==endy)) or
            ((piece.x+2==endx) and (piece.y+1==endy)) or
            ((piece.x+2==endx) and (piece.y-1==endy)) or
            ((piece.x+1==endx) and (piece.y-2==endy)) or
            ((piece.x-1==endx) and (piece.y-2==endy)) or
            ((piece.x-2==endx) and (piece.y-1==endy)) or
            ((piece.x-2==endx) and (piece.y+1==endy)) or
            ((piece.x-1==endx) and (piece.y+2==endy))
            ):
            if isInThWay(board, piece, endx, endy):
                return False
            else:
                return True
        else:
            return False
    #queen - Not Tested But Completed
    if piece.type == "queen":
        if isBishopMove(piece, endx, endy) or isCastleMove(piece, endx, endy):
            if isInThWay(board, piece, endx, endy):
                return False
            else:
                return True
        else:
            return False
    #king - Not Tested But Completed
    if piece.type == "king":
        if (
            (piece.x+1==endx) or (piece.x-1==endx) or
            (piece.y+1==endy) or (piece.y-1==endy) or
            ((piece.y+1==endy) and (piece.x+1==endx)) or
            ((piece.y-1==endy) and (piece.x+1==endx)) or
            ((piece.y-1==endy) and (piece.x-1==endx)) or
            ((piece.y+1==endy) and (piece.x-1==endx))
            ):
            if isIntTheWay(board, piece, endx, endy):
                return False
            else:
                return True
        else:
            return False

#NEED TO WORK ON
def isCapturing():
    return False

#Not Tested
def areBothKingsAlive(board):
    white = False
    black = False
    for p in board:
        if (p.type == "king") and (p.color == "white"):
            white = True
        if (p.type == "king") and (p.color == "black"):
            white = True
    if (white and black):
        return True
    else:
        return False

#Not Completed
def testMove(board, piece, endx, endy, testno):
    if isGoodMove(board, piece, endx, endy):
        carl = 7
    else:
        print("Piece won't move: "+piece.type+str(testno))
        print("from "+str(piece.x)+', '+str(piece.y)+' to '+str(endx)+', '+str(endy))
#highest level check
def isGoodMove(board, piece, endx, endy):
        capture = False
        #if new location is on the board
        if (endx<1) or (endy<1) or (endx>8) or (endy>8):
            print("Invalid move, out of bounds")
            return False
        #if move is in moveset
        if not isInMoveSet(piece, capture, endx, endy):
            print("Invalid Move, not in moveset")
            return False
        #if new location already has team piece (or there is a piece in the way)(isInTheWay)
        if isInTheWay(board, piece, endx, endy):
            print("Invalid move, Team Piece in the way")
            return False
        #if move is capturing, this is mostly for pawns
        capture = isCapturing(board, piece, endx, endy)
