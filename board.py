from turtle import Turtle
import random


class Board:
    def __init__(self):
        self.__drawer = Turtle()
        self.__drawer.shape('square')
        self.__drawer.hideturtle()
        self.__drawer.penup()
        self.__drawer.shapesize(5, 5, outline=0.0)
        self.__drawer.fillcolor('#E0E0E0')

        self.__board = [[0] * 4 for _ in range(4)]
        self.__add_random_element()

    def __add_random_element(self):
        empty_positions = [(row, col) for row in range(4) for col in range(4) if self.__board[row][col] == 0]

        if empty_positions:
            row, col = random.choice(empty_positions)
            self.__board[row][col] = 2
        else:
            pass

    def __merge_row_left(self, row):
        i = 0
        while i < 3:
            if row[i] == 0:
                i += 1
                continue
            j = i + 1
            while j < 4:
                if row[j] == 0:
                    j += 1
                elif row[i] == row[j]:
                    row[i] *= 2
                    row[j] = 0
                    i = j + 1
                    break
                else:
                    break
            i = j

    def __slide_row_left(self, row):
        for i in range(3):
            if row[i] == 0:
                for j in range(i, 4):
                    if row[j] != 0:
                        row[i] = row[j]
                        row[j] = 0
                        break

    def __merge_row_right(self, row):
        i = 3
        while i > 0:
            if row[i] == 0:
                i -= 1
                continue
            j = i - 1
            while j >= 0:
                if row[j] == 0:
                    j -= 1
                elif row[i] == row[j]:
                    row[i] *= 2
                    row[j] = 0
                    i = j - 1
                    break
                else:
                    break
            i = j

    def __slide_row_right(self, row):
        for i in range(3, 0, -1):
            if row[i] == 0:
                for j in range(i, -1, -1):
                    if row[j] != 0:
                        row[i] = row[j]
                        row[j] = 0
                        break

    def __transpose(self):
        n = len(self.__board)
        m = len(self.__board[0])
        transposed = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                transposed[j][i] = self.__board[i][j]
        for i in range(n):
            for j in range(m):
                self.__board[i][j] = transposed[i][j]

    def __merge_and_slide_left(self):
        for row in self.__board:
            self.__merge_row_left(row)
            self.__slide_row_left(row)

    def __merge_and_slide_right(self):
        for row in self.__board:
            self.__merge_row_right(row)
            self.__slide_row_right(row)

    def left(self):
        self.__merge_and_slide_left()
        self.__add_random_element()
        self.display()

    def right(self):
        self.__merge_and_slide_right()
        self.__add_random_element()
        self.display()

    def up(self):
        self.__transpose()
        self.__merge_and_slide_left()
        self.__transpose()
        self.__add_random_element()
        self.display()

    def down(self):
        self.__transpose()
        self.__merge_and_slide_right()
        self.__transpose()
        self.__add_random_element()
        self.display()

    def __draw_tile(self, number: int):
        self.__drawer.stamp()

        if number != 0:
            self.__drawer.sety(self.__drawer.ycor() - 10)
            self.__drawer.write(
                number,
                font=("Verdana", 20, "normal"),
                align="center"
            )

    def display(self):
        self.__drawer.clear()

        starting_y = 150
        for row_index, row in enumerate(self.__board):
            starting_x = -155
            for tile in row:
                self.__drawer.goto(starting_x, starting_y)
                self.__draw_tile(tile)
                starting_x += 100
            starting_y -= 100

        self.__drawer.getscreen().update()
