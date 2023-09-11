"""
print('What is your name?')   # ask for their name
my_name = input()
print('Hi, {}'.format(my_name))
        # What is your name?
        # Martha
        # Hi, Martha
#input() can also set a default message without using print():

my_name = input('What is your name? ')  # default message
print('Hi, {}'.format(my_name))
        # What is your name? Martha
        # Hi, Martha
#It is also possible to use formatted strings to avoid using .format:

my_name = input('What is your name? ')  # default message
print(f'Hi, {my_name}')
        # What is your name? Martha
        # Hi, Martha
"""
'''
a = [1, 2, 3]

# bad
if len(a) > 0:  # evaluates to True
    print("the list is not empty!")
        
# the list is not empty!

# good
if a: # evaluates to True
    print("the list is not empty!")
        
# the list is not empty!
'''

# Import a library of functions called 'pygame'
import math
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#Opening and setting the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

#Setting the window title
pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print("User asked to quit.")
            done = True # Flag that we are done so we exit this loop
            
        elif event.type == pygame.KEYDOWN:
                print("User pressed a key.")
        elif event.type == pygame.KEYUP:
                print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
                print("User pressed a mouse button")
    print("escaped")
    # --- Game logic should go here
       
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

