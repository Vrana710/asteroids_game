import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from pygame.sprite import Group


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()

    updatable = Group()
    drawable = Group()
    asteroids = Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    updatable.add(player)  # Add player to updatable
    drawable.add(player)  # Add player to drawable

    while True:
        dt = clock.tick(60) / 1000  # Seconds per frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        asteroid_field.update(dt)  # Now actually using asteroid_field
        updatable.update(dt)

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
