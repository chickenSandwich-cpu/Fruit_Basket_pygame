import pygame
import random
import time
pygame.font.init()

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Basket")

# Set up game icon
icon = pygame.image.load("assets/tomato.png")
pygame.display.set_icon(icon)

# Basket properties
BASKET_WIDTH = 120
BASKET_HEIGHT = 120

BASKET_VEL = 5

FONT = pygame.font.Font("fonts/PressStart2P.ttf", 20)

# Load images
BG = pygame.image.load("assets/background.png")
basket_img = pygame.image.load("assets/basket.png")
basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))
basket_flipped = pygame.transform.flip(basket_img, True, False)


# if BG:
    # print("Background loaded successfully") # Debug message


def draw(basket_img, basket_rect, elapsed_time, points):
    # Draw the background image
    WIN.blit(BG, (0, 0))

    # Draw the timer
    time_text = FONT.render(f"Time: {round(elapsed_time, 1)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Draw the points
    points_text = FONT.render(f"Points: {points}", 1, "white")
    WIN.blit(points_text, (WIDTH - points_text.get_width() - 10, 10))

    # Draw the basket
    WIN.blit(basket_img, (basket_rect.x, basket_rect.y))

    # Update the display
    pygame.display.update()


# Game loop
def main():
    run = True
    flipped = False

    basket_rect = pygame.Rect(200, HEIGHT - 180, BASKET_WIDTH, BASKET_HEIGHT)
    loading_basket_img = basket_img

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    points = 0


    while run:
        clock.tick(60)  # Set the frame rate to 60 FPS
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_rect.x - BASKET_VEL >= 0:
            basket_rect.x -= BASKET_VEL
            if flipped:
                loading_basket_img = basket_img
                flipped = False

        if keys[pygame.K_RIGHT] and basket_rect.x + BASKET_VEL + basket_rect.width <= WIDTH:
            basket_rect.x += BASKET_VEL
            # points += 1
            if not flipped:
                loading_basket_img = basket_flipped
                flipped = True

        draw(loading_basket_img, basket_rect, elapsed_time, points)

    pygame.quit()


if __name__ == "__main__":
    main()