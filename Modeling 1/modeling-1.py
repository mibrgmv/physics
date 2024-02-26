import pygame


def update_velocity(v1, m1, v2, m2):
    return ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2


WIDTH = 800
HEIGHT = 400
SIZE = 100
BLUE = (0, 0, 60)
CREAM = (255, 255, 220)
FILLINGS = [(60, 0, 0), (70, 30, 0), (60, 55, 0), (0, 60, 0), (10, 50, 60), (0, 0, 60), (60, 0, 60)]
x1, y1 = 600, HEIGHT - SIZE - 100
x2, y2 = 100, HEIGHT - SIZE - 100

v1, v2 = -3, 0
m1, m2 = 10000, 1
no_of_collisions = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('futura', 25)

pause = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_SPACE:
                pause += 1
        if event.type == pygame.QUIT:
            pygame.quit()

    if pause % 2 == 0:
        x1 += v1

        if x2 + SIZE >= x1 or x1 + SIZE < x2:
            v1, v2 = update_velocity(v1, m1, v2, m2), update_velocity(v2, m2, v1, m1)
            no_of_collisions += 1

        x2 += v2
        if x2 <= 0:
            v2 *= -1
            no_of_collisions += 1

    t1 = x1 if x1 >= SIZE else SIZE
    t2 = x2 if x1 >= SIZE else 0

    screen.fill(BLUE)
    screen.blit(font.render('collisions: ' + str(no_of_collisions), True, CREAM), (0, 0))
    pygame.draw.rect(screen, CREAM, (t2, y2, SIZE, SIZE))
    pygame.draw.rect(screen, CREAM, (t1, y1, SIZE, SIZE))
    pygame.draw.line(screen, CREAM, (0, HEIGHT), (WIDTH, HEIGHT), 200)
    pygame.display.flip()
    clock.tick(60)
