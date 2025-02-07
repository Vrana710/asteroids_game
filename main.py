import pygame
from constants import *
from player import Player
from pygame.sprite import Group


def main():
    pygame.init()

    # Set up the game screen and window caption
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Clock for controlling FPS
    clock = pygame.time.Clock()

    # Groups for updatable and drawable objects
    updatable = Group()
    drawable = Group()

    # Create a Player object and add it to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Game loop
    while True:
        dt = clock.tick(60) / 1000  # Amount of seconds between frames (delta time)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update all updatable objects
        updatable.update(dt)

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Manually draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
