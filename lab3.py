import pygame, sys

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Midpoint Circle Algorithm')

def midpoint(xc: int, yc: int, radius: int, color: str):
    x = 0
    y = radius
    p = 1 - radius
    while x <= y:
        screen.set_at((xc + x, yc + y), color)  # 1st octant
        screen.set_at((xc - x, yc + y), color)  # 2nd octant
        screen.set_at((xc + x, yc - y), color)  # 3rd octant
        screen.set_at((xc - x, yc - y), color)  # 4th octant
        screen.set_at((xc + y, yc + x), color)  # 5th octant
        screen.set_at((xc - y, yc + x), color)  # 6th octant
        screen.set_at((xc + y, yc - x), color)  # 7th octant
        screen.set_at((xc - y, yc - x), color)  # 8th octant
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1

if __name__ == '__main__':
    x, y = 200, 200
    r = 100
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        midpoint(x, y, r, 'blue')
        midpoint(x + 110, y + 100, r, 'yellow')
        midpoint(x + 220, y, r, 'white')
        midpoint(x + 330, y + 100, r, 'green')
        midpoint(x + 440, y, r, 'red')
        pygame.display.update()

    pygame.quit()
    sys.exit()
    