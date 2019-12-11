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


#isBishopMove()
p = piece("bishop", "white", 4, 4)
#testisBishopMove(p)
p = piece("castle", "white", 4, 4)
#testisCastleMove(p)
testisOnBoard()
