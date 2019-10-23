#Working with graphics first for program
from graphics import *


def rectangle():
    createRectangle(programWindow, 20,40,40,60,'green',10,'yellow')

def circle():
    createCircle(programWindow,200,200,100,'red')

def main():
    #creating graphic window
    programWindow = createWindow('Graphics Simulator', 891, 630, 'Light Blue')


    #Displaying Header for Title

    #Creating TextBox for Title
    createRectangle(programWindow,290.55,550.34,510.13,590.45,'Blue')

    #Creating Text to Display Title
    createText(programWindow,400,570,"Pattern Creator",16,'bold')


    #Creating Box to Display Pattern
    createRectangle(programWindow,222.75,10,668.25,325,'White')

    #Creating Circle Test (export it to def circle() later after successful execution)
    for x in range (1,4):
        for y in range (1,4):
            #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)
            X=445.5+x*(100)
            Y=167.5+y*(100)
            createCircle(programWindow,X,Y,100,'',2,'Red')


    # Waiting for input for program execution.
    key = programWindow.getKey()
    if key=="Escape":
        programWindow.close()

main()
