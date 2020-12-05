#TODO:make file with profile name
#profile holds:    endless amount of pieces (named and in creation state)
#                   all the preset levels (number names)
#                   levels added (number names)


#context manager (otherwise need to close file)
#f = open('text.txt', 'r')
#           (name, mode)

#IS IT ALL DESTRUCTIVE?
with open('text.txt', 'r') as f:
    pass
    #print("\n\nREAD")
    #loads everything into memory
    #f_contents = f.read()
    #print(f_contents)

    #print("\n\nREADLINES:")
    #if it's a string with newlines and shit
    #returns list of all lines in file
    #fc = f.readlines()
    #print(fc)# (..., end = "")

    #print("\n\nREADLINE")
    #f = f.readline() #each call returns the next
    #print(f)

#all the contents from file at once
with open('text.txt', 'r') as g:
    pass
    #for line in g:
    #    print(line,end="")

#more control
with open("text.txt", 'r') as h:
    pass
    #h_contents = h.read(100) #first 100 chars (no discrimination and each call returns the next)
    #print(h_contents) #at the end, it'll return an empty string

#loop over small chunks to find stuff 
with open("text.txt", 'r') as i:
    sizeToRead = 100
    iContents = i.read(sizeToRead)

    print(i.tell()) #100
   
    #while len(iContents) > 0:
    #    print(iContents, end="")
    #    iContents = i.read(sizeToRead)








'''

        cols = 3
        height10th = abs(boty - topy) // 10
        widthFract = abs(botx - topx) // cols
        x1 = topx
        x2 = botx
        y1 = topy
        y2 = boty
        addHeight = height10th
        addWidth = widthFract
        for x in range(cols):
            for y in range(10):
                canvas.create_rectangle(x1,y1,x2 + addWidth*(x),y1 + addHeight)
                addHeight += height10th
            x1 += addWidth
            x2 += addWidth

'''
import math, copy, random
from cmu_112_graphics import *
from dataclasses import make_dataclass

def redrawAll(app, canvas):
    cols = 3
    rows = 10
    colWidth = app.width // cols
    rowHeight = app.height // rows
    x1 = 0
    y1 = 0
    x2 = colWidth
    y2 = rowHeight
    for col in range(cols):
        for row in range(rows):
            canvas.create_rectangle(x1,y1,x2,y2)
            y1 += rowHeight
            y2 += rowHeight
        y1 = 0
        y2 = rowHeight
        
        x1 += colWidth
        x2 += colWidth

runApp(width=400, height=400)
