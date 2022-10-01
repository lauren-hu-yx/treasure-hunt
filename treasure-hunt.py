#
# Lauren Hu - 2021
#
# Battleship Game Rebranded - Treasure Hunt
#


#import graphics, random, and time libraries
from graphics import *
from random import *
from time import *

#intro - appears at start of game
    #parameters: none
def intro():
    #create new GUI for intro text
    win = GraphWin("Welcome", 500, 500)
    win.setBackground("powderblue")
    rect = Rectangle(Point(50,400),Point(450,100))
    rect.setFill("white")
    rect.setOutline("midnightblue")
    rect.setWidth(5)
    rect.draw(win)
    #background story messages -- appear as user clicks
    message = Text(Point(250,250), "Welcome to Treasure Hunt!").draw(win)
    message.setFace("courier")
    message.setSize(20)
    message2 = Text(Point(250,350), "Click anywhere to continue.").draw(win)
    message2.setStyle("italic")
    win.getMouse()
    message.setText("A pirate has buried some \n treasure around his island \n and you must try to find it.")
    win.getMouse()
    message.setText("However, you also happen to \n have hidden some treasure \n yourself.")
    win.getMouse()
    message.setText("Try to find the pirate's \n treasure before he finds yours! \n Good luck!")
    message2.setText("Click again to start the game!")
    #wait for mouse click to close intro GUI and start game
    win.getMouse()
    win.close()

#closing - appears after a someone wins to show user result
    #parameters: playerFleetTotal = list containing all player ship locations
                #computerFleetTotal = list with all computer ship locations
def closing(playerFleetTotal,computerFleetTotal):
    #create new GUI for closing messages
    win = GraphWin("Game Over", 500, 500)
    win.setBackground("powderblue")
    rect = Rectangle(Point(50,400),Point(450,100))
    rect.setFill("white")
    rect.setOutline("midnightblue")
    rect.setWidth(5)
    rect.draw(win)
    subtext = Text(Point(250,350), "Click anywhere to close.").draw(win)
    subtext.setStyle("italic")
    #display appropriate message for whether user wins or loses
    if playerFleetTotal == []:
        message = Text(Point(250,250), "You lose! \n Better luck next time.").draw(win)
    if computerFleetTotal == []:
        message = Text(Point(250,250), "You win! \n Thank you for playing.").draw(win)
    message.setFace("courier")
    message.setSize(20)
    win.getMouse()
    win.close()


#check if lists overlap (to check ship coordinates to prevent ship overlap)
    #parameters: list1 & list2 = two lists of points to compare
def listOverlap(list1,list2):
    #checks if each list item in one list matches list items in the other list
    for i in list1:
        if i in list2:
            #if any list items match, returns True
            return True
    #if all list items are unique (no overlap), return False
    return False


##We intended this function to guess around the point when the computer detects
##a hit. Unfortunately we did not have time to finish so here lies our program
##in the code graveyard.
##def smart(x,y,computerGuessList,playerFleetTotal,win1):
##    if x < 9 and Point(x+0.5,y) not in computerGuessList:
##        x += 1
##    elif x > 1 and Point(x-0.5,y) not in computerGuessList:
##        x -= 1
##    elif y < 9 and Point(x,y+0.5) not in computerGuessList:
##        y += 1
##    elif y > 1 and Point(x,-0.5) not in computerGuessList:
##        y -= 1


#generates ships for the user
    #parameters: win = window to create ships in
                #fleet = the list of locations that make up a ship
                #numberSpaces = number of spaces in a given ship (5,4,3,3,2)
                #playerMessage2 = text containing any error messages
