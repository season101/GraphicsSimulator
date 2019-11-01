from graphics import *
programWindow = createWindow('Graphics Simulator', 500, 670, 'Light Blue')
createRectangle(programWindow,15,15,485,435,'White')





valueShifter=0

slider=37.5
X=30
Y=30

for x in range (1,3):
    valueShifter+=1
    for y in range (1,3):
        a= str(x*33)
        b= str(y*33)


        if valueShifter== 1:
            colorCode = a+b+str(valueShifter*33)
        if valueShifter== 2:
            colorCode = a+str(valueShifter*33)+b
        if valueShifter== 3:
            colorCode = str(valueShifter*33)+a+b




        #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)
        X=(10)+x*(75)
        Y=(10)+y*(75)
        createRectangle(programWindow,X+slider,Y+slider,X+slider+75,Y+slider+75,'',2,colorCode)

        #Create Circle takes following in order : window, (centre of circle(x,y)), radius, fill color, outline width and color of outline)

        createRectangle(programWindow,X,Y,X+slider,Y+slider,'',2,colorCode)


key = programWindow.getKey()
if key=="Escape":
    programWindow.close()
