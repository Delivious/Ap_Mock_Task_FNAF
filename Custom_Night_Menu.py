import pygame

pygame.init()

screen_width = 2500
screen_height = 1500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

fredAdd = pygame.Rect(100, 100, 100)
fredRemove = pygame.Rect(100, 100, 100)
chicAdd = pygame.Rect(100, 100, 100)
chicRemove = pygame.Rect(100, 100, 100)
bonnAdd = pygame.Rect(100, 100, 100)
bonnRemove = pygame.Rect(100, 100, 100)
foxyAdd = pygame.Rect(100, 100, 100)
foxyRemove = pygame.Rect(100, 100, 100)

screen2 = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Custom Night Menu")
def freddySec(event,fredNum):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
            if fredAdd.collidepoint(event.pos):
                fredNum+=1
                return fredNum
def CN():
    running = True
    clock = pygame.time.Clock()
    fredNum=0
    chicNum=0
    bonnNum=0
    foxyNum=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            fredNum=freddySec(event,fredNum)
        screen2.fill(WHITE)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
# ^ Use of AI for pygame starter ^