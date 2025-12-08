import pygame
import time
import threading
import random
# https://www.youtube.com/watch?v=MwbXp6_C5i8 is the link to the video for threading and running multiple functions concurrently
pygame.init()
class Anim: #Masons class and funcs
    def __init__(self, animatronic, difficulty, curRoom, rooms):
        self._animatronic=animatronic
        self._difficulty=difficulty
        self._curRoom=curRoom
        self._rooms=rooms
    def setAnim(self, animatronic):
        self._animatronic=animatronic
    def setDiff(self, difficulty):
        self._difficulty=difficulty
    def setRoom(self, curRoom):
        self._curRoom=curRoom
    def setRooms(self, rooms):
        self._rooms=rooms
    def getAnim(self):
        return self._animatronic
    def getDiff(self):
        return self._difficulty
    def getRoom(self):
        return self._curRoom
    def getRooms(self):
        return self._rooms=[]
    def animatronicMove(difficulty, time):
        nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        while _6am == False:
            time.sleep(5)
            isWalk = random.choice(nums)
            if isWalk <= difficulty
                move=True
                moveArea(move)
            else:
                move=False
                placeholder=moveArea(move)
    def moveArea(self, move):
        if move == True:
            if self._animatronic == "Freddy":
                if self._curRoom.lower()=="showstage":
                    toMove=["Dining", "Restrooms"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="dining":
                    toMove=["EastHall", "Restrooms", "Kitchen", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="kitchen":
                    toMove=["Dining", "EastHall", "Kitchen"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="restroom":
                    toMove=["Dining", "Kitchen", "Restroom"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="easthall":
                    toMove=["Dining", "EastHallCorner","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="easthallcorner":
                    toMove=["Office", "EastHallCorner","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
            elif self._animatronic == "Chica":
                if self._curRoom.lower()=="showstage":
                    toMove=["Dining", "Restrooms"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="dining":
                    toMove=["EastHall", "Restrooms", "Kitchen", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="kitchen":
                    toMove=["Dining", "EastHall", "Kitchen"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="restroom":
                    toMove=["Dining", "Kitchen", "Restroom"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="easthall":
                    toMove=["Dining", "EastHallCorner","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="easthallcorner":
                    toMove=["Office", "EastHallCorner","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
            elif self._animatronic == "Bonnie":
                if self._curRoom.lower()=="showstage":
                    toMove=["Dining", "Backstage"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="dining":
                    toMove=["WestHall", "BackStage", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="backstage":
                    toMove=["Dining", "WestHall", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="westhall":
                    toMove=["Dining", "WestHallCorner", "SupplyCloset"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="westhallcorner":
                    toMove=["Office", "EastHallCorner","westhall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                elif self._curRoom.lower()=="supplycloset":
                    toMove=["Office","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
            elif self._animatronic == "Foxy":
                if self._curRoom.lower()=="piratecove":
                    toMove=["PirateCove"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                
freddy=Anim("Freddy", 3, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
chica=Anim("Chica", 3, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
bonnie=Anim("Bonnie", 3, "ShowStage", ["ShowStage", "Dining", "Backstage", "SupplyCloset", "WestHall","WestHallCorner"])
foxy=Anim("Foxy", 3, "PiratesCove", ["PiratesCove", "Dining", "WestHall","WestHallCorner"])
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button
            running = False

    # Game logic (e.g., update object positions)

    # Drawing
    screen.fill((0, 0, 0)) # Fill the screen with black (RGB)
    # Update the display
    pygame.display.flip() # or pygame.display.update()

# ^ Use of AI for pygame starter ^

pygame.quit()