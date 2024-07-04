import pygame
import sys

pygame.init()

size = WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption('DDA Line Drawing Algorithm')

def dda_draw(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x = x1
    y = y1

    for i in range(steps):
        screen.set_at((round(x), round(y)), 'white')
        x += x_inc
        y += y_inc


if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        dda_draw(20,20,300,300)
        pygame.display.flip()

