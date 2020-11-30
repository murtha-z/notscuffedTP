import math, copy, random
from cmu_112_graphics import *
from dataclasses import make_dataclass

#for trig "shower effect" (Ping-ya says dy/dx): https://www.studytonight.com/post/trigonometric-function-in-python# 
#NOTE: blah blah smth static method (remember)
#helpful: https://stackabuse.com/saving-text-json-and-csv-to-a-file-in-python/


#Nine doesnt mean anything right now, it's a tag maybe and white is color
def make2dList(rows, cols):
    return [ ([None] * cols) for row in range(rows) ]

def appStarted(app):
    app.sand = make2dList(app.height, app.width)
    app.tag = 0
    app.color = "red"

def mousePressed(app,event):
    if inBox(app, event.x, event.y):# and notOverlappingAnyOthers(app, event.x, event.y):
        app.sand[event.x][event.y] = (app.tag,app.color)
        app.tag += 1


def inBox(app,x,y):
    return True
    #if (20 < y < app.height - 20) and (20 < x < app.width - 20):
    #    return True
    '''
def notOverlappingAnyOthers(app,x,y):
    for grains in app.sand:
        #jank here?
        if overlap(grains.x, grains.y, x, y):
            return False
    return True
def overlap(gx,gy,x,y):
    return gx != x or gy != y
'''
def redrawAll(app,canvas):
    for grains in range(len(app.sand)):
        for rains in range(len(grains)):
            print(rains)
            #canvas.create_oval(grains.x-1, grains.y-1, grains.x+1, grains.y+1)


runApp(width = 10, height = 10)
