#This File will run the Game Logic
#Chess Visualization will Draw the board and take care of the visualizations


#_______________________________________________________________________________
#Checking Variables
player1 = 'white'                       #Variables to check against later in the code
player2 = 'black'
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
