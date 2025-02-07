import pygame
from constants import *


class Player(pygame.sprite.Sprite):  # Ensure it correctly inherits Sprite
    def __init__(self, x, y):
        super().__init__()  # Properly initialize Sprite class

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0  # Initial rotation
        self.radius = PLAYER_RADIUS

        # Create a rect for sprite group compatibility
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def triangle(self):
        # Calculate the vertices of the spaceship (triangle)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-1, dt)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(1, dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            self.move(dt, reverse=True)

        # Update the rect position
        self.rect.center = self.position

    def rotate(self, direction, dt):
        self.rotation += PLAYER_TURN_SPEED * direction * dt

    def move(self, dt, reverse=False):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if reverse:
            forward = -forward
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, screen):
        # Draw the spaceship as a triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
