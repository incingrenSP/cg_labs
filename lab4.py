import pygame, sys, math, random

angle = 0
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Midpoint Ellipse Algorithm')

def circle(center: tuple, major: int, minor: int, radius: int, color: str):
    global angle
    angle += 1
    x = center[0] + int(major * math.cos(angle))
    y = center[1] + int(minor * math.sin(angle))
    pygame.draw.circle(screen, color, (x, y), radius)

def ellipse(xc: int, yc: int, rx: int, ry: int, color: str):
    x = 0
    y = ry
    p1 = round(ry**2 + 1/4 * rx**2 - ry * rx**2)
    while 2 * ry**2 * x <= 2 * rx**2 * y:
        if p1 < 0:
            x += 1
            p1 += 2 * ry**2 * x + ry**2
        else:
            x += 1
            y -= 1
            p1 += 2 * ry**2 * x  - 2 * rx**2 * y + ry**2
        
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        screen.set_at((xc - x, yc + y), color)

    p2 = round(ry**2 * (x + 1/2)**2 + rx**2 * (y-1)**2 - rx**2 * ry**2)
    while y > 0:
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx**2 * y + rx**2
        else:
            x += 1
            y -= 1
            p2 += 2* ry**2 * x - 2* rx**2 * y + rx**2
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        screen.set_at((xc - x, yc + y), color)

if __name__ == '__main__':
    running = True
    center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # orbits
        ellipse(center[0], center[1], 50*2, 20*2, 'white')
        ellipse(center[0], center[1], 80*2, 30*2, 'white')
        ellipse(center[0], center[1], 110*2, 40*2, 'white')
        ellipse(center[0], center[1], 140*2, 50*2, 'white')
        ellipse(center[0], center[1], 190*2, 70*2, 'white')
        ellipse(center[0], center[1], 230*2, 90*2, 'white')
        ellipse(center[0], center[1], 260*2, 110*2, 'white')
        ellipse(center[0], center[1], 280*2, 130*2, 'white')


        #  planets
        circle(center, 0, 0, 30, 'yellow')
        circle(center, 100, 40, 5, 'brown')
        circle(center, 160, 60, 9, 'white')
        circle(center, 220, 80, 13, 'blue')
        circle(center, 280, 100, 7, 'red')
        circle(center, 380, 140, 22, 'orange')
        circle(center, 460, 180, 18, 'yellow')
        circle(center, 520, 220, 13, 'gray')
        circle(center, 560, 260, 15, 'light blue')

        pygame.display.update()
        
    pygame.quit()
    sys.exit()


    