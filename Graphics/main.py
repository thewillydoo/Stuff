# Import a library of functions called 'pygame'
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the game engine
pygame.init()

#Opening and setting the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

#Setting the window title
pygame.display.set_caption("Will's Canvas")

# Clear the screen and set the screen background
screen.fill(WHITE)

#Flipping the Pygame display
# Go ahead and update the screen with what we've drawn.(Do this after you draw something)
pygame.display.flip()


#Proper shutdown of a Pygame program
pygame.quit()









