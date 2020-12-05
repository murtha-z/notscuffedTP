import math, copy, random
from cmu_112_graphics import *
from dataclasses import make_dataclass

# angle of "shower"
#   from trig?
# game over if no movement for 5 sec == clicking done with sand button on app

Sand = make_dataclass('Sand',['tag','x','y', 'lasty', 'color','falling'])

def appStarted(app):
    app.grad = 7
    app.tag = 0
    app.everything = []
    app.sand = []
    app.nonMovingSand = []
    app.timerDelay = 2
    #app.stoppedFalling = False
    #app.gameOver = True

def mousePressed(app,event):
    #    if app.gameOver: return not needed right?
    if inBox(app, event.x, event.y) and notOverlappingAnyOthers(app, event.x, event.y):
        newSand = Sand(tag = app.tag, x = event.x, y = event.y, lasty = event.y, color = "black", falling = True)
        app.sand.append(newSand)
        app.tag += 1
def mouseDragged(app,event):
    if inBox(app, event.x, event.y) and notOverlappingAnyOthers(app, event.x, event.y):
        newSand = Sand(tag = app.tag, x = event.x, y = event.y, lasty = event.y, color = "black", falling = True)
        app.sand.append(newSand)
        app.tag += 1       


def inBox(app,x,y):
    if (20 < y < app.height - 20) and (20 < x < app.width - 20):
        return True
def notOverlappingAnyOthers(app,x,y):
    for grains in app.nonMovingSand: #this slows everything down again
    #for grains in app.sand:
        #this is janky
        if grains.x == x and grains.y == y: return True
        if overlap(app, grains.x, grains.y, x, y):
            return False
    return True
def overlap(app,gx,gy,x,y):
    tooClose = ( (gx - x)**2 + (gy - y)**2 )**.5  <= (app.grad*2)
    #TODO: if 50% overlap, otherwise if it's like this on the x axis just keep going, 
    return tooClose
    '''
def onlySides(app,gx,gy):
    for grains in app.nonMovingSand:
        if 
'''

def moveParticle(app):
    app.everything = app.sand + app.nonMovingSand
    for g in range(len(app.sand)):
        grains = app.sand[g]
        #if inBox(app, grains.x, grains.y) and (onlySides(app,grains.x,grains.y) or notOverlappingAnyOthers(app, grains.x, grains.y)):
        if inBox(app, grains.x, grains.y) and (notOverlappingAnyOthers(app, grains.x, grains.y)):
            grains.y += 1
        else:
            app.nonMovingSand.append(grains)
    for g in app.nonMovingSand:
        if g in app.sand:
            sandIndex = app.sand.index(g)
            app.sand.pop(sandIndex)
            '''
            if grains.lasty != grains.y:
                grains.lasty = grains.y
            else:
                print("Hello")
                app.nonMovingSand.append(grains)
    for g in app.nonMovingSand:
        if g in app.sand:
            sandIndex = app.sand.index(g)
            app.sand.pop(sandIndex)
            '''

def timerFired(app):
    moveParticle(app)

def redrawAll(app, canvas):
    for grains in app.sand:
        canvas.create_oval(grains.x - app.grad, grains.y - app.grad, grains.x + app.grad, grains.y + app.grad, fill = grains.color)
    for grains in app.nonMovingSand:
        canvas.create_oval(grains.x - app.grad, grains.y - app.grad, grains.x + app.grad, grains.y + app.grad, fill = "red", outline = "red")
    print(len(app.sand), len(app.nonMovingSand))
runApp(width=400, height=400)
