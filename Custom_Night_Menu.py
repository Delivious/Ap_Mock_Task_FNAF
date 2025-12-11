import pygame

pygame.init()
# Ori made all of this
screen_width = 2500
screen_height = 1500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (68, 67, 68)
font = pygame.font.SysFont('Arial', 72)
font2 = pygame.font.SysFont('Arial', 62)
freddy = pygame.image.load("fredder.png")
bonnie = pygame.image.load("bonnie.png")
chica = pygame.image.load("chica.png")
foxy = pygame.image.load("froxy.png")
diflevels=font2.render('(0-2)easy, (3-6)med, (7-12)hard, (12+)extreme', True, WHITE)
ready= pygame.Rect((1100,950),(230,150))
ready_text = font.render('Ready', True, WHITE)
fredname = font.render('Freddy', True, WHITE)


fredAdd = pygame.Rect((400,560),(75,100))
fredminus = pygame.Rect((665,560),(75,100))
freddif=0

chicaname = font.render('Chica', True, WHITE)
chicaAdd = pygame.Rect((850,560),(75,100))
chicaminus = pygame.Rect((1115,560),(75,100))
chicadif=0

bonniename = font.render('Bonnie', True, WHITE)
bonnieAdd = pygame.Rect((1300,560),(75,100))
bonnieminus = pygame.Rect((1565,560),(75,100))
bonniedif=0

foxyname = font.render('Foxy', True, WHITE)
foxyAdd = pygame.Rect((1750,560),(75,100))
foxyminus = pygame.Rect((2015,560),(75,100))
foxydif=0

screen2 = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Custom Night Menu")
def difficuties():
    global freddif, chicadif, foxydif, bonniedif, running

    # draw images and buttons
    screen2.blit(freddy, (400, 200))
    screen2.blit(fredname, (460, 100))
    pygame.draw.rect(screen2, GREY, fredAdd)
    pygame.draw.rect(screen2, GREY, fredminus)
    pygame.draw.lines(screen2, WHITE, False, [[420.5,610],[450,640],[420.5,610],[450,580]], 5)
    pygame.draw.lines(screen2, WHITE, False, [[717.5,610],[687,640],[717.5,610],[687,580]], 5)

    # handle one click per event
    

    # CLEAR number area (smaller, fits between the two grey rectangles)
    pygame.draw.rect(screen2, BLACK, (485, 560, 180, 100))  

    # draw number
    screen2.blit(font.render(str(freddif), True, WHITE), (550, 580))


    screen2.blit(chica, (850, 200))
    screen2.blit(chicaname, (920, 100))
    pygame.draw.rect(screen2, GREY, chicaAdd)
    pygame.draw.rect(screen2, GREY, chicaminus)
    pygame.draw.lines(screen2, WHITE, False, [[872.5,610],[902,640],[872.5,610],[902,580]], 5)
    pygame.draw.lines(screen2, WHITE, False, [[1162.5,610],[1132,640],[1162.5,610],[1132,580]], 5)

    # CLEAR number area (smaller, fits between the two grey rectangles)
    pygame.draw.rect(screen2, BLACK, (935, 560, 180, 100))  

    # draw number
    screen2.blit(font.render(str(chicadif), True, WHITE), (1000, 580))

    screen2.blit(bonnie, (1300, 200))
    screen2.blit(bonniename, (1370, 100))
    pygame.draw.rect(screen2, GREY, bonnieAdd)
    pygame.draw.rect(screen2, GREY, bonnieminus)
    pygame.draw.lines(screen2, WHITE, False, [[1317.5,610],[1347,640],[1317.5,610],[1347,580]], 5)
    pygame.draw.lines(screen2, WHITE, False, [[1622.5,610],[1592,640],[1622.5,610],[1592,580]], 5)

    # CLEAR number area (smaller, fits between the two grey rectangles)
    pygame.draw.rect(screen2, BLACK, (1385, 560, 180, 100))  

    # draw number
    screen2.blit(font.render(str(bonniedif), True, WHITE), (1450, 580))

    screen2.blit(foxy, (1750, 200))
    screen2.blit(foxyname, (1820, 100))
    pygame.draw.rect(screen2, GREY, foxyAdd)
    pygame.draw.rect(screen2, GREY, foxyminus)
    pygame.draw.lines(screen2, WHITE, False, [[1767.5,610],[1797,640],[1767.5,610],[1797,580]], 5)
    pygame.draw.lines(screen2, WHITE, False, [[2067.5,610],[2037,640],[2067.5,610],[2037,580]], 5)

    # CLEAR number area (smaller, fits between the two grey rectangles)
    pygame.draw.rect(screen2, BLACK, (1835, 560, 180, 100))  

    # draw number
    screen2.blit(font.render(str(foxydif), True, WHITE), (1900, 580))

    screen2.blit(diflevels, (600, 825))
    pygame.draw.rect(screen2, GREY, ready)
    screen2.blit(ready_text, (1115, 985))

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            mouse_pos = event.pos
            if fredAdd.collidepoint(mouse_pos):
                if freddif < 20:
                    freddif += 1
            elif fredminus.collidepoint(mouse_pos):
                if freddif > 0:
                    freddif -= 1

            if chicaAdd.collidepoint(mouse_pos):
                if chicadif < 20:
                    chicadif += 1
            elif chicaminus.collidepoint(mouse_pos):
                if chicadif > 0:
                    chicadif -= 1

            if bonnieAdd.collidepoint(mouse_pos):
                if bonniedif < 20:
                    bonniedif += 1
            elif bonnieminus.collidepoint(mouse_pos):
                if bonniedif > 0:
                    bonniedif -= 1

            if foxyAdd.collidepoint(mouse_pos):
                if foxydif < 20:
                    foxydif += 1
            elif foxyminus.collidepoint(mouse_pos):
                if foxydif > 0:
                    foxydif -= 1
            if ready.collidepoint(mouse_pos):
                print(f"Starting night with difficulties - Freddy: {freddif}, Chica: {chicadif}, Bonnie: {bonniedif}, Foxy: {foxydif}")
                running = False  # exit menu
                screen2.fill(BLACK)
                from night1 import settingup
                settingup()  # call Custom Night function


def CN():
    global running
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
        difficuties()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
# ^ Use of AI for pygame starter ^
# Use of AI to fix the problem of clicking multiple times without actually clicking multiple times ^
CN()