def shipBuilderPlayer(win,fleet,numberSpaces,playerMessage2):
    #creates list to track the colored boxes to be undrawn later due to an error
    #defines a variable that tracks the last box location in the list "fleet"
    listBoxes = []
    fleetPos = -1
    #repeats until the full ship is created
    while len(fleet) != numberSpaces:
        #creates the first location (space on the board)
        click = win.getMouse()
        x,y = click.getX(),click.getY()
        blueBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
        blueBox.setFill("blue")
        ship = Point(int(x) + 0.5,int(y) + 0.5)
        #checks if space is within boundaries
        if (0 < x < 10) and (0 < y < 10):
            #checks if it is a repeated location (click same space twice)
            if str(ship) in fleet:
                #replaces the repeated ship (doesn't increase fleet number)
                pos = fleet.index(str(ship))
                fleet[pos] = str(ship)
            #if this is the first space in the ship then add the space to
            #list "fleet" and create a blue box marking location
            elif len(fleet) == 0:
                fleet = fleet + [str(ship)]
                fleetPos += 1
                blueBox.draw(win)
                listBoxes = listBoxes + [blueBox]
                fleetPosX = eval(fleet[fleetPos]).getX()
                fleetPosY = eval(fleet[fleetPos]).getY()
            #if the click is one to the left of the first point
            elif (fleetPosX - ship.getX() == -1) and (fleetPosY == ship.getY()):
                #create the desired number of spaces and blue boxes going in
                #that direction
                for i in range(numberSpaces-1):
                    blueBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
                    blueBox.setFill("blue")
                    blueBox.draw(win)
                    listBoxes = listBoxes + [blueBox]
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    #checks if each consecutive point is in bounds
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        x = x + 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    #clears the fleet and undraws the boxes if they are placed
                    #in an invalid spot (out of bounds)
                    else:
                        for box in listBoxes:
                            box.undraw()
                        fleet = []
                        fleetPos = -1
                        playerMessage2.setText("Pieces must be placed in bounds.")
            #if the click is one to the right of the first point
            elif (fleetPosX - ship.getX() == 1) and (fleetPosY == ship.getY()):
                for i in range(numberSpaces-1):
                    blueBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
                    blueBox.setFill("blue")
                    blueBox.draw(win)
                    listBoxes = listBoxes + [blueBox]
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        x = x - 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        for box in listBoxes:
                            box.undraw()
                        fleet = []
                        fleetPos = -1
                        playerMessage2.setText("Pieces must be placed in bounds.")
            #if the click is one down from the first point
            elif (fleetPosY - ship.getY() == -1) and (fleetPosX == ship.getX()):
                for i in range(numberSpaces-1):
                    blueBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
                    blueBox.setFill("blue")
                    blueBox.draw(win)
                    listBoxes = listBoxes + [blueBox]
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        y = y + 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        for box in listBoxes:
                            box.undraw()
                        fleet = []
                        fleetPos = -1
                        playerMessage2.setText("Pieces must be placed in bounds.")
            #if the click is one up from the first point
            elif (fleetPosY - ship.getY() == 1) and (fleetPosX == ship.getX()):
                for i in range(numberSpaces-1):
                    blueBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
                    blueBox.setFill("blue")
                    blueBox.draw(win)
                    listBoxes = listBoxes + [blueBox]
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        y = y - 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        for box in listBoxes:
                            box.undraw()
                        fleet = []
                        fleetPos = -1
                        playerMessage2.setText("Pieces must be placed in bounds.")
    #return the list of points (spaces) that comprise the ship and the colored
    #boxes that display the locations in case they need to be undrawn
    return fleet, listBoxes


