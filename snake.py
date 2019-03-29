import pygame
import time
import random

pygame.init()

green = (178, 255, 102)
black = (153, 0, 153)
blue = (0, 102, 102)
gray = (64, 64, 64)

window_width = 640
window_height = 480

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Python Project - Snake Game')

clock = pygame.time.Clock()
blockSize = 10
noPixel = 0

font = pygame.font.SysFont(None, 25, bold = True)

def snake(blockSize, snakelist):
    for size in snakelist:
        pygame.draw.rect(gameDisplay, black,[size[0],size[1],blockSize,blockSize])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [50, window_height/2])
    
def gameLoop():
    FPS = 15
    score = 0
    gameExit = False
    gameOver = False

    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0
    randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0
    
    while not gameExit:
                    

        while gameOver == True:
            gameDisplay.fill(green)
            string = "Game Over | Your Score is " + str(score) + " | Press C to restart | Press Q to QUIT";
            message_to_screen(string, gray)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:

                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN
                
                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

          
                   
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y
        
        gameDisplay.fill(green)

        AppleThickness = 10
        pygame.draw.rect(gameDisplay, blue, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakeLength:
            del snakelist[0]
            
        for eachSegment in snakelist [:-1]:
            if eachSegment == snakehead:
                gameOver = True
                
        snake(blockSize, snakelist)
        
        pygame.display.update()
        
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1
                score = score + 1
                FPS = FPS + 3

             
        clock.tick(FPS)

    pygame.quit()
    quit()
gameLoop()                                 