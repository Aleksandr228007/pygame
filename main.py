import pygame
import random
from time import sleep

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

bound = 20
border_l = bound
border_r = WIDTH - bound
border_u = bound
border_d = HEIGHT

x, y = WIDTH // 2, HEIGHT // 2
radius = 10
velocity = 8
vx = velocity * random.uniform(-1, 1)
vy = velocity * random.uniform(-1, 1)

paddle_height = 10
paddle_width = 80
xp = (WIDTH - paddle_width) // 2
yp = HEIGHT - bound -5
vp = 10

score = 0
num = 1.5


def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # Верхня межа
    pygame.draw.circle(win, green, (int(x), int(y)), radius)  # М'яч
    pygame.draw.rect(win, green, (xp, yp, paddle_width, paddle_height))  # Майданчик
    pygame.display.update()


def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    font = pygame.font.Font(path, 30)
    text = f"Your points: {score}"
    rendered_text = font.render(text, 1, white)
    win.blit(rendered_text, (WIDTH // 2 - 100, HEIGHT // 3))
    pygame.display.update()


run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > border_l:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < border_r - paddle_width:
        xp += vp


    x += vx
    y += vy

    if x - radius < border_l or x + radius > border_r:
        vx = -vx
    if y - radius < border_u:
        vy = -vy

    if y + radius >= yp:
        if xp <= x + vx <= xp + paddle_width:
            vy = -vy
            vx *= num
            vy *= num
            score += 1
        else:
            drawScore()
            sleep(10)
            run = False

    drawWindow()

pygame.quit()
