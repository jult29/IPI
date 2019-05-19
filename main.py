import sys
import select
import tty
import termios
import os

import Enemy
import Field
import Player
import Tir

old_settings = termios.tcgetattr(sys.stdin)

enemy = []
field = []
player = []
tir = []



def init():
#    player.askName()
    grid = field.create()
            
def run():
        show()
        interact()
        
def show():
    grid = field.show()
#    player.show()
#    tir.show()
#    enemy.show()

#def testVictory():
#    if level = levelmax:
#        testVictory = 1
#        finish()
#    else :
#        testVictory = 0
#        Level(e)

#def Level(e):
#    nbenemny = 3
#    if testVictory = 0
#        nbenemy = nbenemy + 1
#    else:
#        none
    
#def finishLevel():
#    if nbenemny = 0:
#        finishLevel = 1
#        testVictory()
#    else:
#        None



#def finish():
    #affiche le visuel de sortie en fonction du resulatat


#def interact():
#        player.tir()
#            tir.testCollisionTE()
#            enemy.move()
#            enemy.testCollisionEZ()
#            field.create()
#        player.move()
#            enemy.move()
#            enemy.testCollisionEZ()
#            field.create()
#        finishLevel()
#            testVictory()
#        finish()




 

init()
run()
#level a definir + nb enemy
#create nouvelle partie
