#This File will define all Unit Tests
import unittest
from Model import *
from PieceClasses import *

class TestBasicMovement(unittest.TestCase):
    def setUp(self):
        self.c = piece("castle", "white", 4, 4)
        self.wp = piece("pawn", "white", 2, 2)
        self.bp = piece("pawn", "black", 2, 6)
        self.b = piece("bishop", "white", 4, 4)
        self.n = piece("knight", "white", 5, 4)
        self.q = piece("queen", "white", 5, 4)
        self.k = piece("king", "white", 3,3)
    def test_pawn_white(self):
        #good move
        self.assertTrue(isInMoveSet(self.wp, False, 2, 3))
        self.assertTrue(isInMoveSet(self.wp, False, 2, 4))
        #capture
        self.assertTrue(isInMoveSet(self.wp, True, 3, 3))
        self.assertTrue(isInMoveSet(self.wp, True, 1, 3))
        #bad move
        self.assertFalse(isInMoveSet(self.wp, False, 2, 1))
        self.assertFalse(isInMoveSet(self.wp, False, 2, 1))
    def test_pawn_black(self):
        #good move
        self.assertTrue(isInMoveSet(self.bp, False, 2, 5))
        self.assertTrue(isInMoveSet(self.bp, False, 2, 4))
            #capture
        self.assertTrue(isInMoveSet(self.bp, True, 3, 5))
        self.assertTrue(isInMoveSet(self.bp, True, 1, 5))
        #bad move
        self.assertFalse(isInMoveSet(self.bp, False, 2, 1))
        self.assertFalse(isInMoveSet(self.bp, False, 2, 1))
    def test_castle(self):
        #good move
        self.assertTrue(isInMoveSet(self.c, False, 4, 8))
        self.assertTrue(isInMoveSet(self.c, False, 4, 1))
        self.assertTrue(isInMoveSet(self.c, False, 8, 4))
        self.assertTrue(isInMoveSet(self.c, False, 1, 4))
        #bad move
        self.assertFalse(isInMoveSet(self.c, False, 1, 1))
        self.assertFalse(isInMoveSet(self.c, False, 1, 2))
        self.assertFalse(isInMoveSet(self.c, False, 1, 3))
        self.assertFalse(isInMoveSet(self.c, False, 1, 5))
    def test_knight(self):
        #good move
        self.assertTrue(isInMoveSet(self.n, False, 4, 2))
        self.assertTrue(isInMoveSet(self.n, False, 4, 6))
        self.assertTrue(isInMoveSet(self.n, False, 6, 2))
        self.assertTrue(isInMoveSet(self.n, False, 6, 6))
        self.assertTrue(isInMoveSet(self.n, False, 3, 3))
        self.assertTrue(isInMoveSet(self.n, False, 7, 3))
        self.assertTrue(isInMoveSet(self.n, False, 3, 5))
        self.assertTrue(isInMoveSet(self.n, False, 7, 5))
        #bad move
        self.assertFalse(isInMoveSet(self.n, False, 7, 7))
    def test_bishop(self):
        #good move
        self.assertTrue(isInMoveSet(self.b, False, 1, 1))
        self.assertTrue(isInMoveSet(self.b, False, 2, 2))
        self.assertTrue(isInMoveSet(self.b, False, 3, 3))
        self.assertTrue(isInMoveSet(self.b, False, 5, 5))
        self.assertTrue(isInMoveSet(self.b, False, 6, 6))
        self.assertTrue(isInMoveSet(self.b, False, 7, 7))
        #bad move
        self.assertFalse(isInMoveSet(self.n, False, 3, 8))
        self.assertFalse(isInMoveSet(self.n, False, 7, 2))
    def test_queen(self):
        #good move
        self.assertTrue(isInMoveSet(self.q, False, 5, 8))
        self.assertTrue(isInMoveSet(self.q, False, 5, 1))
        self.assertTrue(isInMoveSet(self.q, False, 8, 4))
        self.assertTrue(isInMoveSet(self.q, False, 1, 4))
        self.assertTrue(isInMoveSet(self.q, False, 6, 5))
        self.assertTrue(isInMoveSet(self.q, False, 7, 6))
        self.assertTrue(isInMoveSet(self.q, False, 4, 3))
        self.assertTrue(isInMoveSet(self.q, False, 3, 2))
        #bad move
        self.assertFalse(isInMoveSet(self.q, False, 3, 8))
        self.assertFalse(isInMoveSet(self.q, False, 1, 1))
    def test_king(self):
        #good move
        self.assertTrue(isInMoveSet(self.k, False, 4, 4))
        self.assertTrue(isInMoveSet(self.k, False, 4, 3))
        self.assertTrue(isInMoveSet(self.k, False, 3, 4))
        self.assertTrue(isInMoveSet(self.k, False, 2, 2))
        self.assertTrue(isInMoveSet(self.k, False, 3, 2))
        self.assertTrue(isInMoveSet(self.k, False, 2, 3))
        self.assertTrue(isInMoveSet(self.k, False, 4, 2))
        self.assertTrue(isInMoveSet(self.k, False, 2, 4))
        #bad move
        self.assertFalse(isInMoveSet(self.k, False, 3, 8))
        self.assertFalse(isInMoveSet(self.k, False, 8, 8))
    def test_isOnBoard(self):
        #On Board
        self.assertTrue(isOnBoard(4, 4))
        self.assertTrue(isOnBoard(1, 7))
        self.assertTrue(isOnBoard(1, 6))
        self.assertTrue(isOnBoard(4, 7))
        self.assertTrue(isOnBoard(2, 5))
        self.assertTrue(isOnBoard(8, 2))
        self.assertTrue(isOnBoard(4, 4))
        #Not On Board
        self.assertFalse(isOnBoard(0, 0))
        self.assertFalse(isOnBoard(9, 9))
        self.assertFalse(isOnBoard(4, 9))

class TestInbetweenMovement(unittest.TestCase):
#return 1 = good move, nothing in the way
#return 2 = capturing piece
#return 3 = team piece in the spot
#return 4 = piece in the way-between
    def setUp(self):
        self.c = piece("castle", "white", 4, 6)
        self.b = piece("bishop", "white", 5, 5)
        self.q = piece("queen", "white", 3, 3)
        self.wp = piece("pawn", "white", 2, 2)
        self.bp = piece("pawn", "black", 2, 6)
        self.board = [self.c, self.wp, self.bp, self.q, self.b]
    def test_basic_endpoint(self):
        self.assertEqual(maybeInTheWay(self.board, self.wp, 2, 3), 1)
    def test_between_castle(self):
        #Good Move = 1
        self.assertEqual(maybeInTheWay(self.board, self.c, 5, 6), 1)
        #Capturing = 2
        self.assertEqual(maybeInTheWay(self.board, self.c, 2, 6), 2)

    # def test_between_bishop(self):
    # def test_between_queen(self):


#This Will run all tests
if __name__ == '__main__':
    unittest.main()
