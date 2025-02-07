# main.py
import pygame
from constants import *
from player import Player


def main():
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Clock to limit FPS
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill("black")

        # Draw the player
        player.draw(screen)

        # Update the screen
        pygame.display.flip()

        # Limit FPS to 60
        clock.tick(60)

    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
