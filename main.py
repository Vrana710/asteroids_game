import pygame
from constants import *


def main():
    # Initialize pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Start the game loop
    running = True
    while running:
        # Handle events (e.g., closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop if the window is closed

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the screen
        pygame.display.flip()

    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
