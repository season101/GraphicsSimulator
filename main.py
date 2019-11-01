
# ###################### Introduction #############################
#                                                                 #
#    #Name: Sijan Malla              Date Assigned: Oct. 17,2019  #
#    #                                                            #
#    #Course: 2000-44306             Date Due : Oct. 24, 2019     #
#    #                                                            #
#    #File name: Programming Assignment 5                         #
#    #                                                            #
#    #Program Description: It is a program that displays patterns #
#                          using Graphics library                 #
#                                                                 #
##################### Program Begins ##############################

#Working with graphics first for program
from graphics import *

def circle(programWindow):

    valueShifter=0
    for x in range (1,4):
        valueShifter+=1
        for y in range (3,0,-1):
            a= str(x*33)
            b= str(y*33)

            if valueShifter== 1:
                colorCode = a+b+str(valueShifter*33)
            if valueShifter== 2:
                colorCode = a+str(valueShifter*33)+b
            if valueShifter== 3:
                colorCode = str(valueShifter*33)+a+b

            colorCode = "#"+str(colorCode)

            #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)
            X=90+x*(75)
            Y=75+y*(75)
            createCircle(programWindow,X,Y,75,'',2,colorCode)


def rectangle(programWindow):

    valueShifter=0
    slider=0
    for x in range (1,4):
        valueShifter+=1
        for y in range (1,4):
            a= str(x*33)
            b= str(y*33)


            if valueShifter== 1:
                colorCode = a+b+str(valueShifter*33)
            if valueShifter== 2:
                colorCode = a+str(valueShifter*33)+b
            if valueShifter== 3:
                colorCode = str(valueShifter*33)+a+b

            colorCode = "#"+str(colorCode)

            #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)
            X=(100)+x*(75)
            Y=(80)+y*(75)
            createRectangle(programWindow,X-slider,Y-slider,X-slider+75,Y-slider+75,'',2,colorCode)
        slider+=37.5
            #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)

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
    userChoice = createInputBox(programWindow,"Enter pattern Choice (1 or 2): ",460,"Light Green",10,"bold")

    #Creating Box to Display Pattern
    createRectangle(programWindow,15,15,485,435,'White')

    if userChoice == "1":
        circle(programWindow)

    if userChoice == "2":
        rectangle(programWindow)


    # Waiting for input for program execution.
    key = programWindow.getKey()
    if key=="Escape":
        programWindow.close()

main()
