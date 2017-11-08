#This File will run the Game Logic
#Chess Visualization will Draw the board and take care of the visualizations
import PieceClasses.py

#_______________________________________________________________________________
#Checking Variables
player1 = 'W'                       #Variables to check against later in the code
player2 = 'B'
currentPlayerColor = player1                      #White always goes first

################################################################################
#Create the list of pieces
    #Initializing the list will be the same for every game
#Im going to try one list and fix it later if i have to
#Call the visualization function For First Time

#PLAYER TURN
#loop until one of the kings dies
    #Check the currentPlayerColor
        #Take in a piece they want to move
        #Check to see if piece is alive
        #take in the place where they want to move it
        #Check to see if the move is legal with built in CheckMove Function
        #if it is a legal move, Check to see if there is
            #Same color piece in location
            #A piece in the way of the move ment (Not applicable for Knight)
                #If there is a piece of opposite color in the way, say that the move is illegal
            #Or an opposing piece in the location

        #If the Move is legal
            #Update the location of the moving piece and increment the score
            #Update Life Boolean of captured piece
            #Update board Visualization
            #Change the Current Player color


################################################################################
#This part is the logic from the pseudo code that I made on 11/7/17

# def __init__(Vertical,Horizontal,Color):
#     self.V = Vertical               #Vertical Location on board
#     self.H = Horizontal             #Horizontal Location on board
#     self.C = Color                  #Color of piece
#     self.L = True                   #Check to see if its alive
#     self.moveCount = 0
#     self.type = NULL                #this is a string

#Initaialization function
def __Init__():
    #This function will create a list of the starting chess pieces

def is_clear(V1, H1, V2, H2):
    #We know that the first location is good because that's where the piece starts
    if H1 == H2:
        #Iterate through the vertical line and search for pieces
    if V1 == V2:
        #Iterate through the Horizontal line and search for pieces
    if (V1 != V2 and H1 != H2):
        #iterate through the diagonal Line

def is_legal(Piece, nV, nH):
    #This function will return true if the move is legal in the game and False if it is not


    #Check if there is a same color piece at the desired spot
        #return False

    #####

        #Pawn Legal Moves=======================================================
        if Piece.type == 'P':
            #Need two different versions of this for White and Black
            #White Pawn---------------------------------------------------------
            #move in the Positive V direction
            if Piece.C == 'W':
                #Can move two spaces forward on first move
                #Check for First move
                if Piece.moveCount == 0:
                    if (nV == Piece.V + 2) and (nH == Piece.H):
                        Piece.moveCount = Piece.moveCount + 1#Increment moveCount
                        return True
                #Can move one space forward
                if (nV == Piece.V + 1) and (nH == Piece.H):
                    Piece.moveCount = Piece.moveCount + 1#Increment moveCount
                    return True
                #Can move one space forward and one space in either horizontal direction if it can capture
                if (nV == Piece.V + 1) and (nH == Piece.H-1 or nH == Piece.H+1):
                    ###################################
                    #if there is an enemy piece in the position
                    ###################################
                    return True
                #If none of the above statements are true, fall down into return False
                return False

            #Black Pawn---------------------------------------------------------
            #move in the Negative V direction
            if Piece.C == 'B':
                #Can move two spaces forward on first move
                if Piece.moveCount == 0:
                    if (nV == Piece.V - 2) and (nH == Piece.H):
                        Piece.moveCount = Piece.moveCount + 1#Increment moveCount
                        return True
                #Can move one space forward
                if (nV == Piece.V - 1) and (nH == Piece.H):
                    Piece.moveCount = Piece.moveCount + 1#Increment moveCount
                    return True
                #Can move one space forward and one space in either horizontal direction if it can capture
                if (nV == Piece.V - 1) and (nH == Piece.H-1 or nH == Piece.H+1):
                    ###################################
                    #if there is an enemy piece in the position
                    ###################################
                    return True
                #If none of the above statements are true, fall down into return False
                return False

        #Bishop Legal moves=====================================================
        if Piece.type == 'B':
            #can move diagonally any amount and can capture
            if (nV == Piece.V + )


        #Castle
            #Castling **
            #Can move linearly in any direction for any length and capture

        #Knight
            #Can move one space in one direction and two in the other direction

        #Queen
            #Combine bishop and castle move sets

        #king
            #Can move one space in any direction
