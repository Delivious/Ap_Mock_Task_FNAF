import pygame
import time
import threading
import random

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
                moveArea(move)
    def moveArea(move):


freddy=Anim("Freddy", 3, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
chica=Anim("Chica", 3, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
bonnie=Anim("Bonnie", 3, "ShowStage", ["ShowStage", "Dining", "Backstage", "SupplyCloset", "WestHall","WestHallCorner"])
foxy=Anim("Focxy", 3, "PiratesCove", ["PiratesCove", "Dining", "WestHall","WestHallCorner"])
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