import pygame 

def draw_snowman(screen, x, y):
    # Draw a circle for the head
    pygame.draw.ellipse(screen, white, [35 + x, y, 25, 25])
    # Draw the middle snowman circle
    pygame.draw.ellipse(screen, white, [23 + x, 20 + y, 50, 50])
    # Draw the bottom snowman circle
    pygame.draw.ellipse(screen, white, [x, 65 + y, 100, 100])

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]


size = [400, 500]
screen = pygame.display.set_mode(size)

done = False 
clock = pygame.time.Clock()


while done == False:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    screen.fill(black)

    draw_snowman(screen, 10, 10)
    draw_snowman(screen, 300, 10)
    draw_snowman(screen, 10, 300)

    pygame.display.flip()

pygame.quit()

