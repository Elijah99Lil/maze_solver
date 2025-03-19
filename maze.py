from graphics import Cell, Window
from tkinter import Tk, BOTH, Canvas
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

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