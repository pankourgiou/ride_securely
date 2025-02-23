import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exploration")

# Colors
BLACK = (10, 10, 10)
NEON_BLUE = (0, 255, 255)
NEON_RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Load font
font = pygame.font.Font(None, 30)

# Load background image
background = pygame.image.load("Micra.png")  # Make sure you have an image file
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load character image
character = pygame.image.load("character.png")  # Ensure you have a character sprite
character = pygame.transform.scale(character, (50, 50))

# Character position
char_x, char_y = WIDTH // 2, HEIGHT // 2
current_location = None  # Track current location

# City locations and events (with coordinates)
locations = [
    {"name": "A", "event": "We will paint it to a serious grey...", "x": 180,"y":200},
    {"name": "B", "event": "we apply κ.ο.κ. trffic code perfectly", "x": 200, "y":300},
    {"name": "C", "event": "we change the engine to a unique Mercedes engine!!", "x": 110,"y":300},
    {"name": "D", "event": "Hello! the weather is good..2 degrees celcius but it's ok", "x": 200, "y": 400},
    {"name": "E", "event": "we will ride with style!", "x": 200,"y":450},
]


def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def game_loop():
    global char_x, char_y, current_location  # Ensure variables are modified inside the function
    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(character, (char_x, char_y))
        draw_text("exploration", 50, 50, NEON_BLUE)
        
        # Display locations as interactive points
        for location in locations:
            pygame.draw.circle(screen, NEON_BLUE, (location['x'], location['y']), 10)
            draw_text(location['name'], location['x'] + 15, location['y'] - 10, NEON_BLUE)
        
        # Check if near a location and display event message continuously
        current_location = None
        for location in locations:
            if abs(char_x - location['x']) < 20 and abs(char_y - location['y']) < 20:
                current_location = location
                break  # Stop once you find a location
        
        if current_location:
            draw_text(f"You are at {current_location['name']}: {current_location['event']}", 50, HEIGHT - 50, NEON_BLUE)
        else:
            draw_text("Move closer to a spot...", 50, HEIGHT - 50, NEON_BLUE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    char_x -= 10
                elif event.key == pygame.K_RIGHT:
                    char_x += 10
                elif event.key == pygame.K_UP:
                    char_y -= 10
                elif event.key == pygame.K_DOWN:
                    char_y += 10

    pygame.quit()

if __name__ == "__main__":
    game_loop()
