# main.py
import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Initialize player at the center

    while True:
        dt = clock.tick(60) / 1000  # Get the delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the window is closed

        player.update(dt)  # Call the player's update method

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
