from turtle import Screen
from board import Board

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

board = Board()
board.display()

screen.onkeypress(board.right, 'Right')
screen.onkeypress(board.left, 'Left')
screen.onkeypress(board.up, 'Up')
screen.onkeypress(board.down, 'Down')
screen.listen()

screen.mainloop()
