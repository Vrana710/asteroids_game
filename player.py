import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):  # Inherit from CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Call CircleShape constructor

        self.rotation = 0  # Initial rotation
        self.timer = 0  # Initialize the shoot cooldown timer
        self.velocity = pygame.Vector2(0, 0)

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

        # Update the timer: decrease by dt
        if self.timer > 0:
            self.timer -= dt

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

    def shoot(self):
        # Create a shot at the player's position only if the cooldown is over
        if self.timer <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = forward * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, velocity)

            # Reset the timer for the next shot
            self.timer = PLAYER_SHOOT_COOLDOWN
            return shot
        return None
