__author__ = 'Hendrik'

import serge.visual
import serge.actor
import serge.sound

from cfg import *
from checktile import CheckTile


#class for the bomb. includes all the funcs needed for the bomb
class Bomb(serge.actor.Actor):
    def __init__(self, x, y):
        #vars included in cfg.py, not yet implemented
        global bombs, extime
        """

        :param extime: delay to explode
        :param amount: total bombs
        :param x: x coordinates to drop bomb
        :param y: y coordinates to drop bomb
        """
        #check if bomb is to be placed
        super(Bomb, self).__init__('bomb')

        #set the sprite information
        self.setSpriteName("bomb")
        self.setLayerName("middle")

        #current coordinates
        self.x = x
        self.y = y

        #the checktile func
        self.checktile = CheckTile(x, y)

        #not-yet-implemented vars
        self_bombamount = bombs
        self_timetoexplode = extime

        #sound cfg
        self.bombdrop = serge.sound.SoundItem(RESOURCES_DIR+"/sounds/Bomb_plant.wav")
        self.explode = serge.sound.SoundItem(RESOURCES_DIR+"/sounds/Bomb_explosion.wav")


        """
        "pseudo code", ignore this


        bomb drop - self.timer=time()

        bomb explode - on every update(): time() - self.timer > 2 sec?

        bomb explode action:
            actors at bomb (down, left etc) - list world.findactorsat()
            for each actor in collection:
                is name dirt?
                    world.remove(actor)"""


    def updateActor(self, interval, world):
        global bombmsgs, bombdrop, explode
        #update everything (bomb)
        super(Bomb, self).updateActor(interval, world)
        #bombdrop = serge.sound.SoundItem(RESOURCES_DIR+"/sounds/Bomb_plant.wav")
        explode = serge.sound.SoundItem(RESOURCES_DIR+"/sounds/explosion.wav")
        #bombdrop.play()
        if bombmsgs is True:
            print "DEBUG: bomb was dropped"
        world.removeActor(self)
        if bombmsgs is True:
            print "DEBUG: bomb was removed"
        explode.play()

        #check, where dirt blocks are to be removed
        for i in ["left", "right", "down", "up"]:
            self.checktile.removedirt(world, i)

    def blowup(self, world):
        #WIP


        """
        #check left, right, up, down
        self.tileright = self.checktile.tileright(world)
        self.tileleft = self.checktile.tileleft(world)
        self.tileup = self.checktile.tileup(world)
        self.tiledown = self.checktile.tiledown(world)

        if self.tileright is False:


        if self.tileleft is False:


        if self.tileup is False:


        if self.tiledown is False:"""
