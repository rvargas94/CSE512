#testing graphics out

from graphics import *

def main():
    win = GraphWin ("Circle", 500, 500)
    nose = Circle(Point(250,250), 10)
    eyes = [Circle(Point(200,350), 10),Circle(Point(300,350), 10)]
    nose.draw(win)
    for i in eyes
        eyes[i].draw(win)
    win.getMouse()
    win.close()

main()
