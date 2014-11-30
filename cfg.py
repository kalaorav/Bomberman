__author__ = 'Hendrik'

#this is a configuration file. some/most variables will be
#editable in this file.

#directory of various resource files, such as sprites
RESOURCES_DIR = "data"

#size of one tile. sprite of the player is the same size as tiles
tilesizeX = 64
tilesizeY = 64

#resolution of the window
resoX = 960
resoY = 960

#starting position of the character. don't edit this
stptX = 96
stptY = 96

posX = 64
posY = 64

#the time for the bomb to explode (seconds)
extime = 3

#the amount of bombs possible to drop at the same time (total amount of bombs)
bombs = 2

#map (directory + ) filename
mapfilename = "map.tmx"

#print coords of current tile imported to the world?
importcoordinates = True

#print GID of current tile imported to the world?
printGID = True

#debug config

#output sprite coordinates?
coordoutput = False

#output sprite facing?
facingoutput = False

#output if bomb is placed/explodes?
bombmsgs = True