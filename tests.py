import unittest
from maze import Maze # type: ignore
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(200,200)
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        win = Window(200,200)
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_white_lines(self):
        win = Window(200,200)
        num_rows = 10
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            line = "white"
        )

if __name__ == "__main__":
    unittest.main()