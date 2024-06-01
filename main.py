import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, WHITE, BLUE, FPS
from ball import Ball

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Falling Ball with OOP and User Control")

    clock = pygame.time.Clock()
    ball = Ball(SCREEN_WIDTH // 2, BALL_RADIUS, BALL_RADIUS, BLUE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        ball.update()
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
