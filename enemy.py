import sys
import Field
import os
import Field

def create (color, Y):
    e=dict()
    e["color"]=color
    e["y"]= Y
    e["x"]= X
    
    return e

def getY(e):
    return e['y']
def setY(e,y):
    e['y']=y 

def getX(e):
    return e['x']
def setX(e, x):
    e['x']=x

def move(e,y,field):   #A REVOIR 
    y = e['y'] + y

def getColor(e):
    return e['color']
def setColor(e,c):
    e['color']=c
    
def show(e):
    sys.stdout.write("\033[40m")
    
    c = e["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)
    
#collision enemy-zone
def CollisionEZ(e,y):
    x=int(y)
#    if e['y'] <= y and y < e['y']


#definir la vitesse vy
