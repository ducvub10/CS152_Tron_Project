import pygame
import sys
from Player import Player

# Initialize Pygame
pygame.init()

#Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Set the size of the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Tron bike positions
bike1_position = [100, 50]
bike2_position = [700, 550]


player1 = Player(100, 50, 'right', BLUE)
player2 = Player(700, 550, 'left', RED)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Player 1
            if event.key == pygame.K_UP:
                player1.direction = 'up'
            elif event.key == pygame.K_DOWN:
                player1.direction = 'down'
            elif event.key == pygame.K_LEFT:
                player1.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                player1.direction = 'right'
            # Player 2
            elif event.key == pygame.K_w:
                player2.direction = 'up'
            elif event.key == pygame.K_s:
                player2.direction = 'down'
            elif event.key == pygame.K_a:
                player2.direction = 'left'
            elif event.key == pygame.K_d:
                player2.direction = 'right'


    # Fill the screen with black
    screen.fill(BLACK)

    # Move the players
    player1.move()
    player2.move()

    # Draw the players
    player1.draw(screen)
    player2.draw(screen)

    # If a player hits the screen boundary, end the game
    if player1.x <= 0 or player1.x >= screen_width or player1.y <= 0 or player1.y >= screen_height or \
       player2.x <= 0 or player2.x >= screen_width or player2.y <= 0 or player2.y >= screen_height:
        pygame.quit()
    
    # Check for collisions
    if (player1.x, player1.y) in player2.trail or (player2.x, player2.y) in player1.trail:
        pygame.quit()
        sys.exit()    

    # Update the screen
    pygame.display.flip()

    clock.tick(10)
    