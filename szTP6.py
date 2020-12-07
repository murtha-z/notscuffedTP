#################################################
# Term Project
# Name: Shelly Zhang (shzhang)
# Section: 2
# TP Mentor: Patrick Huang
# Date: 6 December
# Approx Line Count: ~800
#################################################
from cmu_112_graphics import *
import math, copy, string, random, os
from dataclasses import make_dataclass
#################################################
print("\n *************THE FOLLOWING IS PRINTED:*************")

#MAIN MENU, STARTING SCREEN
class startScreen(Mode):
    goBack = ["Back to Menu", "grey", 100, 60, "Times"]
    #words and strings, UI components
    uiText = {  "aboveTitle": "._. by shelly ._.", 
                "titleMessage": "A Sandbox Game",
                "startNew":"New Profile",
                "profiles":"Old Profile",
                "info":"Info ('i')",
                "textCol":"white",
                "buttonCol":"grey",
                   }
    #THE MOST IMPORTANT THING:
    #THE PATH TO THE FILE WE WRITE/READ
    thePath = None
    def appStarted(mode):
        # sizing, dynamic
        mode.titleFont = f"Times {int(min(mode.width, mode.height)//20)} bold"
        mode.buttonFont = f"Times {int(min(mode.width, mode.height)//30)} bold"

        mode.width5th = mode.width // 5
        mode.height6th = mode.height // 6
        mode.widthMid = mode.width // 2
        #toggleable stuff
        mode.drawInfo = False           #info toggled off
        mode.showProfileList = False    #File shit

        #mode.fileOpen = startScreen.singularFilePath
        mode.firstLine = None
        mode.profileExists = False
    def makeAndOpenFile(mode, path):
        with open(path, 'w+') as mode.fileOpen:
            #mode.fileOpen.write(path)
            mode.fileOpen.write(path + " I wrote in this file")
            #ASSIGN PATH TO VARIABLE
            startScreen.thePath = path




    #get cell for old profiles
    def getCell(mode, x, y, numberOfProfiles, listOfProfiles):
        topx = mode.width * .1
        topy = mode.height * .1
        botx = mode.width * .9
        boty = mode.height * .9
        #ADJUSTABLE / EXPANDABLE BOX UI FOR PROFILES
        rows = 10 #set number of 10
        cols = math.ceil(numberOfProfiles / rows)

        colWidth = abs(botx - topx) // cols
        rowHeight = abs(boty - topy) // rows

        marginWidth = mode.width * .1
        marginHeight = mode.height * .1
        
        if not (marginWidth <= x <= mode.width - marginWidth) or not (marginHeight <= y <= mode.height - marginHeight):
            #print("margin")
            return(None, None)
        else:
            mouseClickRow = int((y - marginHeight) / rowHeight)
            mouseClickCol = int((x - marginWidth) / colWidth)
            return (mouseClickRow, mouseClickCol)      
    def getFileNameFromCell(mode, row, col):
        listOfProfiles = os.listdir("Profiles")
        if len(listOfProfiles) < 10:
            numberOfProfiles = 10
        else: 
            numberOfProfiles = len(listOfProfiles)
        rows = 10
        cols = math.ceil(numberOfProfiles / rows)

        listIndex = (row) + (col*10)
        if listIndex < len(listOfProfiles):
            stringTxt = listOfProfiles[listIndex]
        else:
            stringTxt = "Should Do Nothing"
            pass
        #print(stringTxt)
        #stringTxt = "Function for getFileNameFromCell is not written yet"
        return stringTxt

    #MOUSE CONTROL
    def newProfileMousePressed(mode):    
        newProfileName = mode.getUserInput("New Profile!\nPlease, your name:")
        #newProfileName = "text"
        if not os.path.exists(f'Profiles/{newProfileName}.txt'):
            startScreen.makeAndOpenFile(mode, f'Profiles/{newProfileName}.txt')
            #print("should open this new file")
            mode.app.setActiveMode(mode.app.newProjectMenu)
            #print('onto next screen')
        else:
            # couldn't get showMessage to work
            mode.profileExists = True
            #print("Profile Exists already, back to the menu")   
    def normalMousePressed(mode, x, y):
        #needed for resizability :-((
        mode.width5th = mode.width // 5
        mode.height6th = mode.height // 6
        mode.widthMid = mode.width // 2
        #values for button params
        bWidthLeft = mode.width5th * 1.5
        bWidthRight = mode.width5th * 3.5
        height6th = mode.height6th
        widthMid = mode.widthMid
        margin = 0.4
        #FIRST BUTTON
        if (    (bWidthLeft <= x <= bWidthRight) and 
                (height6th*(3-margin) <= y <= height6th*(3+margin)) ):
            startScreen.newProfileMousePressed(mode)#NEW PROFILE Created
        #SECOND BUTTON
        if (    (bWidthLeft <= x <= bWidthRight) and 
                (height6th*(4-margin) <= y <= height6th*(4+margin)) ):
            mode.showProfileList = True #profiles button
        '''
        #mode.app.setActiveMode(mode.app.oldProjectMenu)
        #TODO: transition to open up the correct text file
        '''

        #THIRD BUTTON
        if (    (bWidthLeft <= x <= bWidthRight) and 
                (height6th*(5-margin) <= y <= height6th*(5+margin)) ):
            mode.drawInfo = True #info button
    #TODO: SET UP OLD PROFILES LIST IN TXT
    #TODO: SET UP OLD PROFILES UI
    #TODO: ADD FUNCTION OF OPENING UP MODE
    def profileMousePressed(mode, x, y):
        if (0 <= x <= startScreen.goBack[2]) and (0 <= y <= startScreen.goBack[3]):
                mode.showProfileList = False #back button, go out of Profile List
        else:
            #TODO:USE A GET CELL THING
            #TODO: MAKE SMTH LIKE MODE.PROFILECELLSELECTED

            topx = mode.width * .1
            topy = mode.height * .1
            botx = mode.width * .9
            boty = mode.height * .9
            #list of folder of Profiles
            listOfProfiles = os.listdir("Profiles")
            if len(listOfProfiles) < 10:
                numberOfProfiles = 10
            else: 
                numberOfProfiles = len(listOfProfiles)
            #ADJUSTABLE / EXPANDABLE BOX UI FOR PROFILES
            rows = 10 #set number of 10
            cols = math.ceil(numberOfProfiles / rows)
            colWidth = abs(botx - topx) // cols
            rowHeight = abs(boty - topy) // rows
            x1 = topx
            y1 = topy
            x2 = colWidth + topx
            y2 = rowHeight + topy
            #Buttons for opening the text files
            
            #USE CELL AND ROW TO GET THE NAME OF THE FILE TO GET PATH
            if startScreen.getCell(mode, x, y, numberOfProfiles, listOfProfiles) != (None, None):
                mouseClickRow, mouseClickCol = startScreen.getCell(mode, x, y, numberOfProfiles, listOfProfiles)
                print(f"cell: {mouseClickRow, mouseClickCol}", "Get the name next: ", end = "")
                oldProfileName = startScreen.getFileNameFromCell(mode, mouseClickRow, mouseClickCol) #make sure not out of list
                startScreen.thePath = oldProfileName
            print(f"startScreen.thePath: {startScreen.thePath}")
            
            #GO TO OLD PROFILE UI THING
    def mousePressed(mode, event):
        x, y = event.x, event.y

        #buttons/UI for profiles and Names
        if mode.showProfileList == True:
            startScreen.profileMousePressed(mode, event.x, event.y)
        #gets rid of the UI box for profiles to exist
        elif mode.profileExists == True:
            mode.profileExists = False
        #Normal Function
        elif mode.drawInfo == False and mode.showProfileList == False:
            startScreen.normalMousePressed(mode, event.x, event.y)
        else:
            mode.drawInfo = False 
    #SOME OF THIS' FUNCTIONALITY NEEDS TO CHANGE
    def keyPressed(mode, event): #TODO: sort this out and write the info for the info page
        if event.key == 'i':  mode.drawInfo = not mode.drawInfo               #info toggle 
        '''
        if event.key == 'n':    mode.app.setActiveMode(mode.app.newProjectMenu) #new project
        elif event.key == 'o':  mode.app.setActiveMode(mode.app.oldProjectMenu) #old project
        elif event.key == 's':  mode.app.setActiveMode(mode.app.sandBoxMode)    #to sandbox (will be removed)        
        '''
    
    #UI TIME
    def mainMenuUI(mode, canvas):
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
    def toggleInfo(mode, canvas):
        canvas.create_rectangle(mode.width * .1, mode.height * .1, mode.width * .9, mode.height * .9, fill = "black")
        canvas.create_text(mode.width // 2, mode.height // 3, text = "INFORMATION HERE- press 'i'", font = "Times 28 bold", fill = "white")
        canvas.create_text(mode.width // 2, mode.height // 2, text = "ex. Press 'm' to return to this menu from other screens\n& 's' to go directly to the sand", font = "Times 20 bold", fill = "white")
    def toggleProfiles(mode, canvas):
        topx = mode.width * .1
        topy = mode.height * .1
        botx = mode.width * .9
        boty = mode.height * .9

        #list of folder of Profiles
        listOfProfiles = os.listdir("Profiles")
        if len(listOfProfiles) < 10:
            numberOfProfiles = 10
        else: 
            numberOfProfiles = len(listOfProfiles)
        #ADJUSTABLE / EXPANDABLE BOX UI FOR PROFILES
        rows = 10 #set number of 10
        cols = math.ceil(numberOfProfiles / rows)
        colWidth = abs(botx - topx) // cols
        rowHeight = abs(boty - topy) // rows
        #TITLE AND BIG BOX
        canvas.create_text((botx+topx)/2, topy, text = "Click for Old Profile", anchor = "s", font = mode.titleFont)
        canvas.create_rectangle(topx, topy, botx, boty, fill = "grey34", width = rows)
        x1 = topx
        y1 = topy
        x2 = colWidth + topx
        y2 = rowHeight + topy
        #draw boxes
        #UI buttons for keypressed later
        listTag = 0
        for col in range(cols):
            for row in range(rows):
                canvas.create_rectangle(x1,y1,x2,y2)
                if len(listOfProfiles) > listTag: #TODO: remove the stupid DS and .txt one
                    if listOfProfiles[listTag] != ".txt" or listOfProfiles[listTag] != ".DS_Store":
                        #print(listOfProfiles[listTag])
                        canvas.create_text(x1 + (.5*colWidth),y1 + (.5*rowHeight), text = listOfProfiles[listTag], fill = startScreen.uiText["buttonCol"], font = mode.titleFont)
                    listTag += 1
                y1 += rowHeight
                y2 += rowHeight
            y1, y2 = topy, rowHeight + topy
            x1 += colWidth
            x2 += colWidth
        
        #BACK TO MENU
        canvas.create_rectangle( 0, 0, startScreen.goBack[2], startScreen.goBack[3], fill = startScreen.goBack[1], outline = startScreen.goBack[1])
        canvas.create_text(startScreen.goBack[2]//2, startScreen.goBack[3]//2, text = startScreen.goBack[0], font = startScreen.goBack[4])
    def toggleProfileExistsMessage(mode, canvas):
        topx = mode.width * .1
        topy = mode.height * .1
        botx = mode.width * .9
        boty = mode.height * .9
        canvas.create_rectangle(topx, topy, botx, boty, fill = "grey34")
        canvas.create_text( (botx+topx)//2, (boty+topy)//2, text = "This Profile Exists Already\nor You Clicked 'Cancel'\n\n*either way*\n\nCLICK ANYWHERE TO CONTINUE", fill = "black", font = mode.titleFont, anchor = "center")
    def redrawAll(mode, canvas):
        startScreen.mainMenuUI(mode, canvas) #main UI stuff
        if mode.drawInfo:   startScreen.toggleInfo(mode, canvas)         #info toggle box
        if mode.showProfileList: startScreen.toggleProfiles(mode, canvas)#profile toggle box    TODO: same thing with mouse clicked
        if mode.profileExists: startScreen.toggleProfileExistsMessage(mode, canvas)
        #TAG
        canvas.create_text(mode.width, mode.height, text = "SANDBOX MENU", anchor = "se", font = "Times")
        canvas.create_text(0, mode.height, text = f"FILE OPENED: {startScreen.thePath}", anchor = "sw", font = "Times")































class menuNew(Mode):
    goBack = ["Back to Menu", "grey", 100, 60, "Times"]
    uiText = {  "sbFUN": "Creative Sandbox",
                "sbPLAY": "Play Levels",
                "sbCREATE": "Create Levels",
                "textCol":"white",
                "buttonCol":"grey",
                "title": "Menu: New Person" }
    def appStarted(mode):
        #"standard" font here
        mode.font = min(mode.width, mode.height) // 20
        mode.titleFont = f"Times {int(min(mode.width, mode.height)//20)} bold"
        #button margins
        mode.buttonPercent = .1
        mode.buttonFont = f"Times {int(min(mode.width, mode.height)//30)} bold" #repeat
    #TODO: info popup?: elif event.key == 'i': pass
    def keyPressed(mode,event):
        #to main menu
        if event.key == 'm':    mode.app.setActiveMode(mode.app.mainMenuMode)
        '''
        elif event.key == 's':  mode.app.setActiveMode(mode.app.sandBoxMode) #TODO: remove #to sandbox
        '''

    def mousePressed(mode,event):
        x,y = event.x, event.y

        width4th = mode.width // 4
        height4th = mode.height // 4
        heightMargin = mode.buttonPercent * height4th
        #back button
        if (0 <= x <= menuNew.goBack[2]) and (0 <= y <= menuNew.goBack[3]):
            mode.app.setActiveMode(mode.app.mainMenuMode)
        #button1: CREATIVE SANDBOX
        elif (width4th <= x <= width4th*3) and (height4th*1 + heightMargin <= y <= height4th*2 - heightMargin):




            mode.app.setActiveMode(mode.app.sbFUN)


        #button2: PLAY LEVELS
        elif (width4th <= x <= width4th*3) and (height4th*2 + heightMargin <= y <= height4th*3 - heightMargin):
            pass
        elif (width4th <= x <= width4th*3) and (height4th*3 + heightMargin <= y <= height4th*4 - heightMargin):
            pass
        #sandbox
        else: pass  #mode.app.setActiveMode(mode.app.sandBoxMode)

    def redrawAll(mode, canvas):
        width4th = mode.width // 4
        height4th = mode.height // 4
        heightMargin = mode.buttonPercent * height4th

        #Title
        canvas.create_text(width4th*2, (height4th*.5), font = mode.titleFont, text = menuNew.uiText["title"])
        #Button UI  #canvas.create_rectangle(width4th, height4th*0 + heightMargin, width4th*3, height4th*1 - heightMargin)
        canvas.create_rectangle(width4th, height4th*1 + heightMargin, width4th*3, height4th*2 - heightMargin, fill = menuNew.uiText["buttonCol"], outline = menuNew.uiText["buttonCol"])
        canvas.create_rectangle(width4th, height4th*2 + heightMargin, width4th*3, height4th*3 - heightMargin, fill = menuNew.uiText["buttonCol"], outline = menuNew.uiText["buttonCol"])
        canvas.create_rectangle(width4th, height4th*3 + heightMargin, width4th*3, height4th*4 - heightMargin, fill = menuNew.uiText["buttonCol"], outline = menuNew.uiText["buttonCol"])
        #ButtonText UI
        canvas.create_text(width4th*2, (height4th*1.5), font = mode.buttonFont, fill = menuNew.uiText["textCol"], text = menuNew.uiText["sbFUN"] + "\nONLY THIS ONE RN")
        canvas.create_text(width4th*2, (height4th*2.5), font = mode.buttonFont, fill = menuNew.uiText["textCol"], text = menuNew.uiText["sbPLAY"])
        canvas.create_text(width4th*2, (height4th*3.5), font = mode.buttonFont, fill = menuNew.uiText["textCol"], text = menuNew.uiText["sbCREATE"])

        #go back to main menu button
        canvas.create_rectangle(0, 0, menuNew.goBack[2], menuNew.goBack[3], fill = menuNew.goBack[1], outline = menuNew.goBack[1])
        canvas.create_text(menuNew.goBack[2]//2, menuNew.goBack[3]//2, text = menuNew.goBack[0], font = menuNew.goBack[4])
        #TAG
        canvas.create_text(mode.width, mode.height, text = "NEW PROFILE", anchor = "se", font = "Times")
        canvas.create_text(0, mode.height, text = f"file opened: {startScreen.thePath}", anchor = "sw", font = "Times")
        #TEMPORARY
        canvas.create_text(mode.width//2, mode.height//2, text = "[NEW PROJECT PAGE]\nONLY BUTTON 1 WORKS ATM", font = "Times 28")























#NOT POPULATED YET
class menuProfiles(Mode):
    goBack = ["Back to Menu", "grey", 100, 60, "Times"]
    
    def appStarted(mode):
        #"standard" font here
        mode.font = min(mode.width, mode.height) // 20

    #TODO:  #info popup?: elif event.key == 'i': pass
    def keyPressed(mode,event):
        #to main menu
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.mainMenuMode)
        '''elif event.key == 's': mode.app.setActiveMode(mode.app.sandBoxMode) #to sandbox'''
    
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
        canvas.create_text(0, mode.height, text = f"FILE OPENED: {startScreen.thePath}", anchor = "sw", font = "Times")
        #TEMPORARY
        canvas.create_text(mode.width//2, mode.height//2, text = "click anywhere for sandbox\n[NEW PROJECT PAGE]", font = "Times 28")
 

























class SandboxingTime(Mode):
    preSetCols = [  "misty rose", "navajo white", "pale goldenrod", 
                    "dark sea green", "LightSkyBlue1", "lavender", "black" ]
    
    #TODO: rgb, separate bloc
    def appStarted(mode):

        #starting sand color
        mode.sandColor = SandboxingTime.preSetCols[random.randint(0,6)]
        mode.bg = "grey34"
        mode.buttonTextCol = "white"


        mode.openZeFile = startScreen.thePath

    #TODO: info popup?: elif event.key == 'i':    pass
    def keyPressed(mode,event):
        #main menu key
        if event.key == 'm':    mode.app.setActiveMode(mode.app.mainMenuMode)


    #SAVE FILE
    #TODO: SAVE FILE FUNCTIONALITY
    def saveFile(mode, path):
        print(f"{path} here the saving occurs, OVERALL SANDBOXING TIME")





    #MOUSE PRESSED
    def mousePressedStaticColor(mode, x, y, topx, coltopy, colboty, width10th):
        #static color picking
        if (    (topx <= x <= topx+width10th)
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[0]
        elif (    (topx + width10th <= x <= topx+width10th*2)
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[1]
        elif (    (topx+width10th*2 <= x <= topx+width10th*3)
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[2]
        elif (    (topx+width10th*3 <= x <= topx+width10th*4) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[3]
        elif (    (topx+width10th*4 <= x <= topx+width10th*5) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[4]
        elif (    (topx+width10th*5 <= x <= topx+width10th*6) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[5]
        elif (    (topx+width10th*6 <= x <= topx+width10th*7) 
                and (coltopy <= y <= colboty) ):
            mode.sandColor = SandboxingTime.preSetCols[6]
    #TODO: mousePressed in the boxes SAND TIME?
    #TODO: in sandbox Classes?    
    def mousePressed(mode, event):
        x,y = event.x, event.y

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

        #COLOR PICKING: WORKS, BAD STYLE THO? SEE REDRAWALL
        SandboxingTime.mousePressedStaticColor(mode, x, y, topx, coltopy, colboty, width10th)

        #TODO:other things you can do/UI with
        #MAIN MENU: NO SAVE
        if width10th*8 <= x <= width10th*9.5 and height10th*7 <= y <= height10th*7.5:
            mode.app.setActiveMode(mode.app.mainMenuMode)
        #SAVE FILE
        if width10th*8 <= x <= width10th*9.5 and height10th*8 <= y <= height10th*9:
            #print("thePath: ", startScreen.thePath)
            SandboxingTime.saveFile(mode, startScreen.thePath)

    #UI TIME
    def redrawColorPicker(mode, canvas, height10th, width10th, titleSize):
        #sandbox Main
        topx = width10th * .5
        topy = height10th * 2
        botx = width10th * 7.5
        boty = height10th * 9.5
        #color picker
        coltopy = height10th * 1.25
        colboty = height10th * 1.75
        colmidy = height10th * 1.5

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
    def redrawBasic(mode, canvas):
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
        canvas.create_rectangle(topx, topy, botx, boty, fill = mode.bg)
        canvas.create_text(     topx, coltopy, text = "sandbox", 
                                anchor = "sw", font = f"Times {titleSize}") 
        #color rn: NOTE should this go to the front?
        SandboxingTime.redrawColorPicker(mode, canvas, height10th, width10th, titleSize)
        canvas.create_text(     botx, topy, text = f"Current Color: {mode.sandColor}", 
                                anchor = "ne", font = f"Times {titleSize//2}", fill = mode.sandColor)
        #Main menu No save Button
        canvas.create_rectangle(width10th*8, height10th*7, width10th*9.5, height10th*7.5, fill = mode.bg)
        canvas.create_text(width10th*(8.75), height10th*(7.25), text = " Main Menu\n**No Save**", font = f"Times {titleSize//3}", fill = mode.buttonTextCol)
        #Save Button
        canvas.create_rectangle(width10th*8, height10th*8, width10th*9.5, height10th*9, fill = mode.bg)
        canvas.create_text(width10th*(8.75), height10th*(8.5), text = "SAVE", font = f"Times {titleSize}", fill = mode.buttonTextCol) #oh god, there's bad style

    def redrawAll(mode, canvas):
        #Basic UI framwork
        SandboxingTime.redrawBasic(mode, canvas)
        
        #TAG
        canvas.create_text(mode.width, mode.height, text = "SANDBOX", anchor = "se", font = "Times")
        canvas.create_text(0, mode.height, text = f"FILE OPENED: {startScreen.thePath}", anchor = "sw", font = "Times")
 












#TODO: the different modes of playing?
# angle of "shower"
#   from trig?
# game over if no movement for 5 sec == clicking done with sand button on app


class creativeSandbox(SandboxingTime):
    #automatically go into this one first

    Sand = make_dataclass('Sand', ['tag', 'x', 'y', 'lasty', 'color', 'falling']) #the "falling" doesn't do anything, fuck
    
    def appStarted(mode):
        super().appStarted()
        mode.grad = mode.width // 75 #~15

        #sand dataclass part
        mode.sand = []
        mode.nonMovingSand = []
        mode.everything = []

        mode.tag = 0
        mode.timerDelay = 0

        #ewwww NOTE: ???????
        mode.width10th = mode.width // 10 
        mode.height10th = mode.height // 10
        mode.titleSize = mode.width // 25
        mode.topx = mode.width10th * .5
        mode.topy = mode.height10th * 2
        mode.botx = mode.width10th * 7.5
        mode.boty = mode.height10th * 9.5


    #TODO: SCALEABLE VALUES
    def createSand(mode, x, y):
        newSand = creativeSandbox.Sand(tag = mode.tag, x = x, y = y, lasty = y, color = mode.sandColor, falling = True)
        mode.sand.append(newSand)
        mode.tag += 1

    def mousePressed(mode, event):
        super().mousePressed(event)
        x, y = event.x, event.y
        #SAVE FILE:

        #SAND DROPPING
        if ( creativeSandbox.inBox(mode, event.x, event.y) and creativeSandbox.notOverlappingAnyOthers(mode, event.x, event.y) ):
            creativeSandbox.createSand(mode, x, y)
    def mouseDragged(mode, event):
        super().mouseDragged(event)
        x, y = event.x, event.y

        width10th = mode.width // 10 
        height10th = mode.height // 10
        titleSize = mode.width // 25
        topx = width10th * .5
        topy = height10th * 2
        botx = width10th * 7.5
        boty = height10th * 9.5
        #TODO: THIS SHIT
        #SAND DROPPING
        if ( creativeSandbox.inBox(mode, event.x, event.y) and creativeSandbox.notOverlappingAnyOthers(mode, event.x, event.y) ):
            creativeSandbox.createSand(mode, x, y)




    def inBox(mode,x,y):
        if (mode.topx + mode.grad <= x <= mode.botx - mode.grad) and (mode.topy + mode.grad <= y <= mode.boty - mode.grad):
            return True
    def notOverlappingAnyOthers(mode,x,y):
        for grains in mode.nonMovingSand:
            if grains.x == x and grains.y == y:         return True #Jank?
            if creativeSandbox.overlap(mode, grains.x, grains.y, x, y): return False
        return True
    def overlap(mode, gx, gy, x, y):
        #TODO: sort this shit out
        tooClose = ( (gx - x)**2 + (gy - y)**2 )**.5  <= (mode.grad*2)
        return tooClose
    def moveParticle(mode):
        mode.everything = mode.sand + mode.nonMovingSand
        for g in range(len(mode.sand)):
            grains = mode.sand[g]
            if creativeSandbox.inBox(mode, grains.x, grains.y) and creativeSandbox.notOverlappingAnyOthers(mode, grains.x, grains.y):
                grains.y += 1
            else:
                mode.nonMovingSand.append(grains)
        for g in mode.nonMovingSand:
            if g in mode.sand:
                sandIndex = mode.sand.index(g)
                mode.sand.pop(sandIndex)


    def timerFired(mode):
        creativeSandbox.moveParticle(mode)

    def redrawAll(mode, canvas):
        super().redrawAll(canvas)
        for grains in mode.everything:
            canvas.create_oval(grains.x - mode.grad, grains.y - mode.grad, grains.x + mode.grad, grains.y + mode.grad, fill = grains.color, outline = grains.color)
        

        
        
            
        
        #if len(mode.nonMovingSand) == 15:
         #   print(mode.nonMovingSand)
        #print(len(mode.sand), len(mode.nonMovingSand), len(mode.everything))


#make more ways of 'creation"
class playLevelSandbox(SandboxingTime):
    #make character and levels
    pass
class levelCreateSandbox(SandboxingTime):
    pass


class SandBoxModes(ModalApp):
    def appStarted(app):
        app.mainMenuMode = startScreen()
        app.newProjectMenu = menuNew()
        app.oldProjectMenu = menuProfiles()
        app.sandBoxMode = SandboxingTime()

        app.sbFUN = creativeSandbox()
        app.sbPLAY = playLevelSandbox()
        app.sbCREATE = levelCreateSandbox()
        
        app.setActiveMode(app.mainMenuMode)
        #app.timerDelay = 50

app = SandBoxModes(width=800, height=600)

print("\n*************Done with Shit to do*************")
