import pygame
import random
import time
import winsound

# initialize the pygame
pygame.init()

# creating screen(beware of two paranthesis)
screen = pygame.display.set_mode((800, 650))
# background
background = pygame.image.load("darksky.jpg")

# Title and Icon
pygame.display.set_caption("Space Invaders")
gameicon = pygame.image.load("spaceship.png")
pygame.display.set_icon(gameicon)

# player
playerimg = pygame.image.load("battleship.png")
playerx = 368
playery = 536
playerxchange = 0
playerychange = 0

# enemy and fire
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numberofenemy = 6
for i in range(numberofenemy):
    enemyimg.append(pygame.image.load("helicopter.png"))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(0, 115))
    enemyxchange.append(1.2)
    enemyychange.append(0)
fire = pygame.image.load("fire.png")
# bullet
# ready we cant see the bullet
# fire = the bullet is currently moving
bullet = pygame.image.load("bullet.png")
bulletxchange = 0
bulletychange = 4
bulletx = 0
bullety = 530
bulletstate = "ready"


# Score
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
texty = 10


def gameover(x, y):
    label = font.render("GAME OVER !!!", True, (255, 0, 0))
    screen.blit(label, (x, y))


def showscore(x, y):
    global score
    score = font.render(f"SCORE : {scorevalue}", True, (0, 0, 255))
    screen.blit(score, (x, y))


def motion(x, y):
    # blit function will show the image on the screen and therefore applied on screen
    screen.blit(playerimg, (x, y))


def enemy(enemyimg, x, y, i):
    screen.blit(enemyimg[i], (x[i], y[i]))


def firebullet(x, y):
    global bulletstate
    bulletstate = "fire"
    # for position of release of bullet
    screen.blit(bullet, (x + 16, y))


# playerx and playery will coincide with the top left corner of the playerimg

# game loop for sustaining the display
running = True
# a is just a value which signifies that if a = 0 game is running and if a = 1 then game should stop
a = 0
b = 0
while running:
    # filling the color using rgb
    screen.fill((20, 210, 210))
    # backgroung image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check the keystroke left or right
        # keydown for pressing and keyup for release of the key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -1
            if event.key == pygame.K_RIGHT:
                playerxchange = 1
            if event.key == pygame.K_SPACE and a != 1:
                if bulletstate == "ready":
                    bulletx = playerx
                    firebullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange = 0

    if a == 1:
        playerxchange = 0
    playerx += playerxchange
    if playerx >= 736:
        playerx = 736
    if playerx <= 0:
        playerx = 0

    # enemy motion
    for i in range(numberofenemy):
        enemyx[i] += enemyxchange[i]
        if enemyx[i] >= 736 or enemyx[i] <= 0:
            enemyychange[i] = 100
            enemyxchange[i] = -enemyxchange[i]
            enemyy[i] += enemyychange[i]

        if (
            bulletx > enemyx[i] - 32
            and bulletx < enemyx[i] + 48
            and bullety > enemyy[i] + 30
            and bullety < enemyy[i] + 45
        ):
            scorevalue += 1
            winsound.Beep(1500, 20)
            bulletstate = "ready"
            bulletx = playerx
            bullety = 480
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(0, 115)
        if (
            enemyx[i] + 64 >= playerx
            and enemyx[i] <= playerx + 64
            and enemyy[i] + 64 > playery
        ):
            gameover(325, 320)
            if b == 0:
                winsound.Beep(300, 40)
                b += 1
            a = 1
            enemyxchange.clear()
            for i in range(numberofenemy):
                enemyxchange.append(0)
        enemy(enemyimg, enemyx, enemyy, i)

    # bullet motion
    if bulletstate == "fire":
        firebullet(bulletx, bullety)
        bullety -= bulletychange
    if bullety <= 0:
        bulletstate = "ready"
        bulletx = playerx
        bullety = 480

    motion(playerx, playery)
    showscore(textx, texty)

    pygame.display.update()
