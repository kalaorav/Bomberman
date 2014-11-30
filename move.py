__author__ = 'Hendrik'

#big modules
import pygame
import serge
import os
import time

#my modules
from cfg import *
import bomb
from checktile import CheckTile

#parts of modules
import serge.engine
import serge.actor
import serge.blocks.visualblocks
import serge.blocks.utils
import serge.blocks.directions
import serge.visual
import serge.world

class Player(serge.actor.Actor):
    #the player class, objects to control it

    def __init__(self, world):
        #start it all up
        super(Player, self).__init__("player")

        self.setSpriteName("player")
        self.setLayerName("front")

        #the moving (update) speed of the player.
        #this wasn't put in cfg.py due to it being badly implemented and often bugging out
        self.movespeed = 4

    def addedToWorld(self, world):
        #add the player to the game
        super(Player, self).addedToWorld(world)
        #init the keyboard
        self.keyboard = serge.engine.CurrentEngine().getKeyboard()

    def updateActor(self, interval, world):
        global posX, posY, testposX, testposY
        #update everything, this func is constantly updated
        super(Player, self).updateActor(interval, world)

        #init this class with the coordinates of the player
        checktile = CheckTile(posX, posY)

        #check tile to the right
        canMoveRight = checktile.checkright(world)

        #left
        canMoveLeft = checktile.checkleft(world)

        #up
        canMoveUp = checktile.checkup(world)

        #down
        canMoveDown = checktile.checkdown(world)

        """
        pseudo code, ignore this

        canmoveto(x,y)
            posx+delta,posy
            posx,posy+delta
            posx-delta,posy
            posx,posy-delta
        check(x,y)
        check(x+w-1,y)
        check(x,y+w-1)
        check(x+w-1,y+w-1)
        """

        #where does the player want to go
        #the var 'facing' was implemented for different sprites, depending on
        #where the player was facing at the current moment.
        if self.keyboard.isDown(pygame.K_LEFT) and canMoveLeft is True:
            direction0 = -1
            direction1 = 0
            testposX = posX - self.movespeed
            facing = "left"
        elif self.keyboard.isDown(pygame.K_RIGHT) and canMoveRight is True:
            direction0 = +1
            direction1 = 0
            testposX = posX + self.movespeed
            facing = "right"
        elif self.keyboard.isDown(pygame.K_UP) and canMoveUp is True:
            direction0 = 0
            direction1 = -1
            testposY = posY - self.movespeed
            facing = "up"
        elif self.keyboard.isDown(pygame.K_DOWN) and canMoveDown is True:
            direction0 = 0
            direction1 = +1
            testposY = posY + self.movespeed
            facing = "down"

        #drop the bomb when space is pressed
        elif self.keyboard.isClicked(pygame.K_SPACE):
            b = bomb.Bomb(posX+32, posY+32)
            world.addActor(b)
            direction0, direction1 = 0, 0
            testposX = posX
            testposY = posY
            facing = "forward"

        #if nothing is pressed, do the following.
        else:
            direction0, direction1 = 0, 0
            testposX = posX
            testposY = posY
            facing = "forward"

        #fulfill the task, move (if possible)
        #should be noted, the sprite moves indefinitely.
        #collision detection prevents the sprite from moving when it shouldn't
        #NB - coordinates of the sprite are taken from its upper left corner
        if posX in range(resoX-tilesizeX+1) and posY in range(resoY-tilesizeY+1):
            for i in range(self.movespeed):
                if posX < 0:
                    for j in range(self.movespeed-1):
                        self.move(+1, 0)
                        testposX += 1
                        facing = "left"
                        print facing
                elif posX > resoX-tilesizeX:
                    for k in range(self.movespeed-1):
                        self.move(-1, 0)
                        testposX -= 1
                        facing = "right"
                        print facing
                elif posY < 0:
                    for l in range(self.movespeed-1):
                        self.move(0, +1)
                        testposY += 1
                        facing = "up"
                        print facing
                elif posY > resoY-tilesizeY:
                    for m in range(self.movespeed-1):
                        self.move(0, -1)
                        testposY -= 1
                        facing = "down"
                        print facing
                self.move(direction0, direction1)
                posX = testposX
                posY = testposY

                #debug stuff
                global facingoutput
                global coordoutput

                if facingoutput is True:
                    print facing

                if coordoutput is True:
                    print "Pos",posX,posY


"""
#old code, de-comment to try running the move.py without other modules


#start up the game engine
engine = serge.blocks.utils.getSimpleSetup(resoX, resoY)
world = engine.getWorld("lab")

#create the player
char = Player()
world.addActor(char)
char.moveTo(stptX, stptY)
posX, posY = stptX-tilesizeX/2, stptY-tilesizeY/2

#start up the game
engine.run(60)
"""