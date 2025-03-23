from graphics import Cell, Window
from tkinter import Tk, BOTH, Canvas
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                # calculate coordinates
                x1 = self._x1 + (j * self._cell_size_x)
                y1 = self._y1 + (i * self._cell_size_y)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                new_cell = Cell(x1, y1, x2, y2, self._win)
                row.append(new_cell)
            self._cells.append(row)
        
        # Now draw all cells after the matrix is fully populated
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.008)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        bottom = len(self._cells) - 1
        right = len(self._cells[0]) - 1
        self._cells[bottom][right].has_bottom_wall = False
        self._draw_cell(bottom, right)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j < self._num_cols - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i < self._num_rows - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                random_index = random.randrange(len(to_visit))
                next_i, next_j = to_visit[random_index]

                # If moving right: current (i,j) to (i,j+1)
                if next_i == i and next_j == j + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_i][next_j].has_left_wall = False
                    
                # If moving left: current (i,j) to (i,j-1)
                elif next_i == i and next_j == j - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_i][next_j].has_right_wall = False
                    
                # If moving down: current (i,j) to (i+1,j)
                elif next_i == i + 1 and next_j == j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_i][next_j].has_top_wall = False
                    
                # If moving up: current (i,j) to (i-1,j)
                elif next_i == i - 1 and next_j == j:
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_i][next_j].has_bottom_wall = False

                self._break_walls_r(next_i, next_j)
