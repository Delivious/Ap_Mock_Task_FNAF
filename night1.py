import pygame
import time
import threading
import random
import sys
from Custom_Night_Menu import bonniedif, chicadif, foxydif, freddif
fred = pygame.image.load("freddy1.png")
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
        return self._rooms
    def animatronicMove(self, difficulty, sixam=False):
        global gameGo
        nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        while gameGo == True:
            time.sleep(5)
            isWalk = random.choice(nums)
            if isWalk <= difficulty:
                move=True
                self.moveArea(move)
            else:
                move=False
                self.moveArea(move)
        if sixam==True:
            print("Its 6am")
    def moveArea(self, move):
        """allows animatronics to move"""
        global jumpscare
        if move == True:
            if self._animatronic == "Freddy":
                if self._curRoom.lower()=="showstage":
                    toMove=["Dining", "Restrooms"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="dining":
                    toMove=["EastHall", "Restrooms", "Kitchen", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="kitchen":
                    toMove=["Dining", "EastHall", "Kitchen"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="restrooms":
                    toMove=["Dining", "Kitchen", "Restrooms"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="easthall":
                    toMove=["EastHallCorner","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="easthallcorner":
                    toMove=["Office", "EastHallCorner"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="office":
                    office=True
                    if office==True:
                        check=checkDoorEast()
                        if check==True:
                            jumpscare=False
                            self._curRoom=jumpFunc(jumpscare, self._animatronic) 
                        else:
                            jumpscare=True
            elif self._animatronic == "Chica":
                if self._curRoom.lower()=="showstage":
                    toMove=["Dining", "Restroom"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="dining":
                    toMove=["EastHall", "Restroom", "Kitchen", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="kitchen":
                    toMove=["Dining", "EastHall", "Kitchen"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="restroom":
                    toMove=["Dining", "Kitchen", "Restroom"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="easthall":
                    toMove=["EastHallCorner","EastHall"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="easthallcorner":
                    toMove=["Office", "EastHallCorner"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="office":
                    office=True
                    if office==True:
                        check=checkDoorEast()
                        if check==True:
                            jumpscare=False
                            self._curRoom=jumpFunc(jumpscare, self._animatronic)      
                        else:
                            jumpscare=True
            elif self._animatronic == "Bonnie":
                if self._curRoom.lower()=="showstage":
                    toMove=["Dining", "Backstage"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="dining":
                    toMove=["WestHall", "BackStage", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="backstage":
                    toMove=["Dining", "WestHall", "Dining"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="westhall":
                    toMove=["WestHall", "WestHallCorner", "SupplyCloset"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="westhallcorner":
                    toMove=["Office", "EastHallCorner"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="supplycloset":
                    toMove=["EastHallCorner","EastHall","SupplyCloset"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="office":
                    office=True
                    if office==True:
                        check=checkDoorWest()
                        if check==True:
                            jumpscare=False
                            self._curRoom=jumpFunc(jumpscare, self._animatronic)     
                        else:
                            jumpscare=True
            elif self._animatronic == "Foxy":
                if self._curRoom.lower()=="piratecove":
                    toMove=["PirateCove","Pirate1"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="pirate1":
                    toMove=["Pirate1","Pirate2"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="pirate2":
                    toMove=["Pirate2","Pirate3"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="pirate3":
                    toMove=["Pirate3","Running"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="running":
                    office=False
                    counter=0
                    while office==False:
                        if counter!=5:
                            counter+=1
                            time.sleep(1)
                        else:
                            office=True
                    if office==True:
                        check=checkDoorWest()
                        if check==True:
                            jumpscare=False
                            self._curRoom=jumpFunc(jumpscare, self._animatronic)                       
                        else:
                            jumpscare=True                   
def batteryDrain():
    """drains the battery based on how many things are turned on"""
    global batteryStacks, _battery
    time.sleep(batteryStacks)
    _battery-=1
def battery(): 
    """checks how many things are turned on and using battery"""
    global westDoorState, eastDoorState, cameraState, eastLightState, westLightState, batteryStacks
    batteryList=[westDoorState,eastDoorState,cameraState,eastLightState,westLightState]
    batteryCounter=0
    for _battery in batteryList:
        if _battery:
            batteryCounter+=1
    batteryStacks-=batteryCounter
def jumpFunc(jumpscare,name):
    """Checks if you have been attacked by an animatronic"""
    if jumpscare==False:
        if name == "Freddy":
            return "ShowStage"
        elif name == "Chica":
            return "ShowStage"
        elif name == "Bonnie":
            return "ShowStage"
        else:
            return "PirateCove"
def closeWest():
    """closes and opens left door"""
    global westDoorState
    if westDoorState==True:
        return False
    else:
        return True
def closeEast():
    """opens and closes right door"""
    global eastDoorState
    if eastDoorState==True:
        return False
    else:
        return True
def checkDoorWest():
    """checks if the left door is open or not"""
    global westDoorState
    if westDoorState == False:
        return False
    else:
        return True
def checkDoorEast():
    """checks if the right door is open or not"""
    global eastDoorState
    if eastDoorState == False:
        return False
    else:
        return True
def isKill():
    global jumpscare
    if jumpscare==True:
        if freddy.getRoom().lower()=="office":
            print("feddy jumpscare")
        elif chica.getRoom().lower()=="office":
            print("chicken jumpscare")
        elif bonnie.getRoom().lower()=="office":
            print("bon bon jumpscare")
        else:
            print("fox from smash bros jumpscare")
        sys.exit()
cameraState=False
batteryStacks=6
eastLightState=False
westLightState=False
jumpscare=False
_battery=100
screen_width = 2500
screen_height = 1500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")
freddy = Anim("Freddy", 20, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
chica = Anim("Chica", 20, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
bonnie = Anim("Bonnie", 20, "ShowStage", ["ShowStage", "Dining", "Backstage", "SupplyCloset", "WestHall","WestHallCorner"])
foxy = Anim("Foxy", 20, "PirateCove", ["PiratesCove", "Pirate1", "Pirate2","Pirate3","Running"])
fredAI  = threading.Thread(target=freddy.animatronicMove, args=(freddy.getDiff(),), daemon=True)
chicaAI = threading.Thread(target=chica.animatronicMove, args=(chica.getDiff(),), daemon=True)
bonnAI  = threading.Thread(target=bonnie.animatronicMove, args=(bonnie.getDiff(),), daemon=True)
foxyAI  = threading.Thread(target=foxy.animatronicMove, args=(foxy.getDiff(),), daemon=True)
animList=[fredAI, chicaAI, bonnAI, foxyAI]
eastDoorState = False
westDoorState = False
gameGo = True
running = True
fredAI.start()
time.sleep(1)
chicaAI.start()
time.sleep(1)
bonnAI.start()
time.sleep(1)
foxyAI.start()
time.sleep(1)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button
            running = False
    isKill()
    # Game logic (e.g., update object positions)
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        westDoorState=closeWest()
        time.sleep(0.3)
        if westDoorState==True:
            print("West door Closed")
        else:
            print("West Door Opened")
    elif pressed[pygame.K_RIGHT]:
        eastDoorState=closeEast()
        time.sleep(0.3)
        if eastDoorState==True:
            print("East door Closed")
        else:
            print("East Door Opened")
    # Drawing
    screen.fill((0, 0, 0)) # Fill the screen with black (RGB)
    # Update the display
    pygame.display.flip() # or pygame.display.update()

#Use of AI for pygame starter, fixing threads args and stopping all threads

pygame.quit()