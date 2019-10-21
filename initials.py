from graphics import *

# create a program window
window = createWindow("Initials", 800, 500, 'white')

### DISPLAY HEADER ####

# create box
createRectangle(window, 100, 430, 300, 480, "light yellow", 5, 'orange')

# create text for header
createText(window, 200, 455, "INITIALS!!", 16, 'bold')


### GET USER INPUT ###

# get name
name = createInputBox(window, "Enter full name: ", 380, 'light blue', 14, 'bold')


### CREATE INITIALS ###

# locate space
n = name.find(' ')

# get first and last initial
initials = name[0] + "." + name[n + 1] + "."


### DISPLAY INITIALS ###

# display initials in table
createTable(window, 'orange1', 2, 320, 16, 'bold' , ("Names", name), ("Initials", initials))

## OR

# display initials

##createRectangle(window, 10, 290, 130 ,345, "white", 3, 'orange')
##createRectangle(window, 10, 260, 130 ,305, "white", 3, 'orange')
##
##createText(window, 70, 310, "Initials\n", 16, 'bold')
##createText(window, 45, 280, initials, 16, 'bold')