#generates ships for computer (same process as playerShipBuilder)
def shipBuilderComputer(win,fleet,numberSpaces):
    fleetPos = -1
    while len(fleet) != numberSpaces:
        #generates an x and y value between 0 and 10
        x,y = randint(0,10),randint(0,10)
        ship = Point(int(x) + 0.5,int(y) + 0.5)
        if (0 < x < 10) and (0 < y < 10):
            if str(ship) in fleet:
                pos = fleet.index(str(ship))
                fleet[pos] = str(ship)
            elif len(fleet) == 0:
                fleet = fleet + [str(ship)]
                fleetPos += 1
                fleetPosX = eval(fleet[fleetPos]).getX()
                fleetPosY = eval(fleet[fleetPos]).getY()
            elif (fleetPosX - ship.getX() == -1) and (fleetPosY == ship.getY()):
                for i in range(numberSpaces-1):
                    ship = Point(int(x) + 0.5,int(y) + 0.5)  
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        x = x + 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        fleet = []
                        fleetPos = -1
            elif (fleetPosX - ship.getX() == 1) and (fleetPosY == ship.getY()):
                for i in range(numberSpaces-1):
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        x = x - 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        fleet = []
                        fleetPos = -1
            elif (fleetPosY - ship.getY() == -1) and (fleetPosX == ship.getX()):
                for i in range(numberSpaces-1):
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        y = y + 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        fleet = []
                        fleetPos = -1                        
            elif (fleetPosY - ship.getY() == 1) and (fleetPosX == ship.getX()):
                for i in range(numberSpaces-1):
                    ship = Point(int(x) + 0.5,int(y) + 0.5)
                    if (0 < x < 10) and (0 < y < 10):
                        fleet = fleet + [str(ship)]
                        y = y - 1
                        fleetPos = fleetPos + 1
                        fleetPosX = eval(fleet[fleetPos]).getX()
                        fleetPosY = eval(fleet[fleetPos]).getY()
                    else:
                        fleet = []
                        fleetPos = -1
    #returns points that make up the computer's ship
    return fleet


#sets up GUI and ships for user  
def playerSetup():
    #creates graphics window for player and instruction text
    win1 = GraphWin("Player's Board", 700, 700)
    win1.setCoords(-1,-1,11,11)
    vertical,horizontal = 0,0
    fleet = []
    playerMessage = Text(Point(5,10.6), "TREASURE HUNT").draw(win1)
    playerMessage.setSize(18)
    playerMessage.setStyle("bold")
    playerMessage2 = Text(Point(5,10.3), "Click to start.").draw(win1)
    playerMessage2.setStyle("italic")
    win1.getMouse()
    playerMessage2.setText("Any errors will show up here.")
    #creates veritcal and horizontal line borders
    for i in range(11):
        vLine = Line(Point(vertical,0), Point(vertical,10))
        hLine = Line(Point(0,horizontal), Point(10, horizontal))
        vLine.draw(win1)
        hLine.draw(win1)
        vertical += 1
        horizontal += 1

    playerMessage.setText("Place your 5 piece.")
    #listA and listBoxes contain the points for the 5 space ship and their
    #rectangle boxes
    listA, listBoxes = shipBuilderPlayer(win1,fleet,5,playerMessage2)

    playerMessage.setText("Place your 4 piece.")
    listB, listBoxes = shipBuilderPlayer(win1,fleet,4,playerMessage2)
    #if the points from listA overlaps with listB
    while listOverlap(listA,listB) == True:
        #iterate over all the rectangles in the list
        for box in listBoxes:
            #undraw every rectangle
            box.undraw()
        playerMessage2.setText("Pieces cannot be overlapped.")
        #regenerate the player's 4 space ship
        listB, listBoxes = shipBuilderPlayer(win1,fleet,4,playerMessage2)

    playerMessage.setText("Place your 3 piece.")
    listC, listBoxes = shipBuilderPlayer(win1,fleet,3,playerMessage2)
    #if points from listC overlap with listA or listB
    while listOverlap(listA,listC) == True or listOverlap(listB,listC) == True:
        for box in listBoxes:
            box.undraw()
        playerMessage2.setText("Pieces cannot be overlapped.")
        #regenerate the player's 3 space ship
        listC, listBoxes = shipBuilderPlayer(win1,fleet,3,playerMessage2)

    playerMessage.setText("Place your other 3 piece.")
    listD, listBoxes = shipBuilderPlayer(win1,fleet,3,playerMessage2)
    #if points from listD overlap with listA, listB, or listC
    while listOverlap(listA,listD) == True or listOverlap(listB,listD) == True or listOverlap(listC,listD) == True:
        for box in listBoxes:
            box.undraw()
        playerMessage2.setText("Pieces cannot be overlapped.")
        #regenerate the player's 3 space ship
        listD, listBoxes = shipBuilderPlayer(win1,fleet,3,playerMessage2)

    playerMessage.setText("Place your 2 piece.")
    listE, listBoxes = shipBuilderPlayer(win1,fleet,2,playerMessage2)
    #if points from listD overlap with listA, listB, listC, or listD
    while listOverlap(listA,listE) == True or listOverlap(listB,listE) == True or listOverlap(listC,listE) == True or listOverlap(listD,listE) == True:
        for box in listBoxes:
            box.undraw()
        playerMessage2.setText("Pieces cannot be overlapped.")
        #regenerate the player's 2 space ship
        listE, listBoxes = shipBuilderPlayer(win1,fleet,2,playerMessage2)
    #combine all the point locations of the ships to be used for guessing
    playerFleetTotal = listA + listB + listC + listD + listE
    #return the window, total fleet, and current messages
    return win1,playerFleetTotal,playerMessage,playerMessage2


