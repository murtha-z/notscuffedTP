#################################################
# Term Project
# Name: Shelly Zhang (shzhang)
# Section: 2
# TP Mentor: Patrick Huang
# Date: 29 November
# Approx Line Count: ~250 here and ~50+ in sand test.py
#################################################
from cmu_112_graphics import *
import math, copy, string, random
#################################################
#SAND IMPLEMENTATION TEST

#from sandTest3 import *

#################################################
# for TP1
    # sand dropping
    #   perfect physics
    #   figure out colours
    #   other types of sand?

    #is the info toggle box bad? I want it to be in every mode
    #style and numbers?
    #the fucking sand dropping, help
    #use pixels
    #class attribute at 1
    #make sure sand never gets stuck
    #use dx/dy to calculate the "shower effct" of the sand particles
#################################################
 
#all strings cleaned up
#fix info box in splash screen
#sand rudimentarily integrated with cols
#pixel sand in sandTest4




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
        #font sizing, dynamic
        mode.titleFont = f"Times {int(mode.width//20)} bold"
        mode.buttonFont = f"Times {int(mode.width//30)} bold"
        #info toggled off 
        #TODO: toggling off the info page not just clicking the button area again, use if statement
        mode.drawInfo = False

    def mousePressed(mode, event):
        #no mouse pressed rn thanks, keypresses now
        #TODO: buttons?
        mode.width5th = mode.width // 5
        mode.height6th = mode.height // 6
        mode.widthMid = mode.width // 2
        x, y = event.x, event.y
        if (mode.width5th * 1.5 <= x <= mode.width5th * 3.5) and (mode.height6th * 2.6 <= y <= mode.height6th * 3.4):
            #print("pressed the first button")
            mode.app.setActiveMode(mode.app.newProjectMenu)
        if (mode.width5th * 1.5 <= x <= mode.width5th * 3.5) and (mode.height6th * 3.6 <= y <= mode.height6th * 4.4):
            #print("pressed the second button")
            mode.app.setActiveMode(mode.app.oldProjectMenu)
        if (mode.width5th * 1.5 <= x <= mode.width5th * 3.5) and (mode.height6th * 4.6 <= y <= mode.height6th * 5.4):
            #print("pressed the INFO button")
            if not mode.drawInfo:
                mode.drawInfo = True        
        #else:
        #    print(f'mousePressed at {(event.x, event.y)}')

    def keyPressed(mode, event):
        #new project
        if event.key == 'n':    mode.app.setActiveMode(mode.app.newProjectMenu)
        #old project
        elif event.key == 'o':  mode.app.setActiveMode(mode.app.oldProjectMenu)
        #to sandbox (will be removed)
        elif event.key == 's':  mode.app.setActiveMode(mode.app.sandBoxMode)
        #info toggle
        elif event.key == 'i':  mode.drawInfo = not mode.drawInfo              
        #else:
        #    print(f'key {event.key} does nothing : ]')

    def redrawAll(mode, canvas):
        #just the outline of where i want the ui to go later
        mode.width5th = mode.width // 5
        mode.height6th = mode.height // 6
        mode.widthMid = mode.width // 2

        width5th = mode.width5th
        height6th = mode.height6th
        widthMid = mode.widthMid

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
                            #
                            text = startScreen.uiText["aboveTitle"], 
                            anchor = "s", 
                            fill = startScreen.uiText["buttonCol"], 
                            font = mode.titleFont) #prolly not needed ?
        canvas.create_text( widthMid, height6th + (.5 * height6th), 
                            #
                            text = startScreen.uiText["titleMessage"], 
                            fill = startScreen.uiText["textCol"],
                            font = mode.titleFont)
        canvas.create_text( widthMid, height6th * 3, 
                            #
                            text = startScreen.uiText["startNew"],
                            fill = startScreen.uiText["textCol"], 
                            font = mode.buttonFont)
        canvas.create_text( widthMid, height6th * 4, 
                            #
                            text = startScreen.uiText["profiles"],
                            fill = startScreen.uiText["textCol"], 
                            font = mode.buttonFont)
        canvas.create_text( widthMid, height6th * 5, 
                            #
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
    def mousePressed(mode,event):
    #temporary thru to sandboxing
        mode.app.setActiveMode(mode.app.sandBoxMode)
    
    def appStarted(mode):
        pass
    def keyPressed(mode,event):
        #to main menu
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.mainMenuMode)
        #to sandbox
        elif event.key == 's':
            mode.app.setActiveMode(mode.app.sandBoxMode)
        #info popup
        elif event.key == 'i':
            pass
    def redrawAll(mode, canvas):
        #canvas.create_text(mode.width//2, mode.height//2, text = "first button (n): new project")
        #TAG
        canvas.create_text(mode.width, mode.height, text = "NEW PROFILE", anchor = "se", font = "Times")
        #TEMPORARY
        canvas.create_text(mode.width//2, mode.height//2, text = "click for sandbox / m to go back\n[NEW PROJECT PAGE]", font = "Times 28")






class menuProfiles(Mode):
    def mousePressed(mode,event):
    #temporary thru to sandboxing
        mode.app.setActiveMode(mode.app.sandBoxMode)
    
    def appStarted(mode):
        pass
    def keyPressed(mode,event):
        #to main menu
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.mainMenuMode)
        #to sandbox
        elif event.key == 's':
            mode.app.setActiveMode(mode.app.sandBoxMode)
        #info popup
        elif event.key == 'i':
            pass
    
    def redrawAll(mode, canvas):
        #canvas.create_text(mode.width//2, mode.height//2, text = "second button (o): old project")
        #TAG
        canvas.create_text(mode.width, mode.height, text = "OLD PROFILES", anchor = "se", font = "Times")
        #TEMPORARY
        canvas.create_text(mode.width//2, mode.height//2, text = "click for sandbox / m to go back\n[NEW PROJECT PAGE]", font = "Times 28")
 






class SandboxingTime(Mode):
    preSetCols = [  "misty rose", "navajo white", "pale goldenrod", 
                    "dark sea green", "LightSkyBlue1", "lavender", "black" ]

    def appStarted(mode):
        #TODO: rgb, separate bloc
        pass

    def keyPressed(mode,event):
        #main menu key
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.mainMenuMode)
        #TODO: info popup
        #info toggle like main menu?
        elif event.key == 'i':
            pass
    
    def mousePressed(mode, event):
        #mousePressed in the boxes
        pass
    def mouseDragged(mode, event):
        pass


    def redrawAll(mode, canvas):
        width10th = mode.width // 10 
        height10th = mode.height // 10
        coltopy = height10th * 1.25
        colboty = height10th * 1.75
        colmidy = height10th * 1.5
        topx = width10th * .5
        topy = height10th * 2
        botx = width10th * 7.5
        boty = height10th * 9.5
        titleSize = mode.width // 25
        canvas.create_rectangle(topx, topy, botx, boty) 
        canvas.create_text(topx, coltopy, text = "sandbox", anchor = "sw", font = f"Times {titleSize}") 
        #color selecting UI boxes
        canvas.create_rectangle(topx, coltopy, topx+width10th, colboty, fill = SandboxingTime.preSetCols[0])
        canvas.create_rectangle(topx + width10th, coltopy, topx+width10th*2, colboty, fill = SandboxingTime.preSetCols[1])
        canvas.create_rectangle(topx + width10th*2, coltopy, topx+width10th*3, colboty, fill = SandboxingTime.preSetCols[2])
        canvas.create_rectangle(topx + width10th*3, coltopy, topx+width10th*4, colboty, fill = SandboxingTime.preSetCols[3])
        canvas.create_rectangle(topx + width10th*4, coltopy, topx+width10th*5, colboty, fill =  SandboxingTime.preSetCols[4])
        canvas.create_rectangle(topx + width10th*5, coltopy, topx+width10th*6, colboty, fill = SandboxingTime.preSetCols[5])
        canvas.create_rectangle(topx + width10th*6, coltopy, topx+width10th*7, colboty, fill = SandboxingTime.preSetCols[6])
        #color selecting Labels
        canvas.create_text(topx + .5*width10th, colmidy, text = SandboxingTime.preSetCols[0], font = f"Times {int(titleSize//3)}")
        canvas.create_text(topx + 1.5*width10th, colmidy, text = SandboxingTime.preSetCols[1], font = f"Times {int(titleSize//3)}")
        canvas.create_text(topx + 2.5*width10th, colmidy, text = SandboxingTime.preSetCols[2], font = f"Times {int(titleSize//3)}")
        canvas.create_text(topx + 3.5*width10th, colmidy, text = SandboxingTime.preSetCols[3], font = f"Times {int(titleSize//3)}")
        canvas.create_text(topx + 4.5*width10th, colmidy, text = SandboxingTime.preSetCols[4], font = f"Times {int(titleSize//3)}")
        canvas.create_text(topx + 5.5*width10th, colmidy, text = SandboxingTime.preSetCols[5], font = f"Times {int(titleSize//3)}")
        canvas.create_text(topx + 6.5*width10th, colmidy, text = SandboxingTime.preSetCols[6], font = f"Times {int(titleSize//3)}")
        #TAG
        canvas.create_text(mode.width, mode.height, text = "SANDBOX", anchor = "se", font = "Times")
 

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
