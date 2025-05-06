import pygame
import random
import time

# Initialize Pygame
WIDTH, HEIGHT = 800, 640
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Basket")

BG = pygame.image.load("assets/fruitBasketBackground.png")
if BG:
    print("Background loaded successfully")

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

def draw(player):
    # Draw the background image
    win.blit(BG, (0, 0))

    # Draw the player
    pygame.draw.rect(win, (215, 139, 98), player)

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
        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()