#sets up GUI and ships for computer (similar process as playerSetup, except ships invisible)
def computerSetup(playerMessage):
    win2 = GraphWin("Opponent's Board", 700, 700)
    win2.setCoords(-1,-1,11,11)
    vertical,horizontal = 0,0
    fleet = []
    
    for i in range(11):
        vLine = Line(Point(vertical,0), Point(vertical,10))
        hLine = Line(Point(0,horizontal), Point(10, horizontal))
        vLine.draw(win2)
        hLine.draw(win2)
        vertical += 1
        horizontal += 1

    listA = shipBuilderComputer(win2,fleet,5)
    
    listB = shipBuilderComputer(win2,fleet,4)
    while listOverlap(listA,listB) == True:
        listB = shipBuilderComputer(win2,fleet,4)
    
    listC = shipBuilderComputer(win2,fleet,3)
    while listOverlap(listA,listC) == True or listOverlap(listB,listC) == True:
        listC = shipBuilderComputer(win2,fleet,3)
    
    listD = shipBuilderComputer(win2,fleet,3)
    while listOverlap(listA,listD) == True or listOverlap(listB,listD) == True or listOverlap(listC,listD) == True:
        listD = shipBuilderComputer(win2,fleet,3)
    
    listE = shipBuilderComputer(win2,fleet,2)
    while listOverlap(listA,listE) == True or listOverlap(listB,listE) == True or listOverlap(listC,listE) == True or listOverlap(listD,listE) == True:
        listE = shipBuilderComputer(win2,fleet,2)

    computerFleetTotal = listA + listB + listC + listD + listE
    playerMessage.setText("Treasure has been hidden! The pirates await your first move.")
    return win2,computerFleetTotal


#run each time player needs to make a guess
    #parameters: playerGuessList = list containing spaces the player has guessed
                #computerFleetTotal = total spaces that make up the computer ships
                #win2 = window
                #playerMessage = instruction text
                #x and y = coordinates on the grid
def playerGuess(playerGuessList,computerFleetTotal,win2,playerMessage2,x,y):
    #wait for user to click on opponent's window
    click = win2.getMouse()
    #check if the coords of the click are within the 10x10 grid
    if (0 < click.getX() < 10) and (0 < click.getY() < 10):
        #if valid, convert click coords to represent a box on the grid
        x = int(click.getX()) + 0.5
        y = int(click.getY()) + 0.5
        #check if that point has been guessed already
        if str(Point(x,y)) in playerGuessList:
            #if already guessed, display error message and re-run function so user can guess again
            playerMessage2.setText("You've already looked there!")
            playerGuess(playerGuessList,computerFleetTotal,win2,playerMessage2,x,y)
        else:
            #if not guessed yet, check if point is in computer's ship list
            if str(Point(x,y)) in computerFleetTotal:
                #if point in computer's ship list, remove point from list
                computerFleetTotal.remove(str(Point(x,y)))
                #draw a red box to indicate a hit
                redBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
                redBox.setFill("red")
                redBox.draw(win2)
                #add the newly guessed point to the guess list and display message
                playerGuessList.append(str(Point(x,y)))
                playerMessage2.setText("You found the enemy's treasure!")
            #if point not in computer's ship list, draw a gray box to indicate a miss
            elif str(Point(x,y)) not in computerFleetTotal:
                grayBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
                grayBox.setFill("lightgray")
                grayBox.draw(win2)
                #add the newly guessed point to the guess list and display message
                playerGuessList.append(str(Point(x,y)))
                playerMessage2.setText("Nothing there!")
    #if coords are not in grid, have user guess again (until they make a valid guess)
    else: playerGuess(playerGuessList,computerFleetTotal,win2,playerMessage2,x,y)


