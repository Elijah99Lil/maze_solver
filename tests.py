import unittest
from maze import Maze # type: ignore
from graphics import Window, Line

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
        print(f"Rows = {num_rows} and Columns = {num_cols}")
        print(f"Seed number = {m1.seed}")

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
        print(f"Large Rows = {num_rows} and Large Columns = {num_cols}")
        print(f"Seed number = {m1.seed}")

    def test_reset_visited(self):
        win = Window(200,200)
        num_rows = 10
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

        for row in m1._cells:
            for cell in row:
                cell.visited = True

        m1._reset_cells_visited()

        for row in m1._cells:
            for cell in row:
                self.assertFalse(cell.visited)
        print(f"Visited status = {cell.visited}")
        print(f"Seed number = {m1.seed}")

if __name__ == "__main__":
    unittest.main()