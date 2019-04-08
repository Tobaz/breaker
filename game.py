#Standard liraries
import sys, time
#Third party libraries
import pygame
#My libraries
from objects import Ball, Brick

#Initialization
pygame.init()

screenSize = screenWidth, screenHeight = 320, 240

screen = pygame.display.set_mode(screenSize)
tiles = pygame.image.load("sprites.png").convert()
collide = []
ball = Ball(tiles, loc=[160, 160])
#player = Player()
bricks = [Brick(tiles, 0, [40, 40]), Brick(tiles, 2, [80, 40]), Brick(tiles, 3, [120, 40])]

brickRects = []
for brick in bricks:
    brickRects.append(brick.rect)

#Main loop
while 1:
    #Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #Game logic
    if ball.rect.move(0, ball.speed[1]).collidelist(brickRects) > -1:
        ball.speed[1] = -ball.speed[1]
        ball.move([0, -ball.speed[1]])
    elif ball.rect.move([ball.speed[0], 0]).collidelist(brickRects) > -1:
        ball.speed[0] = -ball.speed[0]
        ball.move([-ball.speed[0], 0])

    ball.move(ball.speed)
    collide = ball.rect.collidelist(brickRects)    
    
    
    if ball.rect.left < 0 or ball.rect.right > screenWidth:
        ball.speed[0] = -ball.speed[0]
    if ball.rect.top < 0 or ball.rect.bottom > screenHeight:
        ball.speed[1] = -ball.speed[1]
    
    if collide > -1:
        bricks.pop(collide)
    brickRects.clear()
    for brick in bricks:
        brickRects.append(brick.rect)

    #Drawing
    screen.fill((0,0,0))

    for brick in bricks:
        screen.blit(brick.tex, brick.pos, brick.texPos)  #blit(image, position, area of image[tile])
    screen.blit(ball.tex, ball.pos, ball.texPos)

    pygame.display.flip()
    time.sleep(0.008)