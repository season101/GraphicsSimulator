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
    '''
    #Creating TextBox for Title
    createRectangle(programWindow,290.55,550.34,510.13,590.45,'Blue')

    #Creating Text to Display Title
    createText(programWindow,400,570,"Pattern Creator",16,'bold')
    '''

    #Creating Box to Display Pattern
    createRectangle(programWindow,222.75,10,668.25,325,'White')


    # Waiting for input for program execution.
    key = programWindow.getKey()
    if key=="Escape":
        programWindow.close()

main()
