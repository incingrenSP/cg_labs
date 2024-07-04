import pygame
import sys

pygame.init()

size = WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bresenham's Algorithm")

def draw_bresen(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    lx = 1 if x2 > x1 else -1
    ly = 1 if y2 > y1 else -1
    x, y = x1, y1

    if dx > dy:
        p = 2 * dy - dx
        while x != x2:
            if p < 0:
                x += lx
                p += 2 * dy
            else:
                x += lx
                y += ly
                p += 2 * dy - 2 * dx

            screen.set_at((x, y), 'white')
    else:
        p = 2 * dx - dy
        while y != y2:
            if p < 0:
                y += ly
                p += 2 * dx
            else:
                x += lx
                y += ly
                p += 2 * dx - 2 * dy
            screen.set_at((x, y), 'white')

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        draw_bresen(20,20,500,500)
        pygame.display.update()