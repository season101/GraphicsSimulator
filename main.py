#Working with graphics first for program
from graphics import *

def rectangle():
    createRectangle(programWindow, 20,40,40,60,'green',10,'yellow')

def circle(programWindow):

    for x in range (1,4):
        for y in range (1,4):

            #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)
            X=90+x*(75)
            Y=75+y*(75)
            createCircle(programWindow,X,Y,75,'',2,"#00ffff")


def main():
    #creating graphic window
    programWindow = createWindow('Graphics Simulator', 500, 670, 'Light Blue')

    #Creating Rectangle To Display Title Box
    createRectangle(programWindow,120,620,370,650,'Green')

    #Creating Text to Display Title
    createText(programWindow,250,635,"Pattern Creator",16,'bold')

    #Creating Table To Display userChoice
    createTable(programWindow,'Light Green',1,595,10,'bold',("Patterns","","1. Circles   ","","2. Rectangles",""))

    #Creating Input Window for Taking userChoice
    createInputBox(programWindow,"Enter pattern Choice (1 or 2): ",460,"Light Green",10,"bold")

    #Creating Box to Display Pattern
    createRectangle(programWindow,15,15,485,435,'White')

    circle(programWindow)



    # Waiting for input for program execution.
    key = programWindow.getKey()
    if key=="Escape":
        programWindow.close()

main()
