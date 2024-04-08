import pygame
import sys

# Initialize game
pygame.init()
pygame.mixer.init()

# Display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Lightcycles")

# Load background image
background = pygame.image.load("MainMenu.jpg").convert()

# Load Music
pygame.mixer.music.load("MenuMusic.mp3")
pygame.mixer.music.play(-1)

# Colors
White = (255, 255, 255)
Black = (0, 0, 0)
TronBlue = (0, 204, 255)
Clear = (0, 0, 0, 0)

# Fonts
font = pygame.font.Font("TRON.TTF", 36)

# Function to display text on screen
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.center = (x, y)
    screen.blit(surface, rect)

# Main Menu
def main_menu():

    while True:
        # Draw background image
        screen.blit(background, (0, 0))

        draw_text("Tron Light Cycles", font, White, WIDTH // 2, HEIGHT // 4)

        # Buttons
        solo = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
        two_player = pygame.Rect(WIDTH // 2 - 100, 270, 200, 50)
        endless = pygame.Rect(WIDTH // 2 - 100, 340, 200, 50)
        leave = pygame.Rect(WIDTH // 2 - 100, 410, 200, 50)

        # Draw Buttons
        pygame.draw.rect(screen, Clear, solo)
        draw_text("Solo", font, White, WIDTH // 2, 225)
        pygame.draw.rect(screen, Clear, two_player)
        draw_text("Two Players", font, White, WIDTH // 2, 295)
        pygame.draw.rect(screen, Clear, endless)
        draw_text("Endless", font, White, WIDTH // 2, 365)
        pygame.draw.rect(screen, Clear, leave)
        draw_text("Leave Game", font, White, WIDTH // 2, 435)

        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # Check if mouse click is inside any button
                if solo.collidepoint(mouse_pos):
                    # Start Solo
                    print("Starting solo play...good luck")
                    pygame.mixer.music.stop()
                elif two_player.collidepoint(mouse_pos):
                    print("Starting two player mode...")
                    pygame.mixer.music.stop()
                elif endless.collidepoint(mouse_pos):
                    print("Starting Endless mode")
                    pygame.mixer.music.stop()
                elif leave.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

# Run the main menu
if __name__ == "__main__":
    main_menu()
