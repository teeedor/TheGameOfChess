
#Move Function

#Board Layout

#1
#2
#3
#4
#5
#6
#7
#8
#   A   B   C   D   E   F   G   H

#Create a class for a piece
    #Vertical Location (1-8)
    #Horizontal Location (A-H)
    #Color (White or Black)
    #Life Boolean (True=alive, False=dead)


#Subclasses
    #Pawn
        #Can Move:
            #Forward 1 space
            #forward two spaces on first move
                #Check for how many moves have been taken
            #Can capture one
    #Bishop
        #Can Move:
            #diagonally any amount
            #Can Capture anywhere it can move
    #Castle
        #Can Move:
            #forward or backward any amount
    #Knight
        #Can move two in one direction and one in the other direction
        #Can Capture any of those Locations
    #Queen
        #Can Move:
            #Combine move sets of the castle and the Bishop
    #King (White 1-E, Black 8-E)
        #Can Move:
            #In any direction one space


#_______________________________________________________________________________
#_______________________________________________________________________________
#Flow of the Program
#Create all the pieces
    #Default Locations


#White goes first
#Player Chooses a piece then a move
#Determine if the move is illegal, Legal, or a Capture
#Repeat until the king of one color dies
#Special Cases
    #Castling
    #When a Pawn Goes to the end of the board
#Keep Score for each Player

class GamePiece:
    #Functions
    #Initializing Function
    def __init__(Vertical,Horizontal,Color):
        self.V = Vertical               #Vertical Location on board
        self.H = Horizontal             #Horizontal Location on board
        self.C = Color                  #Color of piece
        self.L = True                   #Check to see if its alive
        self.moveCount = 0
    #Check Move (implemented in subclass)



class pawn(GamePiece):
    def __init__():
        GamePiece.__init__(Vertical,Horizontal,Color)

    def checkMove(VertIn, HorizIn):
        #Check to see if the input value is valid
        #if White, check if vertIn is larger by 1
        #if Black, check if VertIn is smaller by 1
        #if self.moveCount is 0, then you can move by two spaces if its legal
        #if theres another piece

class castle(GamePiece):
    def __init__():
        GamePiece.__init__(Vertical,Horizontal,Color)
    def checkMove():

class bishop(GamePiece):
    def __init__():
        GamePiece.__init__(Vertical,Horizontal,Color)
    def checkMove():

class knight(GamePiece):
    def __init__():
        GamePiece.__init__(Vertical,Horizontal,Color)
    def checkMove():

class queen(GamePiece):
    def __init__():
        GamePiece.__init__(Vertical,Horizontal,Color)
    def checkMove():

class king(GamePiece):
    def __init__():
        GamePiece.__init__(Vertical,Horizontal,Color)
    def checkMove():
