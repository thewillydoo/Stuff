"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BRICK = (118,64,64)
SKY = (138, 221, 225)
YELLOW = (244, 226, 52)
ROOF = (56, 42, 11)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Will's Canvas")

pi = 3.141592653
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    #Background
    pygame.draw.rect(screen, SKY, [0, 0, 700, 500])
    pygame.draw.rect(screen, GREEN, [0, 400, 700, 500])
    #House
    pygame.draw.rect(screen, BRICK, [50, 300, 400, 200])
    pygame.draw.polygon(screen, ROOF, [[50, 300], [450, 300],[250, 150]])
    #Door
    pygame.draw.rect(screen, BLACK, [175, 375, 75, 125])
    pygame.draw.circle(screen, WHITE, (240, 450), 3)
    #Window
    pygame.draw.rect(screen, BLACK, [350, 375, 50, 50], 2)
    pygame.draw.line(screen, WHITE, (350, 400), (400, 400), 2)
    pygame.draw.line(screen, WHITE, (375, 375), (375, 425), 2)
    

    #Sun
    pygame.draw.circle(screen, YELLOW, (100, 50), 40)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()