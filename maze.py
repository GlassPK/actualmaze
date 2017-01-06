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

stage = 1
# Timer
clock = pygame.time.Clock()
refresh_rate = 60
begintime = 60
time_remaining = 60
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
YELLOW = (255, 255, 0)

#make goals
bluebox1 = [75, 600, 50, 10]
bluebox2 = [75, 600, 10, 50]
bluebox3 = [75, 650, 50, 10]
bluebox4 = [125, 600, 10, 60]

greenbox1 = [63, 588, 75, 10]
greenbox2 = [63, 588, 10, 75]
greenbox3 = [63, 663, 75, 10]
greenbox4 = [138, 588, 10, 85]

redbox1 = [50, 575, 100, 10]
redbox2 = [50, 575, 10, 100]
redbox3 = [150, 575, 10, 100]
redbox4 = [50, 675, 110, 10]

bluetouch = False
greentouch = False
redtouch = False

bluelock = [225, 550, 25, 25]
redlock = [175, 450, 25, 25]
greenlock = [25, 475, 25, 25] 

bluegoal = [bluebox1, bluebox2, bluebox3, bluebox4]
redgoal = [redbox1, redbox2, redbox3, redbox4]
greengoal = [greenbox1, greenbox2, greenbox3, greenbox4]
# Make a player
player =  [25, 25, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
walls = wall_list.wall_list()

#make toggle walls

switch = [452, 703, 20, 20]

switchwall1 = [900, 500, 75, 25]
switchwall2 = [825, 475, 25, 25]

switchwalls = [switchwall1, switchwall2]

# Make key hitboxes
bluekey = [944, 34, 14, 28]
greenkey = [455, 35, 14, 28]
redkey = [944, 459, 14, 28]


blukeylist = [bluekey]
grnkeylist = [greenkey]
rdkeylist = [redkey]

haskey_blue = False
haskey_green = False
haskey_red = False

switched = False
randomcolors = False
# Game loop
win = False
done = False
score = 0
stage = 1
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

    if not redtouch:
        for w in redgoal:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    if not greentouch:
        for w in greengoal:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    if not bluetouch:
        for w in bluegoal:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

    if not switched:
        for w in switchwalls:
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

    if not redtouch:
        for w in redgoal:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

    if not bluetouch:
        for w in bluegoal:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

    if not greentouch:
        for w in greengoal:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

    if not switched:
        for w in switchwalls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

    if intersects.rect_rect(player, switch):
        switched = True

    if haskey_blue:
        if intersects.rect_rect(player, bluelock):
            bluetouch = True
    if haskey_green:
        if intersects.rect_rect(player, greenlock):
            greentouch = True
    if haskey_red:
        if intersects.rect_rect(player, redlock):
            redtouch = True
                            
    for b in blukeylist:
        if intersects.rect_rect(player, b):
            haskey_blue = True

    for g in grnkeylist:
        if intersects.rect_rect(player, g):
            haskey_green = True

    for r in rdkeylist:
        if intersects.rect_rect(player, r):
            haskey_red = True

    
    ''' win '''
    winblock = [95, 620, 20, 20]
    if intersects.rect_rect(player, winblock):
        win = True
    
    
    '''warps'''

    if player[1] == -25 and player_vy < 2:
        player[0] = 700
        player[1] = 775

    if player[0] == -25 and player_vx < 2:
        player[0] = 1025
        player[1] = 225

    if player[0] == 1025 and player_vx > 2:
        player[0] = -25
        player[1] = 25

    if player[1] == 775 and player_vy > 2:
        player[0] = 25
        player[1] = -25

        
    '''filthy prank'''

    '''if player[0] >= 40 and player[0] <= 100:
        if player[1] <= 70:
            prankwall = [65, 150, 35, 25]
            walls.append(prankwall)'''
    
    ''' here is where you should resolve player collisions with screen edges '''

    
    if not player[0] < 75:
        if not player[0] == 700 and player[1] > 700:
            if not player[0] > 975 and player[1] == 225:

                if player[1] < 0:
                    player[1] = 0
                if player[1] + player[3] > HEIGHT:
                    player[1] = HEIGHT - player[3]
                if player[0] < 0:
                    player[0] = 0
                if player[0] + player[2] > WIDTH:
                    player[0] = WIDTH - player[2]
    screen.fill(BLACK)


    
    
    '''timer stuff'''
   
   

    ticks += 1

    if ticks % refresh_rate == 0:
        time_remaining -= 1

    if time_remaining == 0:
        lose = True


    ''' get the coins '''
    #coins = [c for c in coins if not intersects.rect_rect(player, c)]

    

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    #screen.fill(BLACK)
    if randomcolors:
        PlayerColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.rect(screen, PlayerColor, player)

    
    for w in walls:
        if randomcolors:
            WALL = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.rect(screen, WALL, w)

    if not switched:
        for w in switchwalls:
            pygame.draw.rect(screen, YELLOW, w)

    pygame.draw.rect(screen, YELLOW, switch)

    #Draw locks
    #Blue
    
    pygame.draw.rect(screen, BLUE, [225, 550, 25, 25])
    if haskey_blue == False:
        lock(227, 548)
    #Green
    pygame.draw.rect(screen, GREEN, [25, 475, 25, 25])
    if haskey_green == False:
        lock(27, 472)
    #Red
    pygame.draw.rect(screen, RED, [175, 450, 25, 25])
    if haskey_red == False:
        lock(177, 448)
    #Draw keys


    keys = [bluekey]
    #blue key
    if haskey_blue == False:
        key(3, 945, 35)

    #green key
    if haskey_green == False:
        key(2, 455, 35)

    #red key
    if haskey_red == False:
        key(1, 945, 460)
    
    #goal walls

    redbox1 = [50, 575, 100, 10]
    redbox2 = [50, 575, 10, 100]
    redbox3 = [150, 575, 10, 100]
    redbox4 = [50, 675, 110, 10]
    if not redtouch:
        pygame.draw.rect(screen, RED, [50, 575, 100, 10])
        pygame.draw.rect(screen, RED, [50, 575, 10, 100])
        pygame.draw.rect(screen, RED, [150, 575, 10, 100])
        pygame.draw.rect(screen, RED, [50, 675, 110, 10])

    redgoal = [redbox1, redbox2, redbox3, redbox4]

    greenbox1 = [63, 588, 75, 10]
    greenbox2 = [63, 588, 10, 75]
    greenbox3 = [63, 663, 75, 10]
    greenbox4 = [138, 588, 10, 85]
    if not greentouch:
        pygame.draw.rect(screen, GREEN, greenbox1)
        pygame.draw.rect(screen, GREEN, greenbox2)
        pygame.draw.rect(screen, GREEN, greenbox3)
        pygame.draw.rect(screen, GREEN, greenbox4)

    greengoal = [greenbox1, greenbox2, greenbox3, greenbox4]

    bluebox1 = [75, 600, 50, 10]
    bluebox2 = [75, 600, 10, 50]
    bluebox3 = [75, 650, 50, 10]
    bluebox4 = [125, 600, 10, 60]
    if not bluetouch:
        pygame.draw.rect(screen, BLUE, bluebox1)
        pygame.draw.rect(screen, BLUE, bluebox2)
        pygame.draw.rect(screen, BLUE, bluebox3)
        pygame.draw.rect(screen, BLUE, bluebox4)

    bluegoal = [bluebox1, bluebox2, bluebox3, bluebox4]
    
    pygame.draw.rect(screen, WHITE, [95, 620, 20, 20])

    
    #COIN = (random.randint(30,255),random.randint(30,255),random.randint(30,255))
    
    
    '''for c in coins:
        if randomcolors:
            COIN = (random.randint(30,255),random.randint(30,255),random.randint(30,255))
        pygame.draw.rect(screen, COIN, c)

    hit_list = [c for c in coins if intersects.rect_rect(player, c)]

    for hit in hit_list:
        coins.remove(hit)
        score += 100
    if len(coins) == 0:
        win = True  '''
    
    #Timer
    font = pygame.font.Font(None, 64)
    timer_text = font.render(format_time(time_remaining), True, WHITE)
    screen.blit(timer_text, [900, 0])
    
    if win:
        font = pygame.font.Font(None, 64)
        WINCOLOR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        text = font.render("You Win!", 1, WINCOLOR)
        screen.blit(text, [(WIDTH/2)-96, (HEIGHT/2)-32])
        score = begintime - time_remaining
        

    
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

    
# Close window and quit
pygame.quit()
