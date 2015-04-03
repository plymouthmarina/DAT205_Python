# Import graphics.py library
from graphics import *

# Open and read data.txt file.
file = open("data.txt")
allGrades = file.readlines()
print allGrades

# GraphWin window 1200x800.
win = GraphWin("Grades", 1200, 800)

# Draw X and Y axes of graph as Line objects.
l = Line(Point(100,200), Point(100,700)).draw(win)
l2 = Line(Point(100,700), Point(1100,700)).draw(win)

# Draw title as Text object. 
text = Text(Point(300, 100), "DAT205 PhoneGap Grades")
text.setSize(20)
text.setFace("helvetica")
text.draw(win)

# Function to draw text at specific coordinates. 
def drawText(x,y,message):
    t = Text(Point(x, y), message)
    t.setFace("helvetica")
    t.setSize(10)
    t.draw(win)

# Draw Y coordinates 50px = 10.
drawText(80, 650,"10")
drawText(80, 600,"20")
drawText(80, 550,"30")
drawText(80, 500,"40")
drawText(80, 450,"50")
drawText(80, 400,"60")
drawText(80, 350,"70")
drawText(80, 300,"80")
drawText(80, 250,"90")

# Draw X coordinates.
drawText(300, 720,"200")
drawText(500, 720,"400")
drawText(700, 720,"600")
drawText(900, 720,"800")

# Specify starting X position for Rectangle object.
firstX = 100
secondX = 130

# Loop through the text file reading each line, converting it into int and draw a rectangle for each grade.
for line in allGrades:    
    grade = int(float(line.strip("\n")))
    rect = Rectangle(Point(firstX, 700 - grade*5),Point(secondX, 700))
    
    # Calculate RGB value of Rectangle object based on each grade (the lower the grade, the darker the rectangle).    
    rect.setFill(color_rgb(grade*2.55,grade*2.55,grade*2.55))
    rect.draw(win)
    firstX = firstX+30
    secondX = secondX+30

# Pause for click in window and close window.
win.getMouse() 
win.close()