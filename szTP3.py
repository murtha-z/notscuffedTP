#################################################
# Term Project
# Name: Shelly Zhang (shzhang)
# Section: 2
# TP Mentor: Patrick Huang
# Date: 30 November
# Approx Line Count: --
#################################################
from cmu_112_graphics import *
import math, copy, string, random
#################################################
#SAND IMPLEMENTATION TEST
'''
from sandTest4 import *
'''
#################################################
# for TP1
    # sand dropping
    #   perfect physics
    #   static + changing colors
    #   +concrete or smth

    #   info toggle on every mode?I want it to be in every mode
    #       use another file possibly

    #Patrick:
    #use pixels
    #Ping-ya:
    #class attribute at 1
    #make sure sand never gets stuck
    #use dx/dy to calculate the "shower effct" of the sand particles
#################################################

#pixel sand in sandTest4

#TODO: THREE DIFF TYPES OF STUFF: CREATIVE SANDBOX, PLAY-LEVEL SANDBOX, AND LEVEL-CREATE SANDBOX



class startScreen(Mode):
    #words and strings, UI components
    uiText = {  "aboveTitle": "._.", 
                "titleMessage": "A Sandbox Game",
                "startNew":"New Project ('n')",
                "profiles":"Old Projects ('o')",
                "info":"Press 'i' for Info",
                "textCol":"white",
                "buttonCol":"grey",
                   }

    def appStarted(mode):
        # sizing, dynamic
        mode.titleFont = f"Times {int(min(mode.width, mode.height)//20)} bold"
        mode.buttonFont = f"Times {int(min(mode.width, mode.height)//30)} bold"

        mode.width5th = mode.width // 5
        mode.height6th = mode.height // 6
        mode.widthMid = mode.width // 2
        #info toggled off
        mode.drawInfo = False

    def mousePressed(mode, event):
        x, y = event.x, event.y
        bWidthLeft = mode.width5th * 1.5
        bWidthRight = mode.width5th * 3.5
        height6th = mode.height6th
        widthMid = mode.widthMid
        margin = 0.4

        #buttons/UI
        if mode.drawInfo == False:
            if (    (bWidthLeft <= x <= bWidthRight) and 
                    (height6th*(3-margin) <= y <= height6th*(3+margin)) ):
                mode.app.setActiveMode(mode.app.newProjectMenu)
            if (    (bWidthLeft <= x <= bWidthRight) and 
                    (height6th*(4-margin) <= y <= height6th*(4+margin)) ):
                mode.app.setActiveMode(mode.app.oldProjectMenu)
            if (    (bWidthLeft <= x <= bWidthRight) and 
                    (height6th*(5-margin) <= y <= height6th*(5+margin)) ):
                mode.drawInfo = True #info button
        else:   mode.drawInfo = False

    def keyPressed(mode, event):
        #new project
        if event.key == 'n':    mode.app.setActiveMode(mode.app.newProjectMenu)
        #old project
        elif event.key == 'o':  mode.app.setActiveMode(mode.app.oldProjectMenu)
        #to sandbox (will be removed)
        elif event.key == 's':  mode.app.setActiveMode(mode.app.sandBoxMode)
        #info toggle
        elif event.key == 'i':  mode.drawInfo = not mode.drawInfo              

    def redrawAll(mode, canvas):
        #needs to be here for re-scaleability
        width5th = mode.width // 5
        height6th = mode.height // 6
        widthMid = mode.width // 2

        #buttons
        canvas.create_rectangle(    width5th, height6th, 
                                    width5th * 4, height6th * 2, 
                                    fill = startScreen.uiText["buttonCol"], 
                                    outline = startScreen.uiText["buttonCol"])
        canvas.create_rectangle(    width5th * 1.5, height6th * 2.6, 
                                    width5th * 3.5, height6th * 3.4, 
                                    fill = startScreen.uiText["buttonCol"], 
                                    outline = startScreen.uiText["buttonCol"])
        canvas.create_rectangle(    width5th * 1.5, height6th * 3.6, 
                                    width5th * 3.5, height6th * 4.4, 
                                    fill = startScreen.uiText["buttonCol"], 
                                    outline = startScreen.uiText["buttonCol"])
        canvas.create_rectangle(    width5th * 1.5, height6th * 4.6, 
                                    width5th * 3.5, height6th * 5.4,
                                    fill = startScreen.uiText["buttonCol"], 
                                    outline = startScreen.uiText["buttonCol"])
        #button text
        canvas.create_text( widthMid, height6th, 
                            text = startScreen.uiText["aboveTitle"], 
                            anchor = "s", 
                            fill = startScreen.uiText["buttonCol"], 
                            font = mode.titleFont) #prolly not needed ?
        canvas.create_text( widthMid, height6th + (.5 * height6th), 
                            text = startScreen.uiText["titleMessage"], 
                            fill = startScreen.uiText["textCol"],
                            font = mode.titleFont)
        canvas.create_text( widthMid, height6th * 3, 
                            text = startScreen.uiText["startNew"],
                            fill = startScreen.uiText["textCol"], 
                            font = mode.buttonFont)
        canvas.create_text( widthMid, height6th * 4, 
                            text = startScreen.uiText["profiles"],
                            fill = startScreen.uiText["textCol"], 
                            font = mode.buttonFont)
        canvas.create_text( widthMid, height6th * 5, 
                            text = startScreen.uiText["info"], 
                            fill = startScreen.uiText["textCol"],
                            font = mode.buttonFont)
        #info toggle box
        if mode.drawInfo:
            canvas.create_rectangle(mode.width * .1, mode.height * .1, mode.width * .9, mode.height * .9, fill = "black")
            canvas.create_text(mode.width // 2, mode.height // 3, text = "INFORMATION HERE- press 'i'", font = "Times 28 bold", fill = "white")
            canvas.create_text(mode.width // 2, mode.height // 2, text = "ex. Press 'm' to return to this menu from other screens\n& 's' to go directly to the sand", font = "Times 20 bold", fill = "white")
        #TAG
        canvas.create_text(mode.width, mode.height, text = "SANDBOX MENU", anchor = "se", font = "Times")
 





class menuNew(Mode):
    goBack = ["Back to Menu", "grey", 100, 60, "Times"]
    
    def appStarted(mode):
        #"standard" font here
        mode.font = min(mode.width, mode.height) // 20

    def keyPressed(mode,event):
        #to main menu
        if event.key == 'm':    mode.app.setActiveMode(mode.app.mainMenuMode)
        #to sandbox
        elif event.key == 's':  mode.app.setActiveMode(mode.app.sandBoxMode)
        #info popup?: elif event.key == 'i': pass

    def mousePressed(mode,event):
        x,y = event.x, event.y
        if (0 <= x <= menuNew.goBack[2]) and (0 <= y <= menuNew.goBack[3]):
            mode.app.setActiveMode(mode.app.mainMenuMode)
        else: #sandbox
            mode.app.setActiveMode(mode.app.sandBoxMode)


    def redrawAll(mode, canvas):

        #go back to main menu button
        canvas.create_rectangle(0, 0, menuNew.goBack[2], menuNew.goBack[3], fill = menuNew.goBack[1], outline = menuNew.goBack[1])
        canvas.create_text(menuNew.goBack[2]//2, menuNew.goBack[3]//2, text = menuNew.goBack[0], font = menuNew.goBack[4])
        #TAG
        canvas.create_text(mode.width, mode.height, text = "NEW PROFILE", anchor = "se", font = "Times")
        #TEMPORARY
        canvas.create_text(mode.width//2, mode.height//2, text = "click anywhere for sandbox\n[NEW PROJECT PAGE]", font = "Times 28")






class menuProfiles(Mode):
    goBack = ["Back to Menu", "grey", 100, 60, "Times"]
    
    def appStarted(mode):
        #"standard" font here
        mode.font = min(mode.width, mode.height) // 20

    def keyPressed(mode,event):
        #to main menu
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.mainMenuMode)
        #to sandbox
        elif event.key == 's':
            mode.app.setActiveMode(mode.app.sandBoxMode)
        #info popup?: elif event.key == 'i': pass
    
    def mousePressed(mode,event):
        x,y = event.x, event.y
        if (0 <= x <= menuProfiles.goBack[2]) and (0 <= y <= menuProfiles.goBack[3]):
            mode.app.setActiveMode(mode.app.mainMenuMode)
        else: #sandbox
            mode.app.setActiveMode(mode.app.sandBoxMode)

    def redrawAll(mode, canvas):

        #go back to main menu button
        canvas.create_rectangle(0, 0, menuProfiles.goBack[2], menuProfiles.goBack[3], fill = menuProfiles.goBack[1], outline = menuProfiles.goBack[1])
        canvas.create_text(menuProfiles.goBack[2]//2, menuProfiles.goBack[3]//2, text = menuProfiles.goBack[0], font = menuProfiles.goBack[4])
        #TAG
        canvas.create_text(mode.width, mode.height, text = "OLD PROFILES", anchor = "se", font = "Times")
        #TEMPORARY
        canvas.create_text(mode.width//2, mode.height//2, text = "click anywhere for sandbox\n[NEW PROJECT PAGE]", font = "Times 28")
 






class SandboxingTime(Mode):
    preSetCols = [  "misty rose", "navajo white", "pale goldenrod", 
                    "dark sea green", "LightSkyBlue1", "lavender", "black" ]

    def appStarted(mode):
        #starting sand color
        mode.sandColor = SandboxingTime.preSetCols[random.randint(0,6)]
        #TODO: rgb, separate bloc

    def keyPressed(mode,event):
        #main menu key
        if event.key == 'm':    mode.app.setActiveMode(mode.app.mainMenuMode)
        #TODO: info popup?: elif event.key == 'i':    pass

    #TODO: in sandbox Classes?    
    def mousePressed(mode, event):
        x,y = event.x, event.y


        #COLOR PICKING
        #WORKS, BAD STYLE THO? SEE REDRAWALL
        width10th = mode.width // 10 
        height10th = mode.height // 10
        titleSize = mode.width // 25

        topx = width10th * .5
        topy = height10th * 2
        botx = width10th * 7.5
        boty = height10th * 9.5
        
        coltopy = height10th * 1.25
        colboty = height10th * 1.75
        #colmidy = height10th * 1.5
        #static color picking
        if (    (topx <= x <= topx+width10th)
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[0]
        if (    (topx + width10th <= x <= topx+width10th*2)
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[1]
        if (    (topx+width10th*2 <= x <= topx+width10th*3)
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[2]
        if (    (topx+width10th*3 <= x <= topx+width10th*4) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[3]
        if (    (topx+width10th*4 <= x <= topx+width10th*5) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[4]
        if (    (topx+width10th*5 <= x <= topx+width10th*6) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[5]
        if (    (topx+width10th*6 <= x <= topx+width10th*7) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[6]

        #TODO: mousePressed in the boxes SAND TIME?
        pass
    def mouseDragged(mode, event):
        pass

    def redrawAll(mode, canvas):
        width10th = mode.width // 10 
        height10th = mode.height // 10
        titleSize = mode.width // 25

        #sandbox Main
        topx = width10th * .5
        topy = height10th * 2
        botx = width10th * 7.5
        boty = height10th * 9.5
        #Color Picker
        coltopy = height10th * 1.25
        colboty = height10th * 1.75
        colmidy = height10th * 1.5

        #sandbox boxes and text
        canvas.create_rectangle(topx, topy, botx, boty, fill = "gainsboro") 
        canvas.create_text(     topx, coltopy, text = "sandbox", 
                                anchor = "sw", font = f"Times {titleSize}") 
        #color selecting UI boxes
        canvas.create_rectangle(    topx, coltopy, topx+width10th, colboty, 
                                    fill = SandboxingTime.preSetCols[0])
        canvas.create_rectangle(    topx + width10th, coltopy, 
                                    topx+width10th*2, colboty, 
                                    fill = SandboxingTime.preSetCols[1])
        canvas.create_rectangle(    topx + width10th*2, coltopy, 
                                    topx+width10th*3, colboty, 
                                    fill = SandboxingTime.preSetCols[2])
        canvas.create_rectangle(    topx + width10th*3, coltopy, 
                                    topx+width10th*4, colboty, 
                                    fill = SandboxingTime.preSetCols[3])
        canvas.create_rectangle(    topx + width10th*4, coltopy, 
                                    topx+width10th*5, colboty, 
                                    fill =  SandboxingTime.preSetCols[4])
        canvas.create_rectangle(    topx + width10th*5, coltopy, 
                                    topx+width10th*6, colboty, 
                                    fill = SandboxingTime.preSetCols[5])
        canvas.create_rectangle(    topx + width10th*6, coltopy, 
                                    topx+width10th*7, colboty, 
                                    fill = SandboxingTime.preSetCols[6])
        #color selecting Labels
        labelFont = f"Times {int(titleSize//3)}"
        canvas.create_text( topx + .5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[0], 
                            font = labelFont)
        canvas.create_text( topx + 1.5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[1], 
                            font = labelFont)
        canvas.create_text( topx + 2.5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[2], 
                            font = labelFont)
        canvas.create_text( topx + 3.5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[3], 
                            font = labelFont)
        canvas.create_text( topx + 4.5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[4], 
                            font = labelFont)
        canvas.create_text( topx + 5.5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[5], 
                            font = labelFont)
        canvas.create_text( topx + 6.5*width10th, colmidy, 
                            text = SandboxingTime.preSetCols[6], 
                            font = labelFont, fill = "white")
        #TAG
        canvas.create_text(mode.width, mode.height, text = "SANDBOX", anchor = "se", font = "Times")
 

#TODO: the different modes of playing?
class creativeSandbox(SandboxingTime):
    pass
class playLevelSandbox(SandboxingTime):
    pass
class levelCreateSandbox(SandboxingTime):
    pass



class SandBoxModes(ModalApp):
    def appStarted(app):
        app.mainMenuMode = startScreen()
        app.newProjectMenu = menuNew()
        app.oldProjectMenu = menuProfiles()
        app.sandBoxMode = SandboxingTime()
        app.setActiveMode(app.mainMenuMode)
        #app.timerDelay = 50

app = SandBoxModes(width=800, height=600)
