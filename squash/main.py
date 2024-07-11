import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
TOP_PANEL=50
BG = (55,55,55)

FONT = pygame.font.SysFont("Consolas", int(SCREEN_WIDTH/20))

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT +TOP_PANEL))
pygame.display.set_caption("Squash")

CLOCK = pygame.time.Clock()

# Paddles
player = pygame.Rect(0, 0, 60, 60)
player.center = (200,550)
player_score = 0
high_score = 0 

# Ball
dia=18
ball = pygame.Rect(0, 0, dia, dia)
ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

x_speed, y_speed = 0,0

#load images
court_image=pygame.image.load("assets/sqaush_court.jpeg").convert_alpha()
ball_image=pygame.image.load("assets/ball.png").convert_alpha()
player_image=pygame.image.load("assets/player.png").convert_alpha()


run=True
while run:
    keys_pressed = pygame.key.get_pressed()
  
    #to start game, press spacebar
    if keys_pressed[pygame.K_SPACE] and x_speed == 0 and y_speed == 0:
        x_speed,y_speed=random.choice([1, -1]), random.choice([1, -1])

    if keys_pressed[pygame.K_RIGHT]:
        if player.right < SCREEN_WIDTH:
            player.right += 2
    if keys_pressed[pygame.K_LEFT]:
        if player.left > 2 :
            player.left -= 2
    if keys_pressed[pygame.K_UP]:
        if player.top > (SCREEN_HEIGHT+TOP_PANEL)/2:
            player.top -= 2
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < SCREEN_HEIGHT+TOP_PANEL :
            player.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if ball.y >= SCREEN_HEIGHT+TOP_PANEL:
        ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        x_speed, y_speed = 0,0
        high_score = max(player_score, high_score)
        player_score = 0
    if ball.y <= 50:
        y_speed = 1
    if ball.x <= 0:
        x_speed = 1
    if ball.x >= SCREEN_WIDTH:
        x_speed = -1
    if player.left <= ball.x <= player.right and ball.y == player.top :
        player_score+=1
        y_speed = -1

    ball.x += x_speed * 1.5
    ball.y += y_speed * 1.5

    SCREEN.fill("Black")

    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.circle(SCREEN, "white", ball.center, 10)

    #draw court
    SCREEN.blit(court_image,(0,TOP_PANEL))
    # #draw play ball
    SCREEN.blit(ball_image, (ball.x,ball.y))
    # #draw player
    SCREEN.blit(player_image, (player.x,player.y))

    #display text
    player_score_text = FONT.render("SCORE: "+str(player_score), True, "white")
    player_high_score_text = FONT.render("HIGH SCORE: "+str(high_score), True, "white")

    SCREEN.blit(player_score_text,(10,15))
    SCREEN.blit(player_high_score_text,(220,15))



    pygame.display.update()
    CLOCK.tick(250)

pygame.quit()