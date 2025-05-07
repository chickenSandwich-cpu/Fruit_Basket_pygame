import pygame
import random
import time

# Initialize Pygame
WIDTH, HEIGHT = 800, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Basket")

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

PLAYER_VEL = 1

BG = pygame.image.load("assets/pixelated_background.png")

if BG:
    print("Background loaded successfully") # Debug message

def draw(player):
    # Draw the background image
    WIN.blit(BG, (0, 0))

    # Draw the player
    pygame.draw.rect(WIN, (215, 139, 98), player)

    # Update the display
    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT*2, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()