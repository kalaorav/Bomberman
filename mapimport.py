__author__ = 'Hendrik'

#this is the interesting part of the game
#the following imports the needed sprites from the .tmx map file

import pytmx
import serge.actor
import serge.visual
import serge.blocks.utils
from cfg import *


#this class includes all the needed funcs for importing the map's tile-sprites
class HMap(serge.common.Loggable):

    def __init__(self, world):
        #init the map-importing module
        self.tmxdata = pytmx.TiledMap(mapfilename)

        #dictionary of all the imported sprites (tiles)
        self.sprited = dict()

        #2D array
        self.w = [[None for i in xrange(15)] for i in xrange(15)]

        #init stuff
        self.world = world
        self._initialize()

    def _initialize(self):
        #not very dynamic, but if the map is 15x15 tiles big, scan every tile
        for i in range(15):
            for j in range(15):
                self.addToWorld(i, j)

    def addToWorld(self, x, y):
        global RESOURCES_DIR

        #if the bool is true (set in cfg.py),
        # print the coordinates of the current tile being imported
        if importcoordinates is True:
            print x,y

        #path of sprites
        serge.visual.Sprites.setPath(RESOURCES_DIR+"/sprites")

        #info of tile
        imgt = self.tmxdata.get_tile_image(x, y, 0)

        #if there's a tile, do the following
        if not imgt is None:

            #if the bool is true, print the GID of the tile being imported
            if printGID is True:
                print imgt

            #split the GID into the image name etc
            (imgfile, x1, x2) = imgt
            (imgname, extn) = imgfile.split(".")

            #find image name without excess stuff
            for i in imgname.split("/"):
                imga = i

            #if tile not yet drawn, draw it
            if imga not in self.sprited:

                #add tile to drawn list
                self.sprited[imga] = imgfile

                #register the tile image
                serge.visual.Sprites.registerItem(imga, imgfile)

            #make the tile image an actor, on the midlle layer, draw it
            #at the correct location
            a = serge.actor.Actor(imga)
            a.setSpriteName(imga)
            a.setLayerName('middle')
            a.moveTo(x*64+32, y*64+32)

            #add the actor to the world
            self.world.addActor(a)
            self.w[y][x] = imga



