import pygame

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
BALL_WIDTH = 20
BALL_HEIGHT = 20

def initBlockLists():
    blockList = getListOf10Blocks(xLoc, 150)
    blockList2 = getListOf10Blocks(xLoc, 300)
    blockList3 = getListOf10Blocks(xLoc, 450)
    blockList4 = getListOf10Blocks(xLoc, 600)

    return blockList, blockList2, blockList3, blockList4

def getListOf10Blocks(xLoc, yLoc):
    BLOCK_WIDTH = 75
    BLOCK_HEIGHT = 40
    BLOCK_SPACING = 125

    blockList = []

    for num in range(1000):
        blockList.append(pygame.Rect(xLoc, yLoc, BLOCK_WIDTH, BLOCK_HEIGHT))

        xLoc = xLoc + BLOCK_WIDTH + BLOCK_SPACING

    return blockList


# --- Your Variables Here
xBall = (SCREEN_WIDTH // 2) - (BALL_WIDTH // 2)
yBall = SCREEN_HEIGHT - BALL_HEIGHT
ball = pygame.Rect(xBall, yBall, BALL_WIDTH, BALL_HEIGHT)
gameSpeed = 60
xLoc = 62.5
firstRun = True
base = pygame.Rect(400, 0, 200, 100)
lives = 3
animate = True

# --- Setup Tasks
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Frogger")
done = False
clock = pygame.time.Clock()

# --- Main Game Loop
while not done:

    font = pygame.font.SysFont("comic sans", 60)
    font1 = pygame.font.SysFont("comic sans", 40)
    lifeTracker = font1.render("Lives: " + str(lives), 1, BLACK)
    loss = font.render("GAME OVER", 1, BLACK)
    won = font.render("GAME WON", 1, BLACK)
    
    # --- Event Processing
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xBall = xBall + 30
                if xBall > 1000:
                    xBall = (SCREEN_WIDTH // 2) - (BALL_WIDTH // 2)
            if event.key == pygame.K_LEFT:
                xBall = xBall - 30
                if xBall < 0:
                    xBall = (SCREEN_WIDTH // 2) - (BALL_WIDTH // 2)
            if event.key == pygame.K_UP:
                yBall = yBall - 30
            if event.key == pygame.K_DOWN:
                yBall = yBall + 30

    # --- Your Drawing & Updating Here
    if animate:

        # --- Clear the screen
        screen.fill(WHITE)

        screen.blit(lifeTracker, (800, 50))

        if firstRun == True:
            blockList, blockList2, blockList3, blockList4 = initBlockLists()
            firstRun = False
        else:
            for n in range(len(blockList)):
                blockList[n] = blockList[n].move(-5, 0)
                pygame.draw.rect(screen, GREEN, blockList[n])
            for n in range(len(blockList2)):
                blockList2[n] = blockList2[n].move(-2, 0)
                pygame.draw.rect(screen, GREEN, blockList2[n])
            for n in range(len(blockList3)):
                blockList3[n] = blockList3[n].move(-3, 0)
                pygame.draw.rect(screen, GREEN, blockList3[n])
            for n in range(len(blockList4)):
                blockList4[n] = blockList4[n].move(-4, 0)
                pygame.draw.rect(screen, GREEN, blockList4[n])
                
        ball = pygame.Rect(xBall, yBall, BALL_WIDTH, BALL_HEIGHT)
        pygame.draw.rect(screen, BLACK, ball)
        pygame.draw.rect(screen, RED, base)

        index = ball.collidelist(blockList)
        index2 = ball.collidelist(blockList2)
        index3 = ball.collidelist(blockList3)
        index4 = ball.collidelist(blockList4)

    if index != -1 or index2 != -1 or index3 != -1 or index4 != -1:
        xBall = (SCREEN_WIDTH // 2) - (BALL_WIDTH // 2)
        yBall = SCREEN_HEIGHT - BALL_HEIGHT
        lives = lives - 1
        if lives == 0:
            animate = False
            screen.blit(loss, (400,300))
                        
    if xBall > 400 and xBall < 600 and yBall > 0 and yBall < 100:
        animate = False
        screen.blit(won, (400, 300))

    # --- Other Tasks After Drawing
    pygame.display.flip() # show what we've drawn
    clock.tick(gameSpeed) # 60 frames per second
 

pygame.quit() # Close the window and quit.
