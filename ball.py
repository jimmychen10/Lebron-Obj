import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, BALL_RADIUS, GRAVITY

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.y_velocity = 0
        self.x_velocity = 0
        self.speed = 5

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_velocity = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.x_velocity = self.speed
        else:
            self.x_velocity = 0

    def update(self):
        self.handle_keys()
        self.y_velocity += GRAVITY
        self.y += self.y_velocity
        self.x += self.x_velocity

        # Prevent the ball from going out of bounds
        if self.x - self.radius < 0:
            self.x = self.radius
        if self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius

        # If the ball hits the bottom of the screen, stop it
        if self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.y_velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
