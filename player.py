import sys
import Field
import os
import Tir

def create(color, X):
    p = dict()
    p["color"]=color
    p["x"]=X
    p["vx"]=vx
    p["y"]=y
    
    return p

def getX(p):
    return p['x']
def setX(p, x):
    p['x']=x

def getVX(p):
    return p['vx']
def setVX(p, vx):
    p['vx']=vx

def getY(p):
    return p['y']
def setY(p,y):
    p['y']=y

def getColor(p):
    return p['color']
def setColor(p, color):
    p['color']

def changeColor(p):
    p['color']=p['color']+1

def move(p, x, field):  #A REVOIR
    x = p['x'] + x

def show(p):
    sys.stdou.write("F30D09")
    
    #c = p['color']
    

    
#tir
#if Keypress = #espace :
#    tir.show(t)

#def score():
#    S = #introduit le score
#    nb4 = #chiffre des dizaines du score
#        if nb5 =< 9 :
 #           nb4 = 0
  #      else:
   #         nb4 = nb + 1
   # nb5 = #chiffre des unites du score
   #     nb5 = 0
   #     if testCollisionTE = 1:
   #         nb5 = nb5 + 1
   #     else :
    #        none
                                                                                                                                                                                                                                                                

#vies
#nb3 = #nombre de vie
                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                #~ = #symbole pour le vie, equivalent d'un coeur


#nom
#def askName():
    

#player = X
