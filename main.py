import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from pygame.sprite import Group
from shot import Shot


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()

    updatable = Group()
    drawable = Group()
    asteroids = Group()
    shots = Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    updatable.add(player)
    drawable.add(player)

    while True:
        dt = clock.tick(60) / 1000  # Seconds per frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Shooting
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            if shot:  # Only add the shot if it's not None (i.e., cooldown is over)
                shots.add(shot)

        # Collision detection between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return

        # Bullet and asteroid collision detection
        for shot in shots:
            for asteroid in asteroids:
                if shot.rect.colliderect(asteroid.rect):  # Check if shot and asteroid collide
                    shot.kill()  # Remove the shot from the game
                    asteroid.split()  # Split the asteroid if it’s large enough

        asteroid_field.update(dt)
        updatable.update(dt)

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
