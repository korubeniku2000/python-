import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("test")
    font = pygame.font.Font(None, 50)

    while (1):
        screen.fill((255, 255, 255))
        text = font.render("Hello, World!", True, (0, 0, 0))
        screen.blit(text, [400, 300])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
