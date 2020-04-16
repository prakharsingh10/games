import pygame
import math
import winsound
import time
import random

# import

pygame.init()

screen = pygame.display.set_mode((700, 500))

# mariocreation
marioimg = pygame.image.load("001-jogging.png")
mariox = 150
marioy = 400
marioychange = 0


def mario(x, y):
    screen.blit(marioimg, (x, y))


# score
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf", 32)
font1 = pygame.font.Font("freesansbold.ttf", 48)
textx = 10
texty = 10


def score(x, y):
    score = font.render(f"SCORE : {scorevalue}", True, (50, 50, 50))
    screen.blit(score, (x, y))


# game over
def gameover():
    label = font1.render("GAME OVER !!!", True, (255, 0, 0))
    screen.blit(label, (190, 210))


# sun
sunimg = pygame.image.load("sunny.png")
sunx = 500
suny = 15
sunxchange = -0.005


def sun(x, y):
    screen.blit(sunimg, (x, y))


# hurdle
hurdleimg = pygame.image.load("002-hurdles.png")
hurdlex = random.randint(1200, 1800)
hurdley = 400
hurdlexchange = -1.5


def hurdle(x, y):
    screen.blit(hurdleimg, (x, y))


# game name and icon
gameicon = pygame.image.load("running.png")
pygame.display.set_icon(gameicon)
pygame.display.set_caption("Runner")

# palm tree
listbird = []
for i in range(15):
    listbird.append(700 + i)

for i in range(150):
    listbird.append(3500 + i)
birdxchange = -1.5
birdx = 2000
birdy = 400 - 300
birdimg = pygame.image.load("003-bird.png")


def bird(x, y):
    screen.blit(birdimg, (x, y))


ta = 0
running = True
a = 0
while running:

    screen.fill((0, 0, 0))
    if sunx > 260:
        screen.fill((sunx - 261, sunx - 261, sunx - 261))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (
                math.sqrt(
                    float(mariox - hurdlex) * float(mariox - hurdlex)
                    + float(marioy - hurdley) * float(marioy - hurdley)
                )
                > 43.0
            ):
                marioychange = -1
                winsound.Beep(1500, 10)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and (
                    math.sqrt(
                        float(mariox - hurdlex) * float(mariox - hurdlex)
                        + float(marioy - hurdley) * float(marioy - hurdley)
                    )
                    > 43
                ):
                    marioychange = -1
    # mario jump smoothness
    if marioy > 305 and marioy < 350 and marioychange < 0:
        marioychange = -0.87
    if marioy >= 260 and marioy < 305 and marioychange < 0:
        marioychange = -0.8
    if marioy >= 245 and marioy < 260 and marioychange < 0:
        marioychange = -0.72
    if marioy >= 238 and marioy < 245 and marioychange < 0:
        marioychange = -0.53
    if marioy >= 235 and marioy < 238 and marioychange < 0:
        marioychange = -0.3
    if marioy < 235:
        marioychange = 1
    if marioy > 400:
        marioychange = 0
        marioy = 400
    marioy += marioychange

    hurdlex += hurdlexchange
    if hurdlex <= -65:
        hurdlex = random.randint(1200, 1800)
        hurdley = 400
        scorevalue += 10
    if (
        math.sqrt(
            (mariox - hurdlex) * (mariox - hurdlex)
            + (marioy - hurdley) * (marioy - hurdley)
        )
        < 43
    ):
        hurdlexchange = 0
        marioychange = 0
        birdxchange = 0
        sunxchange = 0
        gameover()
        a += 1
        if a == 1:
            winsound.Beep(3000, 300)

    if (
        math.sqrt(
            (mariox - birdx) * (mariox - birdx) + (marioy - birdy) * (marioy - birdy)
        )
        < 43
    ):
        hurdlexchange = 0
        marioychange = 0
        birdxchange = 0
        sunxchange = 0
        gameover()
        a += 1
        if a == 1:
            winsound.Beep(3000, 300)
    birdx += birdxchange
    if birdx <= -65:
        birdx = random.choice(listbird)
        birdy = random.randint(0, 330)
        scorevalue += 5
    hurdle(hurdlex, hurdley + 12)
    bird(birdx, birdy)
    mario(mariox, marioy)
    score(10, 10)
    sunx += sunxchange
    if sunx < 65:
        sunx = -65
        sunxchange = 0
    sun(sunx, suny)
    pygame.display.update()
