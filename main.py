from graphics import Window, Line, Point, Cell
from maze import Maze # type: ignore

def main():
    win = Window(825, 625)

    maze = Maze(10, 10, 12, 16, 50, 50, win)
    
    '''#Test a simple line to make sure the Window is working
    test_line = Line(Point(10, 10), Point(100, 100))
    win.draw_line(test_line)
    

    # Create and draw cells
    cell = Cell(100, 100, 125, 125, win)
    cell.has_top_wall = False
    cell.has_right_wall = False
    cell.draw()
    
    cell2 = Cell(125, 100, 150, 125, win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell2.draw()
    cell.draw_move(cell2)

    cell3 = Cell(125, 125, 150, 150, win)
    cell3.has_bottom_wall = False
    cell3.has_top_wall = False
    cell3.draw()
    cell2.draw_move(cell3)'''
        
    print()
    win.wait_for_close()

main()