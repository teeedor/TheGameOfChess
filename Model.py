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
#DONE NOT TESTED
def testMove(board, piece, endx, endy, testno):
    if isGoodMove(board, piece, endx, endy):
        print("Good Move")
    else:
        print("Piece won't move: "+piece.type+str(testno))
        print("from "+str(piece.x)+', '+str(piece.y)+' to '+str(endx)+', '+str(endy))
#DONE NOT TESTED
def updateBoard(board, movepiece, endx, endy, capture, prisonerList):
    #At this point, the move should be legal,
    #this function does not check, it just updates
    #search the board for the specific piece based on first location
    if capture:
        for piece in board:
            if(piece.x == endx) and (piece.y == endy):
                #remove the captured piece from the board
                board.remove(piece)
    for piece in board:
        if (piece.x == movepiece.x) and (piece.y == movepiece.y):
            piece.x = endx
            piece.y = endy
            piece.movecount += 1
            return board
        else:
            print("Cannot find piece to move")
#FINISH CASTLE STYLE MOVEMENT
def maybeInTheWay(board, piece, endx, endy):
#return 1 = good move, nothing in the way
#return 2 = capturing piece
#return 3 = team piece in the way
    type = piece.type
    xfactor = 1
    yfactor = 1

    #check the path
    if type ==("bishop") or ("castle") or ("queen"):
        deltax = endx - piece.x
        deltay = endy - piece.y
        #castle Style movement
        if(deltax == 0 and deltay != 0) or (deltax != 0 and deltay == 0):
            pass
        #bishop style movement
        if deltax < 0:
            xfactor = -1
        if deltay < 0:
            yfactor = -1
        iterx = piece.x
        itery = piece.y
        #check the correct diagonal from starting pos
        for i in range(0, abs(deltax)):
            #not checking the last location, next part of function does that
            if (iterx == endx) and (itery == endy):
                break
            else:
                #check to see if there is a piece in the between location
                for p in board:
                    if(p.x == iterx) and (p.y == itery):
                        return 4
                    else:
                        iterx = iterx + (xfactor*1)
                        itery = itery + (yfactor*1)


    #check final Location for all pieces
    for p in board:
        if (p.x == endx) and (p.y == endy):
            if piece.color == p.color:
                #team piece is in the way
                return 3
            else:
                #capturing opposing team piece
                return 2
#DONE TESTED!
def isBishopMove(piece, endx, endy):
    absdx = abs(endx-piece.x)
    absdy = abs(endy-piece.y)
    if absdx is absdy:
        return True
    #if we drop out of the loop, then it will never be completed
    return False
#DONE TESTED!
def isCastleMove(piece, endx, endy):
    if (piece.y == endy) or (piece.x == endx):
        return True
    else:
        return False
#DONE TESTED!
def isInMoveSet(piece, capture, endx, endy):
    #checks to see what color the piece is to allow for both color pawns to work
    if (piece.color == "white"):
        yNegSwitch = 1
    else:
        yNegSwitch = -1
    #pawn - Not Tested But Completed
    if piece.type =="pawn":
        if (
            ((endx == piece.x) and (endy == piece.y+(1*yNegSwitch))) or
            ((piece.movecount==0) and (endx == piece.x) and (endy == piece.y+(2*yNegSwitch))) or
            (capture and (endy == piece.y+(1*yNegSwitch)) and ((endx == piece.x-1)or(endx == piece.x+1)))
            ):
            return True
        else:
            return False

    #bishop - Not Tested But Completed
    if piece.type =="bishop":
        #need to take account of the 4 different move directions
            if isBishopMove(piece, endx, endy):
                return True
            else:
                return False

    #castle - Not Tested But Completed
    if piece.type == "castle":
        if isCastleMove(piece, endx, endy):
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
            return True
        else:
            return False
    #queen - Not Tested But Completed
    if piece.type == "queen":
        if isBishopMove(piece, endx, endy) or isCastleMove(piece, endx, endy):
            return True
        else:
            return False
    #king - Not Tested But Completed
    if piece.type == "king":
        if (
            ((piece.x+1==endx) and (piece.y==endy)) or
            ((piece.x-1==endx) and (piece.y==endy)) or
            ((piece.x==endx) and (piece.y+1==endy)) or
            ((piece.x==endx) and (piece.y-1==endy)) or
            ((piece.y+1==endy) and (piece.y-1==endy)) or
            ((piece.y+1==endy) and (piece.x+1==endx)) or
            ((piece.y-1==endy) and (piece.x+1==endx)) or
            ((piece.y-1==endy) and (piece.x-1==endx)) or
            ((piece.y+1==endy) and (piece.x-1==endx))
            ):
            return True
        else:
            return False
#MIGHT ONLY NEED THIS FOR PAWN MOVESET
def isCapturing():
    pass
#DONE NOT TESTED
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
#DONE TESTED!
def isOnBoard(endx, endy):
    if (endx<1) or (endy<1) or (endx>8) or (endy>8):
        print("Invalid move, out of bounds")
        return False
    else:
        return True
#DONE NOT TESTED
def maybeGoodMove(board, piece, endx, endy):
        capture = False
        #if new location is on the board
        if not isOnBoard(endx, endy):
            return False
        #if move is in moveset
        if not isInMoveSet(piece, capture, endx, endy):
            print("Invalid Move, not in moveset")
            return False
        #if new location already has team piece (or there is a piece in the way)(isInTheWay)
        ms = maybeInTheWay(board, piece, endx, endy)
        if ms == 1: #nothing in the way
            return 1
        if ms == 2: #capturing the opposite teams piece
            capture = 2
        if ms == 3: #same team piece in the way
            return 3
        if ms == 4: #Opposing team piece in path
            return 4
#move() will check to see if the move is valid, then update the board with the new piece positions
def move(board, piece, endx, endy):
    moveOption = maybeGoodMove(board, piece, endx, endy)
    #1: nothing in the way
    if moveOption == 1:
        updateBoard()
    #2: capturing
    #3: same team piece in way
    #4: oppossing team piece in the way
    #update board to reflect new move
    pass
