from PieceClasses import *
VERBOSE = False
def buildBoard():
    #needs to create a 32 element array that contains all pieces for the game
    pieceList=[]
    #add white pawns first 8
    for x in range(1,9):
        newPiece = piece("pawn", "white", x, 2)
        pieceList.append(newPiece)
    #black pawns 8
    for x in range(1,9):
        newPiece = piece("pawn", "black", x, 7)
        pieceList.append(newPiece)
    #white bishops
    newPiece = piece("bishop", "white", 3, 1)
    pieceList.append(newPiece)
    newPiece = piece("bishop", "white", 6, 1)
    pieceList.append(newPiece)
    #black bishops
    newPiece = piece("bishop", "black", 3, 8)
    pieceList.append(newPiece)
    newPiece = piece("bishop", "black", 6, 8)
    pieceList.append(newPiece)
    #white castles
    newPiece = piece("castle", "white", 1, 1)
    pieceList.append(newPiece)
    newPiece = piece("castle", "white", 8, 1)
    pieceList.append(newPiece)
    #black castles
    newPiece = piece("castle", "black", 1, 8)
    pieceList.append(newPiece)
    newPiece = piece("castle", "black", 8, 8)
    pieceList.append(newPiece)
    #white knights
    newPiece = piece("knight", "white", 2, 1)
    pieceList.append(newPiece)
    newPiece = piece("knight", "white", 7, 1)
    pieceList.append(newPiece)
    #black knights
    newPiece = piece("knight", "black", 2, 8)
    pieceList.append(newPiece)
    newPiece = piece("knight", "black", 7, 8)
    pieceList.append(newPiece)
    #kings and queens
    newPiece = piece("king", "white", 5, 1)
    pieceList.append(newPiece)
    newPiece = piece("queen", "white", 4, 1)
    pieceList.append(newPiece)
    newPiece = piece("king", "black", 5, 8)
    pieceList.append(newPiece)
    newPiece = piece("queen", "black", 4, 8)
    pieceList.append(newPiece)

    #for printing out the entire array
    if VERBOSE:
        count = 0
        for x in pieceList:
            count = count +1
            print("COUNT, TYPE,COLOR,X,Y: "+count+x.type+","+x.color+","+str(x.x)+","+str(x.y))

    return pieceList
#this function just read the piecce to return what character to print to the board
def symbolCheck(piece):
    if piece.color=="white":
        result = "w"
    else:
        result = "b"
    if piece.type=="pawn":
        result = result + "p"
    if piece.type=="bishop":
        result = result + "b"
    if piece.type=="castle":
        result = result + "c"
    if piece.type=="knight":
        result = result + "k"
    if piece.type=="queen":
        result = result + "q"
    if piece.type=="king":
        result = result + "M"
    return result
def draw(pieces):
    posx = 1
    posy = 1
    #run through drawiing the board drawing xes where there are no pieces
    for posy in range (1, 9): #y values of board
        xline = ''
        for posx in range(1,9): #x values of board
            #iterate through entire pieccelist to see if there is a piece for this location
            full = False #this will be set to true if a piece is in this spot
            for i in range(0,32):
                #print("This one: "+ str(i))
                if pieces[i].x == posx:
                    if pieces[i].y == posy:
                        #this is the correct pieces for the square
                        #print("posx: "+str(posx))
                        xline= xline+symbolCheck(pieces[i])+" "
                        full = True
            if full == False:
                xline= xline+'  '
        print(xline)
