"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pressed_1 = False
mouse_button = False
w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False
objects_list = []
y = 100
x = 100
player = [x,y,20,20]


def actionDetection():
    global pressed_1, mouse_button,w_pressed,a_pressed,s_pressed,d_pressed,player,y,x
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print("User asked to quit.")
            pygame.quit()
            return True
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "1":
                pressed_1 = True
            if pygame.key.name(event.key) == "w":
                w_pressed = True
            if pygame.key.name(event.key) == "a":
                a_pressed = True
            if pygame.key.name(event.key) == "s":
                s_pressed = True
            if pygame.key.name(event.key) == "d":
                d_pressed = True
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            if pygame.key.name(event.key) == "1":
                pressed_1 = False
            if pygame.key.name(event.key) == "w":
                w_pressed = False
            if pygame.key.name(event.key) == "a":
                a_pressed = False
            if pygame.key.name(event.key) == "s":
                s_pressed = False
            if pygame.key.name(event.key) == "d":
                d_pressed = False
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button = True
            #drawground(True)
            print("User pressed a mouse button")
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button = False
            #drawground(True)
            print("User let go of mouse button")
    return False


def draw_player(x,y):
    objects_list.append([screen, RED, x, y, 20, 20,True])

def drawground(T_F):
        [x,y] = mouseLocation_finder()
        pygame.draw.rect(screen, GREEN, [x, y, 100, 10], 0)
        pygame.draw.rect(screen, BLACK, [x, y+10, 100, 20], 0)
        if T_F == True:
            objects_list.append([screen, GREEN, x, y, 100, 10,True])
            objects_list.append([screen, BLACK, x, y+10, 100, 20,True])
        elif T_F == False:
            objects_list.append([screen, GREEN, x, y, 100, 10,False])
            objects_list.append([screen, BLACK, x, y+10, 100, 20,False])
def mouseLocation_finder():
    mouse_pos = pygame.mouse.get_pos() 
    return mouse_pos




pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:

    player = [x,y,20,20]
    # --- Main event loop
    done == actionDetection()  # Flag that we are done so we exit this loop   
    # --- Game logic should go here
    if pressed_1 == True and mouse_button == True:
        drawground(True)
    elif pressed_1 == True and mouse_button == False:
        drawground(False)
    if w_pressed == True and d_pressed == False:
        y = y - 10
        draw_player(x,y)
        print(x,y)


    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    


    #pygame.draw.rect(Surface, color, Rect, width=0): return Rect
    #pygame.draw.rect(screen, RED, [55, 50, 20, 25], 0)
    # Draw on the screen a green line from (0, 0) to (100, 100)
    # that is 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)



 
    for item in objects_list:
        pygame.draw.rect(item[0], item[1], [item[2], item[3], item[4], item[5]], 0) 
        if item[6] == False:
            objects_list.remove(item)
    
    
    
    for i in range(200):
    
        radians_x = i / 20
        radians_y = i / 6
    
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200
    
        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)  
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text",True,BLACK)
    
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()