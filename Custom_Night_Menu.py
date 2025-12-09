import pygame

pygame.init()

screen_width = 2500
screen_height = 1500
WHITE = (255, 255, 255)

screen2 = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Custom Night Menu")


def CN():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen2.fill(WHITE)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
# ^ Use of AI for pygame starter ^