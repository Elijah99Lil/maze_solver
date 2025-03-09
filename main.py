from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    
    # Test a simple line to make sure the Window is working
    test_line = Line(Point(10, 10), Point(100, 100))
    win.draw_line(test_line)
    
    # Create and draw cells
    cell = Cell(200, 200, 300, 300, win)
    cell.draw()
    
    cell2 = Cell(400, 400, 500, 500, win)
    cell2.has_bottom_wall = False
    cell2.draw()
    
    win.wait_for_close()



main()