#run each time computer needs to make guess
    #parameters: computerGuessList = list containing spaces the computer has guessed
                #playerFleetTotal = total spaces that make up the player ships
                #win1 = window
                #result = hit/miss text
                #x and y = coordinates on the grid
def computerGuess(computerGuessList,playerFleetTotal,win1,result,x,y):
    #if last shot was a hit, have computer make an "educated" guess (hits next one over)
    if result == True:
        if x < 9 and Point(x+0.5,y) not in computerGuessList:
            x += 1
        #if box is on right edge or is in guess list already, generate random numbers
        else: x,y = randint(0,9) + 0.5,randint(0,9) + 0.5
    #default - generate random numbers for computer random guess
    else:
        x,y = randint(0,9) + 0.5,randint(0,9) + 0.5
    #check if that point has been guessed already
    if str(Point(x,y)) in computerGuessList:
        #if already guessed, re-run function so computer generates a new guess
        return computerGuess(computerGuessList,playerFleetTotal,win1,result,x,y)
    else:
        #if not guessed yet, check if point is in user's ship list
        if str(Point(x,y)) in playerFleetTotal:
            #if point in user's ship list, remove point from list
            playerFleetTotal.remove(str(Point(x,y)))
            #draw a red box to indicate a hit
            redBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
            redBox.setFill("red")
            redBox.draw(win1)
            #add the newly guessed point to the guess list
            computerGuessList.append(str(Point(x,y)))
            #return True (hit) and the coords (x,y)
            return True,x,y
        #if point not in user's ship list, draw a gray box to indicate a miss
        elif str(Point(x,y)) not in playerFleetTotal:
            grayBox = Rectangle(Point(int(x),int(y)),Point(int(x)+1,int(y)+1))
            grayBox.setFill("lightgray")
            grayBox.draw(win1)
            #add the newly guessed point to the guess list
            computerGuessList.append(str(Point(x,y)))
            #return False (miss) and the coords (x,y)
            return False,x,y
            

#MAIN FUNCTION         
def main():
    #intro GUI
    intro()
    #setup GUIs and ships for player and computer
    win1,playerFleetTotal,playerMessage,playerMessage2 = playerSetup()
    win2,computerFleetTotal = computerSetup(playerMessage)
    #instruct/remind user objective of game
    playerMessage2.setText("Find the pirate's treasure before he finds yours!")

    #initialize lists and variables (guess lists, computer guess result, and coords)
    playerGuessList = [Point(-1,-1)]
    computerGuessList = [Point(-1,-1)]
    result = False
    x,y = -1,-1
    #take turns guessing until one ship list is empty (all ships hit)
    while playerFleetTotal != [] and computerFleetTotal != []:
        #text + player guess function
        playerMessage.setText("Your turn.")
        playerGuess(playerGuessList,computerFleetTotal,win2,playerMessage2,x,y)
        #check if both lists still aren't empty
        if playerFleetTotal != [] and computerFleetTotal != []:
            playerMessage.setText("Opponent's turn.")
            #real time pause (0.5 seconds) to simulate opponent taking their turn
            sleep(0.5)
            #computer guess function -- returns True(hit)/False(miss) and coords
            result,x,y = computerGuess(computerGuessList,playerFleetTotal,win1,result,x,y)

    #closing GUI + close game windows (user and computer)
    closing(playerFleetTotal,computerFleetTotal)
    win1.close()
    win2.close()
#run main
main()