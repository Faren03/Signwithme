import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Character Customization")

# Function to draw the character
def draw_character(hair_color, shirt_color):
    # Clear the screen
    screen.fill(WHITE)

    # Draw head
    pygame.draw.circle(screen, BLACK, (200, 150), 30)

    # Draw hair
    if hair_color == "Brown":
        pygame.draw.rect(screen, (139, 69, 19), (175, 120, 50, 30))
    elif hair_color == "Blond":
        pygame.draw.rect(screen, (255, 222, 173), (175, 120, 50, 30))
    elif hair_color == "Black":
        pygame.draw.rect(screen, BLACK, (175, 120, 50, 30))

    # Draw body
    pygame.draw.rect(screen, shirt_color, (185, 180, 30, 50))

    # Update the display
    pygame.display.flip()

# Function to get user input
def get_user_input():
    hair_color = input("Enter hair color (Brown/Blond/Black): ").capitalize()
    shirt_color = input("Enter shirt color (Red/Blue/Green): ").capitalize()

    # Validate input
    valid_colors = ["Brown", "Blond", "Black", "Red", "Blue", "Green"]
    if hair_color not in valid_colors or shirt_color not in valid_colors:
        print("Invalid color selection. Using default colors.")
        hair_color, shirt_color = "Brown", "Red"

    return hair_color, shirt_color

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get user input
    user_hair_color, user_shirt_color = get_user_input()

    # Draw the character with user-specified colors
    draw_character(user_hair_color, user_shirt_color)

    # Wait for a short duration to control the frame rate
    pygame.time.delay(100)
