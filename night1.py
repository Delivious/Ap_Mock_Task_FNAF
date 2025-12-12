import pygame
import time
import threading
import random
import sys
from Custom_Night_Menu import freddif, foxydif, chicadif, bonniedif
fred = pygame.image.load("freddy1.png")
screen_width = 1332
screen_height = 594
allnoanim= pygame.image.load("officeimages/all.png")
bothdoorchica= pygame.image.load("officeimages/bothdoorchica.png")
bothdoorleftlight= pygame.image.load("officeimages/bothdoorleftlight.png")
bothdoorrightlight= pygame.image.load("officeimages/bothdoorrightlight.png")
bothdoors=  pygame.image.load("officeimages/bothdoors.png")
bothlightleftdoor= pygame.image.load("officeimages/bothlightleftdoor.png")
bothlightrightdoor= pygame.image.load("officeimages/bothlightsrightdoor.png")
bothlights= pygame.image.load("officeimages/bothlights.png")
chicabothlight= pygame.image.load("officeimages/chicabothlight.png")
chicaleftdoor= pygame.image.load("officeimages/chicaleftdoor.png")
chicalightbothdoor= pygame.image.load("officeimages/chicalightbothdoor.png")
chicalightrightdoor= pygame.image.load("officeimages/chicalightrightdoor.png")
chicalightleftdoor= pygame.image.load("officeimages/chicalightleftdoor.png")
chicarightdoor= pygame.image.load("officeimages/chicarightdoor.png")
leftdoorleftlight= pygame.image.load("officeimages/leftdoorleftlight.png")
leftdoorrightlight= pygame.image.load("officeimages/leftdoorrightlight.png")
blackout= pygame.image.load("officeimages/officeblackout.png")
officebonnie= pygame.image.load("officeimages/officebonnie.png")
officechica= pygame.image.load("officeimages/officechica.png")
officeleftlight= pygame.image.load("officeimages/officeleftlight.png")
officerightlight= pygame.image.load("officeimages/officerightlight.png")
officenodoor= pygame.image.load("officeimages/officenodoor.png")
officerightdoor= pygame.image.load("officeimages/officerightdoor.png")
officeleftdoor= pygame.image.load("officeimages/officeleftdoor.jpg")
rightdoorrightlight= pygame.image.load("officeimages/rightdoorrightlight.png")
rightdoorleftlight= pygame.image.load("officeimages/rightdoorleftlight.png")
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
# https://www.youtube.com/watch?v=MwbXp6_C5i8 is the link to the video for threading and running multiple functions concurrently
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
        global gameGo, eastDoorState, westDoorState
        nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        while gameGo == True:
            time.sleep(5)
            isWalk = random.choice(nums)
            if isWalk <= difficulty:
                move=True
                self.moveArea(move)
            elif self._curRoom.lower()=="office":
                if self._animatronic == "freddy" and eastDoorState:
                    jumpscare=False
                    jumpFunc(jumpscare, self._animatronic)
                elif self._animatronic == "chica" and eastDoorState:
                    jumpscare=False
                    jumpFunc(jumpscare, self._animatronic)
                elif self._animatronic == "bonnie" and westDoorState:
                    jumpscare=False
                    jumpFunc(jumpscare, self._animatronic)
                elif self._animatronic == "foxy" and westDoorState:
                    jumpscare=False
                    jumpFunc(jumpscare, self._animatronic)
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
                    toMove=["Dining", "BackStage"]
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
                    toMove=["Office", "WestHallCorner"]
                    whereMove=random.choice(toMove)
                    self._curRoom=whereMove
                    print(f"{self._animatronic} is in {self._curRoom}")
                elif self._curRoom.lower()=="supplycloset":
                    toMove=["WestHallCorner","WestHall","SupplyCloset"]
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
def cameraPos(position):
    if position == 1:
        print(position)
    elif position == 2:
        print(position)
    elif position == 3:
        print(position)
    elif position == 4:
        print(position)
    elif position == 5:
        print(position)
    elif position == 6:
        print(position)
    elif position == 7:
        print(position)
    elif position == 8:
        print(position)
    elif position == 9:
        print(position)
    elif position == 10:
        print(position)
    else:
        position=position
