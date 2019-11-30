#The Piece Class contains the following data variables
#type (pawn, bishop etc.) - dictionary
#color (white, black) - bool
#Location(Array [x,y]) - int array
#move count - int
#drawn(reduces number of checks when drawing the board) - bool

class piece:
    def __init__(self, TYPE, COLOR, posx, posy):
        self.type=TYPE
        self.color = COLOR
        self.x = posx
        self.y = posy
        self.movecount = 0
        self.drawn = False
