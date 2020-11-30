
'''
2d list size of window
get and put pixel
# for TP1
    # sand dropping
    #   perfect physics
    #   figure out colours
    #   other types of sand?

    #is the info toggle box bad? I want it to be in every mode
    #style and numbers?
    #the fucking sand dropping, ew
    #use pixels
    #class attribute at 1
    #make sure sand never gets stuck
    #use dx/dy to calculate the "shower effct" of the sand particles
'''

import math, copy, random
from cmu_112_graphics import *
from dataclasses import make_dataclass

#testing with radius 10 circles instead of small circles or pixels

Sand = make_dataclass('Sand',['tag','x','y','color'])

def appStarted(app):
    app.tag = 0
    app.sand = []

def mousePressed(app,event):
    if inBox(app, event.x, event.y) and notOverlappingAnyOthers(app, event.x, event.y):
        newSand = Sand(tag = app.tag, x = event.x, y = event.y, color = "black")
        app.sand.append(newSand)
        app.tag += 1
def mouseDragged(app,event):
    if inBox(app, event.x, event.y) and notOverlappingAnyOthers(app, event.x, event.y):
        newSand = Sand(tag = app.tag, x = event.x, y = event.y, color = "black")
        app.sand.append(newSand)
        app.tag += 1       


def inBox(app,x,y):
    if (20 < y < app.height - 20) and (20 < x < app.width - 20):
        return True
def notOverlappingAnyOthers(app,x,y):
    for grains in app.sand:
        #this is janky
        if grains.x == x and grains.y == y: return True
        if overlap(grains.x, grains.y, x, y):
            return False
    return True
def overlap(gx,gy,x,y):
    return ( (gx - x)**2 + (gy - y)**2 )**.5  <= 20*.75


def moveParticle(app):
    for grains in app.sand:
        if inBox(app, grains.x, grains.y) and notOverlappingAnyOthers(app,grains.x,grains.y):# and 
            grains.y += 1

def timerFired(app):
    moveParticle(app)

def redrawAll(app, canvas):
    for grains in app.sand:
        canvas.create_oval(grains.x - 10, grains.y - 10, grains.x + 10, grains.y + 10)

#runApp(width=400, height=400)
