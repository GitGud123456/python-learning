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
import pygame
# Initialize the game engine
pygame.init()