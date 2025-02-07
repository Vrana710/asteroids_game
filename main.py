import pygame
from constants import *


def main():
    # Initialize pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop if the window is closed

        # Fill the screen with black (this will refresh the screen)
        screen.fill((0, 0, 0))

        # Update the screen
        pygame.display.flip()

        # Limit the frame rate to 60 FPS and get delta time
        dt = clock.tick(60) / 1000  # Delta time in seconds

    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
