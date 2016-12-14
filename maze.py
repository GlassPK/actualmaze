# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1250
HEIGHT = 975
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COIN = (255, 255, 0)
GREEN = (0, 255, 0)
PlayerColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
WALL = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


# Make a player
player =  [137, 0, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
wall1 =  [100, 0, 25, 175]
wall2 =  [175, 0, 25, 175]
wall3 =  [40, 225, 180, 25]
wall4 =  [40, 0, 25, 225]
wall5 =  [220, 225, 25, 300]
wall6 =  [295, 225, 25, 390]
wall7 =  [20, 550, 275, 25]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

# Make coins
coin1 = [320, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 175, 25, 25]
coin4 = [70, 0, 25, 25]
coin5 = [70, 30, 25, 25]
coin6 = [70, 60, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5, coin6]

randomcolors = False
# Game loop
win = False
done = False
score = 0

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                PlayerColor = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
            if event.key == pygame.K_r:
                randomcolors = not randomcolors

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0
        
    if left:
        player_vx = -player_speed
    elif right:
        player_vx = player_speed
    else:
        player_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]

    '''filthy prank'''
    if player[0] >= 40 and player[0] <= 100:
        if player[1] <= 70:
            prankwall = [65, 150, 35, 25]
            walls.append(prankwall)
    ''' here is where you should resolve player collisions with screen edges '''
    if player[1] < 0:
        player[1] = 0
    if player[1] + player[3] > HEIGHT:
        player[1] = HEIGHT - player[3]
    if player[0] < 0:
        player[0] = 0
    if player[0] + player[2] > WIDTH:
        player[0] = WIDTH - player[2]
    


    ''' get the coins '''
    #coins = [c for c in coins if not intersects.rect_rect(player, c)]

    

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    if randomcolors:
        PlayerColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.rect(screen, PlayerColor, player)

    
    for w in walls:
        if randomcolors:
            WALL = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.rect(screen, WALL, w)
        
    #COIN = (random.randint(30,255),random.randint(30,255),random.randint(30,255))
    
    
    for c in coins:
        if randomcolors:
            COIN = (random.randint(30,255),random.randint(30,255),random.randint(30,255))
        pygame.draw.rect(screen, COIN, c)

    hit_list = [c for c in coins if intersects.rect_rect(player, c)]

    for hit in hit_list:
        coins.remove(hit)
        score += 100
    if len(coins) == 0:
        win = True
    
        
    if win:
        font = pygame.font.Font(None, 64)
        WINCOLOR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        text = font.render("You Win!", 1, WINCOLOR)
        screen.blit(text, [(WIDTH/2)-96, (HEIGHT/2)-32]) 

    font = pygame.font.Font(None, 64)
    text1 = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text1, [0, 0])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
