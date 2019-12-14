# This file will contain the main logic for the game

#First build the starting arrays to be drawn to the board
from PieceClasses import *
from View import *
from Model import *

board = buildBoard() #ChessVisualization
draw(board)
