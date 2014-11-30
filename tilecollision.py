__author__ = 'Hendrik'

import mapimport


#input tile coordinates, output coordinates on screen
def findcoordinatfromtile(tilelocation):
    screenlocation = []
    try:
        for i in tilelocation:
            screenlocation.append(i*64)
    except:
        print "Can't multiply non-int by int"
        raise ValueError
    return screenlocation

def findtilefromcoordinate(screenlocation):
    tilelocation = []




