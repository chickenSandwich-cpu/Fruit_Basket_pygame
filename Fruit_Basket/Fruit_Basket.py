import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Basket")

# Set up game icon
icon = pygame.image.load("assets/tomato.png")
pygame.display.set_icon(icon)

BASKET_WIDTH = 80
BASKET_HEIGHT = 80

BASKET_VEL = 5

BG = pygame.image.load("assets/background.png")
basket_img = pygame.image.load("assets/basket.png")
basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))


# if BG:
    # print("Background loaded successfully") # Debug message


def draw(basket_img, basket_rect):
    # Draw the background image
    WIN.blit(BG, (0, 0))

    # Draw the basket
    # pygame.draw.rect(WIN, (215, 139, 98), basket)
    WIN.blit(basket_img, (basket_rect.x, basket_rect.y))

    # Update the display
    pygame.display.update()


# Game loop
def main():
    run = True

    basket_rect = pygame.Rect(200, HEIGHT - BASKET_HEIGHT*2, BASKET_WIDTH, BASKET_HEIGHT)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # Set the frame rate to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_rect.x - BASKET_VEL >= 0:
            basket_rect.x -= BASKET_VEL
        if keys[pygame.K_RIGHT] and basket_rect.x + BASKET_VEL + basket_rect.width <= WIDTH:
            basket_rect.x += BASKET_VEL

        draw(basket_img, basket_rect)

    pygame.quit()


if __name__ == "__main__":
    main()