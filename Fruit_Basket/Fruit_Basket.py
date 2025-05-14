import pygame
import random
import time
from pygame import mixer
pygame.font.init()

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
mixer.init()
mixer.music.load("sounds/collect_fruit.mp3")

# Set up the display
WIDTH, HEIGHT = 800, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Basket")

# Set up game icon
icon = pygame.image.load("assets/tomato.png")
pygame.display.set_icon(icon)

# Basket properties
BASKET_WIDTH, BASKET_HEIGHT = 120, 120
BASKET_VEL = 8

# Fruit properties
FRUIT_WIDTH, FRUIT_HEIGHT = 32, 32
FRUIT_VEL = 5

# Set up font
FONT = pygame.font.Font("fonts/PressStart2P.ttf", 20)

# Load images
BG = pygame.image.load("assets/background.png")
basket_img = pygame.image.load("assets/basket.png")
basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))
basket_flipped = pygame.transform.flip(basket_img, True, False)

# Load fruit images
fruit_images = [
    pygame.image.load("assets/tomato.png"),
    pygame.image.load("assets/carrot.png"),
    pygame.image.load("assets/green_apple.png")
    ]


# if BG:
    # print("Background loaded successfully") # Debug message


def draw(basket_img, basket_rect, elapsed_time, points, fruits):
    # Draw the background image
    WIN.blit(BG, (0, 0))

    # Draw the timer
    time_text = FONT.render(f"Time: {round(elapsed_time, 1)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Draw the points
    points_text = FONT.render(f"Points: {points}", 1, "white")
    WIN.blit(points_text, (WIDTH - points_text.get_width() - 10, 10))

    # Draw the fruits
    for fruit in fruits:
        WIN.blit(fruit["image"], (fruit["rect"].x, fruit["rect"].y))

    # Draw the basket
    WIN.blit(basket_img, (basket_rect.x, basket_rect.y))

    # Update the display
    pygame.display.update()


# Game loop
def main():
    run = True
    flipped = False

    # Load the basket image
    basket_rect = pygame.Rect(200, HEIGHT - 180, BASKET_WIDTH, BASKET_HEIGHT)
    loading_basket_img = basket_img

    # Timer
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    # Points
    points = 0

    # Basket speed
    basket_vel = BASKET_VEL

    # Fruit spawning
    fruit_add_increment = 1000
    fruit_count = 0
    
    fruits = []

    while run:
        fruit_count += clock.tick(60)  # Set the frame rate to 60 FPS
        elapsed_time = time.time() - start_time

        # Update the basket speed every 10 seconds
        basket_vel = min(12, BASKET_VEL + int(elapsed_time // 10))  

        # Spawn fruits
        if fruit_count >= fruit_add_increment:
            fruit_x = random.randint(0, WIDTH - FRUIT_WIDTH)
            fruit_type = random.choice(fruit_images)
            fruit = {
                "rect": pygame.Rect(fruit_x, -FRUIT_HEIGHT, FRUIT_WIDTH, FRUIT_HEIGHT),
                "image": fruit_type
                }
            fruits.append(fruit)

            fruit_add_increment = max(600, fruit_add_increment - 75)
            fruit_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_rect.x - BASKET_VEL >= 0:
            basket_rect.x -= basket_vel
            if flipped:
                loading_basket_img = basket_img
                flipped = False

        if keys[pygame.K_RIGHT] and basket_rect.x + BASKET_VEL + basket_rect.width <= WIDTH:
            basket_rect.x += basket_vel
            if not flipped:
                loading_basket_img = basket_flipped
                flipped = True

        for fruit in fruits[:]:
            fruit["rect"].y += FRUIT_VEL  # Move downward

            if fruit["rect"].y > HEIGHT:
                fruits.remove(fruit)  # Remove fruit if it goes off screen
            elif fruit["rect"].colliderect(basket_rect):
                points += 1
                fruits.remove(fruit)


        draw(loading_basket_img, basket_rect, elapsed_time, points, fruits)

    pygame.quit()


if __name__ == "__main__":
    main()