def blitOffice():
    global eastLightState, westLightState, westDoorState, eastDoorState, curTime, _battery, lastPrint
    printCooldown=100
    if curTime - lastPrint > printCooldown:
        if (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bothAnimAll")
            lastPrint=curTime
            

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState and eastDoorState==False and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit both bonnie and chica Left Door")
            lastPrint=curTime
            
        
        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState==False and eastDoorState==False and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit both bonnie and chica")
            lastPrint=curTime
            
        
        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState==False and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit both bonnie and chica Lights Right Door")
            lastPrint=curTime
            
        
        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState==False and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit both bonnie and chica Right Door")
            lastPrint=curTime
    

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState and eastDoorState:
            screen.blit(chicalightbothdoor, (0, 0))
            lastPrint=curTime
            

        elif eastLightState and westLightState and westDoorState and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bonnie both lights and doors")
            lastPrint=curTime
            

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState and westDoorState and eastDoorState==False:
            screen.blit(officechica, (0, 0))
            lastPrint=curTime
            

        elif eastLightState and westLightState and westDoorState and eastDoorState==False and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bonnie both Lights Left Door")
            lastPrint=curTime
            

        elif chica.getRoom().lower() == "easthallcorner" and eastLightState and westLightState and westDoorState==False and eastDoorState:
            screen.blit(chicalightrightdoor, (0, 0))
            lastPrint=curTime
            

        elif eastLightState and westLightState and westDoorState==False and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bonnie both Lights Right Door")
            lastPrint=curTime
            

        elif _battery < 0:
            screen.blit(blackout, (0, 0))
            lastPrint=curTime
            

        elif eastLightState==False and westLightState and westDoorState==False and eastDoorState==False and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            screen.blit(officebonnie, (0, 0))
            lastPrint=curTime
            

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState==False and westDoorState==False and eastDoorState==False:
            screen.blit(officechica, (0, 0))
            lastPrint=curTime
            

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState==False and westDoorState==False and eastDoorState:
            screen.blit(chicarightdoor, (0, 0))
            lastPrint=curTime
            

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState==False and westDoorState and eastDoorState==False:
            screen.blit(chicaleftdoor, (0, 0))
            lastPrint=curTime
            

        elif (chica.getRoom().lower() == "easthallcorner" or chica.getRoom().lower()=="office") and eastLightState and westLightState==False and westDoorState and eastDoorState:
            screen.blit(bothdoorchica, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState==False and westLightState and westDoorState and eastDoorState==False and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bonnie left light left door")
            lastPrint=curTime
            

        elif eastLightState==False and westLightState and westDoorState==False and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bonnie left light right door")
            lastPrint=curTime
            
        
        elif eastLightState==False and westLightState and westDoorState and eastDoorState and (bonnie.getRoom().lower() == "westhallcorner" or bonnie.getRoom().lower()=="office"):
            print("will blit bonnie left light both doors")
            lastPrint=curTime
            
        
        elif eastLightState and westLightState and westDoorState and eastDoorState:
            screen.blit(allnoanim, (0, 0))
            lastPrint=curTime
            

        elif eastLightState and westLightState and westDoorState==False and eastDoorState:
            screen.blit(bothlightrightdoor, (0, 0))
            lastPrint=curTime


        elif eastLightState and westLightState and westDoorState and eastDoorState==False:
            screen.blit(bothlightleftdoor, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState and westLightState==False and westDoorState and eastDoorState:
            screen.blit(bothdoorrightlight, (0, 0))
            lastPrint=curTime
            

        elif eastLightState==False and westLightState and westDoorState and eastDoorState:
            screen.blit(bothdoorleftlight, (0, 0))
            lastPrint=curTime
            

        elif eastLightState and westLightState==False and eastDoorState and westDoorState==False:
            screen.blit(rightdoorrightlight, (0, 0))
            lastPrint=curTime
            

        elif eastLightState==False and westLightState and eastDoorState==False and westDoorState:
            screen.blit(leftdoorleftlight, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState and westLightState==False and eastDoorState==False and westDoorState:
            screen.blit(leftdoorrightlight, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState==False and westLightState and eastDoorState and westDoorState==False:
            screen.blit(rightdoorleftlight, (0, 0))
            lastPrint=curTime
            

        elif eastLightState and westLightState and westDoorState==False and eastDoorState==False:
            screen.blit(bothlights, (0, 0))
            lastPrint=curTime
            
        elif eastLightState==False and westLightState==False and westDoorState and eastDoorState:
            screen.blit(bothdoors, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState and westLightState==False and westDoorState==False and eastDoorState==False:
            screen.blit(officerightlight, (0, 0))
            lastPrint=curTime
            

        elif eastLightState==False and westLightState==False and westDoorState and eastDoorState==False:
            screen.blit(officeleftdoor, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState==False and westLightState and westDoorState==False and eastDoorState==False:
            screen.blit(officeleftlight, (0, 0))
            lastPrint=curTime
            
        
        elif eastLightState==False and westLightState==False and westDoorState==False and eastDoorState:
            screen.blit(officerightdoor, (0, 0))
            lastPrint=curTime
            

        elif eastLightState==False and westLightState==False and westDoorState==False and eastDoorState==False:
            screen.blit(officenodoor, (0, 0))
            lastPrint=curTime
            
        

        pygame.display.flip()
        return lastPrint
def timeLeft():
    global _6am,timeCounter
    timeCounter=0
    _6am=False
    
    while timeCounter < 6:
        if timeCounter==0:
            print(f"It is {12}am")
        else:
            print(f"It is {timeCounter}am")
        time.sleep(75)
        timeCounter+=1
    if timeCounter==6:
        _6am=True
def camera(switch):
    global cameraState
    if switch == 0:
        cameraState = not cameraState
    elif switch != 0 and cameraState:
        cameraPos(switch)
def westLight():
    global westLightState
    westLightState = not westLightState
def eastLight():
    global eastLightState
    eastLightState = not eastLightState
def batteryDrain():
    """drains the battery based on how many things are turned on"""
    global batteryStacks, _battery
    while _battery>0:
        time.sleep(batteryStacks)
        _battery-=1
        print(f"{_battery}%")
def battery(): 
    """checks how many things are turned on and using battery"""
    global westDoorState, eastDoorState, cameraState, eastLightState, westLightState, batteryStacks
    batteryList=[westDoorState,eastDoorState,cameraState,eastLightState,westLightState]
    batteryCounter=0
    batteryStacks=6
    for _battery in batteryList:
        if _battery:
            batteryCounter+=1
    batteryStacks-=batteryCounter
def jumpFunc(jumpscare,name):
    """Checks if you have been attacked by an animatronic"""
    if jumpscare==False:
        if name == "Freddy":
            print("Freddy has left")
            return "ShowStage"
        elif name == "Chica":
            print("Chica has left")
            return "ShowStage"
        elif name == "Bonnie":
            print("Bonnie has left")
            return "ShowStage"
        else:
            print("Foxy has left")
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
    global jumpscare, _battery, _6am
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
    elif _battery <= 0:
        print("feddy jumpscare")
        sys.exit()
    elif _6am:
        print("You win brochacho")
        sys.exit()
def settingup():
    global screen, freddy, chica, bonnie, foxy, fredAI, chicaAI, bonnAI, foxyAI, animList, eastDoorState, westDoorState, gameGo, running, cameraState, batteryStacks, eastLightState, westLightState, jumpscare, _battery,clock, cooldown,lastPressedWLight,lastPressedELight,lastPressedCam,lastPressedEDoor, curTime, lastPressedWDoor, lastPrint
    cameraState=False
    batteryStacks=6
    eastLightState=False
    westLightState=False
    jumpscare=False
    _battery=100
    global running
    running = True
    clock = pygame.time.Clock()
    cooldown=333
    cooldownCam=200
    printCooldown=100
    lastPressedWLight=-cooldown
    lastPressedELight=-cooldown
    lastPressedCam=-cooldown
    lastPressedEDoor=-cooldown
    lastPressedWDoor=-cooldown
    lastPrint=-printCooldown
    
    pygame.display.set_caption("My Pygame Window")
    freddy = Anim("Freddy", freddif, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
    chica = Anim("Chica", chicadif, "ShowStage", ["ShowStage", "Dining", "Restrooms", "Kitchen", "EastHall","EastHallCorner"])
    bonnie = Anim("Bonnie", bonniedif, "ShowStage", ["ShowStage", "Dining", "Backstage", "SupplyCloset", "WestHall","WestHallCorner"])
    foxy = Anim("Foxy", foxydif, "PirateCove", ["PiratesCove", "Pirate1", "Pirate2","Pirate3","Running"])
    fredAI  = threading.Thread(target=freddy.animatronicMove, args=(freddy.getDiff(),), daemon=True)
    chicaAI = threading.Thread(target=chica.animatronicMove, args=(chica.getDiff(),), daemon=True)
    bonnAI  = threading.Thread(target=bonnie.animatronicMove, args=(bonnie.getDiff(),), daemon=True)
    foxyAI  = threading.Thread(target=foxy.animatronicMove, args=(foxy.getDiff(),), daemon=True)
    batteryThread = threading.Thread(target=batteryDrain, daemon=True)
    timeThread = threading.Thread(target=timeLeft, daemon=True)
    animList=[fredAI, chicaAI, bonnAI, foxyAI]
    eastDoorState = False
    westDoorState = False
    gameGo = True
    running = True
    curTime=pygame.time.get_ticks()
    pygame.display.flip()
    batteryThread.start()
    timeThread.start()
    fredAI.start()
    time.sleep(0.5)
    chicaAI.start()
    time.sleep(0.5)
    bonnAI.start()
    time.sleep(0.5)
    foxyAI.start()
    time.sleep(0.5)
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # User clicked the close button
                running = False
        curTime=pygame.time.get_ticks()
        
        
        isKill()
        battery()
        blitOffice()
        # Game logic (e.g., update object positions)
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            westDoorState=closeWest()
            time.sleep(0.3)
            if westDoorState==True:
                print("West door Closed")
            else:
                print("West Door Opened")
        if pressed[pygame.K_RIGHT]:
            eastDoorState=closeEast()
            time.sleep(0.3)
            if eastDoorState==True:
                print("East door Closed")
            else:
                print("East Door Opened")
            lastPressedEDoor=curTime
        if pressed[pygame.K_a]:
            if curTime - lastPressedWLight > cooldown:
                westLight()
                if westLightState:
                    print("West light turned on")
                else:
                    print("West light turned off")
                lastPressedWLight=curTime
        if pressed[pygame.K_d]:
            if curTime - lastPressedELight > cooldown:
                eastLight()
                if eastLightState:
                    print("east light turned on")
                else:
                    print("east light turned off")
                lastPressedELight=curTime
        if pressed[pygame.K_s]:
            if curTime - lastPressedCam > cooldown:
                camera(0)
                if cameraState:
                    print("Camera opened")
                else:
                    print("Camera Closed")
                lastPressedCam=curTime
        if pressed[pygame.K_1]:
            if curTime - lastPressedCam > cooldownCam:
                camera(1)
        elif pressed[pygame.K_2]:
            if curTime - lastPressedCam > cooldownCam:
                camera(2)
        elif pressed[pygame.K_3]:
            if curTime - lastPressedCam > cooldownCam:
                camera(3)
        elif pressed[pygame.K_4]:
            if curTime - lastPressedCam > cooldownCam:
                camera(4)
        elif pressed[pygame.K_5]:
            if curTime - lastPressedCam > cooldownCam:
                camera(5)
        elif pressed[pygame.K_6]:
            if curTime - lastPressedCam > cooldownCam:
                camera(6)
        elif pressed[pygame.K_7]:
            if curTime - lastPressedCam > cooldownCam:
                camera(7)
        elif pressed[pygame.K_8]:
            if curTime - lastPressedCam > cooldownCam:
                camera(8)
        elif pressed[pygame.K_9]:
            if curTime - lastPressedCam > cooldownCam:
                camera(9)
        elif pressed[pygame.K_0]:
            if curTime - lastPressedCam > cooldownCam:
                camera(10)
        

        


    # Drawing
    
    # Update the display
    pygame.display.flip() # or pygame.display.update()
settingup()
#Use of AI for pygame starter, fixing threads args and stopping all threads

pygame.quit()
