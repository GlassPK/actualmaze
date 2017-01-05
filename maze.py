# Imports
import pygame
import intersects
import random
import wall_list


# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 750
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze Game"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

time_remaining = 120
ticks = 0
#define functions 
def format_time(seconds):
    m = seconds // 60
    s = seconds % 60

    if s < 10:
        s = "0" + str(s)

    return str(m) + ":" + str(s)

def lock(x, y):
    pygame.draw.rect(screen, BLACK, [x, y+12, 18, 12])
    pygame.draw.rect(screen, BLACK, [x+5, y+6, 8, 2])
    pygame.draw.rect(screen, BLACK, [x+5, y+8, 2, 4])
    pygame.draw.rect(screen, BLACK, [x+11, y+8, 2, 4])

def key(color, x, y):
    if color == 1:
        COLOR = RED
    if color == 2:
        COLOR = GREEN
    if color == 3:
        COLOR = BLUE

    pygame.draw.rect(screen, COLOR, [x, y, 12, 4])
    pygame.draw.rect(screen, COLOR, [x, y+4, 4, 4])
    pygame.draw.rect(screen, COLOR, [x, y+8, 12, 4])
    pygame.draw.rect(screen, COLOR, [x+8, y+4, 4, 4])
    pygame.draw.rect(screen, COLOR, [x+4, y+12, 4, 16])
    pygame.draw.rect(screen, COLOR, [x+8, y+16, 4, 4])
    pygame.draw.rect(screen, COLOR, [x+8, y+24, 4, 4])
    
# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COIN = (255, 255, 0)
GREEN = (0, 255, 0)
PlayerColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
WALL = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


# Make a player
player =  [25, 25, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
walls = wall_list.wall_list()

# Make coins


coins = []

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

    '''if player[0] >= 40 and player[0] <= 100:
        if player[1] <= 70:
            prankwall = [65, 150, 35, 25]
            walls.append(prankwall)'''
    
    ''' here is where you should resolve player collisions with screen edges '''

    ticks += 1

    if ticks % refresh_rate == 0:
        time_remaining -= 1

    if time_remaining == 0:
        lose = True


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

    #Draw locks
    #Blue
    pygame.draw.rect(screen, BLUE, [225, 550, 25, 25])
    lock(227, 548)
    #Green
    pygame.draw.rect(screen, GREEN, [25, 475, 25, 25])
    lock(27, 472)
    #Red
    pygame.draw.rect(screen, RED, [175, 450, 25, 25])
    lock(177, 448)
    #Draw keys
    key(3, 625, 75)
    
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
    
    #Timer
    font = pygame.font.Font(None, 64)
    timer_text = font.render(format_time(time_remaining), True, WHITE)
    screen.blit(timer_text, [900, 0])
    
    '''if win:
        font = pygame.font.Font(None, 64)
        WINCOLOR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        text = font.render("You Win!", 1, WINCOLOR)
        screen.blit(text, [(WIDTH/2)-96, (HEIGHT/2)-32])  '''

    font = pygame.font.Font(None, 64)
    text1 = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text1, [0, 0])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
