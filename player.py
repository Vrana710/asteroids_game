# player.py
import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape  # Make sure to import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class constructor, passing the PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initialize rotation to 0

    def triangle(self):
        # This method calculates the points of the triangle (spaceship)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the player (triangle) on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
