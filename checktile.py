__author__ = 'Hendrik'

#class and functions to check if there is a sprite somewhere
class CheckTile():

    #feed the current coordinates into the class init
    def __init__(self, posX, posY):
        self.xtile = posX
        self.ytile = posY
        self.tileright = (posX+67)
        self.tileleft = (posX-4)
        self.tileup = (posY-4)
        self.tiledown = (posY+67)

        #vars with _ in the end are for the removedirt func
        self.xtile_ = self.xtile# - 32
        self.ytile_ = self.ytile# - 32
        self.tileright_ = self.xtile_+67
        self.tileleft_ = self.xtile_-35
        self.tileup_ = self.ytile_-35
        self.tiledown_ = self.ytile_+67


    #extremely ugly code, for checking if player is obstructed by a tile
    def checkleft(self, world):
        #print self.xtile, self.ytile, self.tiledown
        if len(world.findActorsAt(self.tileleft, self.ytile).forEach().getSpriteName() + \
                world.findActorsAt(self.tileleft, self.ytile+63).forEach().getSpriteName()) > 2:
            canMoveLeft = False
        else:
            canMoveLeft = True
        return canMoveLeft

    def checkright(self, world):
        if len(world.findActorsAt(self.tileright, self.ytile).forEach().getSpriteName() + \
                world.findActorsAt(self.tileright, self.ytile+63).forEach().getSpriteName()) > 2:
            canMoveRight = False
        else:
            canMoveRight = True
        return canMoveRight

    def checkup(self, world):
        if len(world.findActorsAt(self.xtile, self.tileup).forEach().getSpriteName() + \
                world.findActorsAt(self.xtile+63, self.tileup).forEach().getSpriteName()) > 2:
            canMoveUp = False
        else:
            canMoveUp = True
        return canMoveUp

    def checkdown(self, world):
        if len(world.findActorsAt(self.xtile, self.tiledown).forEach().getSpriteName() + \
                world.findActorsAt(self.xtile+63, self.tiledown).forEach().getSpriteName()) > 2:
            canMoveDown = False
        else:
            canMoveDown = True
        return canMoveDown

    #func for deleting dirt blocks. called out by bomb.py
    def removedirt(self, world, side):

        #check all the sides
        if side == "left":
            for i in (world.findActorsAt(self.tileleft_, self.ytile_)) + (world.findActorsAt(self.tileleft_, self.ytile_)):
                if i.getSpriteName() == "Dirt":
                    print "removed left"
                    try:
                        world.removeActor(i)
                    except:
                        pass

        if side == "right":
            print self.tileright_
            for j in (world.findActorsAt(self.tileright_, self.ytile_)) + (world.findActorsAt(self.tileright_, self.ytile_)):
                if j.getSpriteName() == "Dirt":
                    print "removed right"
                    try:
                        world.removeActor(j)
                    except:
                        pass

        if side == "up":
            for k in (world.findActorsAt(self.xtile_, self.tileup_)) + (world.findActorsAt(self.xtile_, self.tileup_)):
                if k.getSpriteName() == "Dirt":
                    print "removed up"
                    try:
                        world.removeActor(k)
                    except:
                        pass

        if side == "down":
            for l in (world.findActorsAt(self.xtile_, self.tiledown_)) + (world.findActorsAt(self.xtile_, self.tiledown_)):
                print l.getSpriteName(),l.getSpriteName
                if l.getSpriteName() == "Dirt":
                    print "removed down"
                    try:
                        world.removeActor(l)
                    except:
                        pass