#NOT TESTED
def isNotInMoveSet(piece, capture, endx, endy):
    #return true means the move is not allowed
    #pawn
    if piece.type =="pawn":
        #check for white and black pawns
        #white
        if (endx == piece.x) and (endy == piece.y+1)
            return False
        if (piece.movecount==0) and (endx == piece.x) and (endy == piece.y+2):
            return False
        if capture and (endy == piece.y+1) and ((endx == piece.x-1)or(endx == piece.x+1)):
            return False
    #bishop
    #castle
    #knight
    #queen
    #king


def isInTheWay(board, piece, endx, endy):


def isCapturing():

def isGoodMove(board, piece, endx, endy):
        capture = False
        #if new location is on the board
        if (endx<1) or (endy<1) or (endx>8) or (endy>8):
            print("Invalid move, out of bounds")
            return False
        #if new location already has team piece (or there is a piece in the way)(isInTheWay)
        if isInTheWay(board, piece, endx, endy):
            print("Invalid move, Team Piece in the way")
            return False
        #if move is capturing, this is mostly for pawns
        capture = isCapturing(board, piece, endx, endy)
        #if move is in moveset
        if isNotInMoveSet(piece, capture, endx, endy):
            print("Invalid Move, not in moveset")
            return False
