import pygame, sys, math

TOP = [250, 300]
LEFT = [200, 50]
RIGHT = [300, 100]

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('2D Transformations')

def translate(tx, ty):
    global TOP, LEFT, RIGHT
    for coords in TOP, LEFT, RIGHT:
        coords[0] = coords[0] + tx
        coords[1] = coords[1] + ty

def rotate(theta):
    global TOP, LEFT, RIGHT
    for coords in TOP, LEFT, RIGHT:
        x, y = coords[0], coords[1]
        coords[0] = x * math.cos(theta) - y * math.sin(theta)
        coords[1] = x * math.sin(theta) + y * math.cos(theta)

def scale(sx, sy):
    global TOP, LEFT, RIGHT
    for coords in TOP, LEFT, RIGHT:
        coords[0] = coords[0] * sx
        coords[1] = coords[1] * sy

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    translate(170, 60)
                elif event.key == pygame.K_2:
                    rotate(math.radians(45))
                elif event.key == pygame.K_3:
                    scale(2,2)
        screen.fill('white')
        pygame.draw.polygon(screen, 'black', [TOP, RIGHT, LEFT], 2)
        pygame.display.update()