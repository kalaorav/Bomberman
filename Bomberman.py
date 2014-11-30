__author__ = 'Hendrik'
#this is the startup file of the game
#loads everything in and starts the game

import serge.blocks.utils
import serge.blocks.visualblocks
import serge.visual
import serge.sound

import move
import mapimport

from cfg import *
#start engine
engine = serge.blocks.utils.getSimpleSetup(resoX, resoY)
world = engine.getWorld("lab")

#some graphics cfg
serge.visual.Sprites.setPath(RESOURCES_DIR+"/sprites")
serge.visual.Sprites.registerItem("player", "player.png")
serge.visual.Sprites.registerItem("bomb", "bomb.png")

#some sound cfg
music = serge.sound.MusicItem(RESOURCES_DIR+"/sounds/levelmusic.mp3")


#create the player
char = move.Player(world)
world.addActor(char)
char.moveTo(stptX, stptY)

#import the map from the map file
hmap = mapimport.HMap(world)

#background
bg = serge.blocks.utils.addVisualActorToWorld(world, 'bg', 'bg',
            serge.blocks.visualblocks.Rectangle((resoX, resoY), (128, 128, 128)),
            layer_name='back',
            center_position=(resoX/2, resoY/2))

#music
music.play(-1)

#run the game/engine
engine.run(30)

