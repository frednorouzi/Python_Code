"""
Fariborz Norouzi
MET_CS521
6/21/2018
Term Project _ part2
Description:
   (Tkinter: Connect Four Game by using a GUI program)
   The program enables two players to place red and yellow disks in turn.
   To place a disk, the player needs to click on an available cell.
   An available cell is unoccupied and its downward neighbor is occupied.
   The program flashes the four winning cells if a player wins, and reports 
   no winners if all cells are occupied with no winners. 
"""
from tkinter import *
import tkinter.messagebox as box
class Board(Canvas):
    def __init__(self, parent):
        super().__init__(parent, width = 280, height = 240, bg = 'white')
        # Create grid
        self.bmp = BitmapImage(file="connect_four_small.xbm")
        for row in range(6):
            for col in range(7):
                self.create_image(20 + 40*col, 20 + 40*row, image = self.bmp)
                if col != 0:
                    self.create_line(40*col, 0, 40*col, 240, fill = 'grey')
            if row != 0:
                self.create_line(0, 40*row, 280, 40*row, fill = 'grey')
        # Create a variable to check if token is currently dropping
        self.__dropping = False
    def createToken(self, color, col, row):
        ''' Creates a disk of a specific color and calls dropToken to drop
           it into the correct place'''
        if self.__dropping == True:
            self.after(3, self.createToken, color, col, row)
        else:
            token = self.create_oval(40*col, 0, 40*(col + 1), 40, fill=color,
                                     width = 0, tags=str(row) + ',' + str(col))
            self.tag_lower(token)
            self.dropToken(token, row)

    def dropToken(self, token, row):
        ''' This method animates the drop of the token into the correct 
            space.'''
        if self.coords(token)[1] < 40*row:
            self.__dropping = True
            self.move(token, 0, 1)
            self.after(4, self.dropToken, token, row)
        else:
            self.__dropping = False
class ConnectFour:
    def __init__(self):
        # Create the window
        win = Tk()
        win.title('Connect Four')
        # Create the Connect Four board
        self.board = Board(win)
        self.board.pack()
        # Create reset button
        Button(win, text = 'Start Over', command = self.reset).pack()

        # Create 2d list to represent the board (for easier win-checking)
        self.filled = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7, ['']*7]

        # Create variable to hold the current player
        self.turn = 'red'
        # Create variable to tell when game is over (at which point clicking
        # shouldn't do anything)
        self.gameOver = False
        # Bind mouse clicks to board
        self.board.bind('<Button-1>', self.makeSelection)
        # Start event loop
        win.mainloop()

    def makeSelection(self, event):
        ''' If the user clicks on an available space, a token is dropped into
            that column.'''
        if not (event.x % 40 == 0 or event.y % 40 == 0 or self.gameOver):
            row, col = event.y // 40, event.x // 40
            if self.filled[row][col] == '' and (row == 5 or
               self.filled[row+1][col] != ''):
                self.board.createToken(self.turn, col, row)
                self.filled[row][col] = self.turn
                if not self.isWinner():
                    self.moreSpaces()
                self.turn = 'yellow' if self.turn == 'red' else 'red'

    def isWinner(self):
        ''' Checks if there is a winner.  If so it sets gameOver to True, 
             displays a message for the users, turns the winning tokens 
             turquoise, and returns True. Otherwise, it returns False.'''
        check = [self.checkRows(), self.checkColumns(), self.checkDiagonals()]
        if check != [[], [], []]:
            box.showinfo('Winner', self.turn.capitalize() + ' Player wins!')
            self.gameOver = True
            if check[0] != []:
                [self.board.itemconfig(str(x) + ',' + str(y),fill='turquoise1')
                 for [x,y] in check[0]]
            elif check[1] != []:
                [self.board.itemconfig(str(x) + ',' + str(y),fill='turquoise1')
                 for [x,y] in check[1]]
            else:
                [self.board.itemconfig(str(x) + ',' + str(y),fill='turquoise1')
                 for [x,y] in check[2]]
            return True
        return False

    def moreSpaces(self):
        ''' Checks if the game board is completely filled.  If it is, gameOver
            is set to True and a message is displayed to the users.'''
        self.gameOver = True
        for row in self.filled:
            if '' in row:
                self.gameOver = False
                break
        if self.gameOver:
            box.showinfo('Draw', 'The board is full.  You both draw.')

    def reset(self):
        ''' This function resets everything so play can begin again.'''
        self.filled = [['']*7, ['']*7, ['']*7, ['']*7, ['']*7, ['']*7]
        for row in range(6):
            for col in range(7):
                self.board.delete(str(row) + ',' + str(col))
        self.turn = 'red'
        self.gameOver = False

    def checkRows(self):
        ''' Checks for four-in-a-row. Returns a list of [row, column] lists
           if there are four-in-a-row. Otherwise, it returns the empty list.'''
        b = self.filled
        for row in range(6):
            for col in range(4):
                if b[row][col] != '' and (b[row][col] == b[row][col + 1] ==
                                          b[row][col + 2] == b[row][col + 3]):
                    return [[row, i] for i in range(col, col + 4)]
        return []

    def checkColumns(self):
        '''Checks for four-in-a-column. Returns a list of [row, column] lists
        if there are four-in-a-column. Otherwise, it returns the empty list.'''
        b = self.filled
        for col in range(7):
            for row in range(3):
                if b[row][col] != '' and (b[row][col] == b[row + 1][col] ==
                                          b[row + 2][col] == b[row + 3][col]):
                    return [[i, col] for i in range(row, row + 4)]
        return []

    def checkDiagonals(self):
        ''' Checks for four-in-a-diagonal.  There are two types of diagonals,
        so it checks them individually. Returns a list of [row, column] lists
        if there are four-in-a-diagonal. Otherwise, it returns the empty list.
        '''
        b = self.filled
        # Check backslash kind of diagonal
        for col in range(4):
            for row in range(3):
                if b[row][col] != '' and (b[row][col] == b[row+1][col+1] ==
                                          b[row+2][col+2] == b[row+3][col+3]):
                    return [[row + i, col + i] for i in range(4)]
        # Check forwardslash kind of diagonal
        for col in range(4):
            for row in range(3, 6):
                if b[row][col] != '' and (b[row][col] == b[row-1][col+1] ==
                                          b[row-2][col+2] == b[row-3][col+3]):
                    return [[row - i, col + i] for i in range(4)]
        return []
ConnectFour()
