import pygame
import random
import time
import math
from pygame import mixer
pygame.font.init()

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
mixer.init()

# Set up the display
WIDTH, HEIGHT = 800, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Basket")

# Set up game icon
icon = pygame.image.load("assets/tomato.png")
pygame.display.set_icon(icon)

# Basket properties
BASKET_WIDTH, BASKET_HEIGHT = 120, 120
BASKET_VEL = 9

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

# Sound effects
collect_sound = [
    mixer.Sound("sounds/collect_fruit_1.mp3"),
    mixer.Sound("sounds/collect_fruit_2.mp3"),
    mixer.Sound("sounds/collect_fruit_3.mp3"),
    ]

songs = [
    "sounds/background_music_1.mp3",
    "sounds/background_music_2.mp3",
    "sounds/background_music_3.mp3"
    ]
random.shuffle(songs)

def play_songs():
    global songs
    if songs:
        mixer.music.load(songs.pop(0))
        mixer.music.set_volume(0.2)
        mixer.music.play()
        mixer.music.set_endevent(pygame.USEREVENT)
    else: 
        songs = [
            "sounds/background_music_1.mp3",
            "sounds/background_music_2.mp3",
            "sounds/background_music_3.mp3"
            ]
        random.shuffle(songs)
        play_songs()

mixer.music.set_endevent(pygame.USEREVENT)
play_songs()

def draw(basket_img, basket_rect, elapsed_time, points, lives, fruits):
    # Draw the background image
    WIN.blit(BG, (0, 0))

    # Draw the timer
    time_text = FONT.render(f"Time: {round(elapsed_time, 1)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (10, 10))

    # Draw the points
    points_text = FONT.render(f"Points: {points}", 1, (255, 255, 255))
    WIN.blit(points_text, (WIDTH - points_text.get_width() - 10, 10))

    # Draw the lives
    lives_text = FONT.render(f"Lives: {lives}", 1, (255, 255, 255))
    WIN.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 40))

    # Draw the fruits
    for fruit in fruits:
        WIN.blit(fruit["image"], (fruit["rect"].x, fruit["rect"].y))

    # Draw the basket
    WIN.blit(basket_img, (basket_rect.x, basket_rect.y))

    # Update the display
    pygame.display.update()

# Start screen
def start_screen(window):
    font = pygame.font.Font("fonts/PressStart2P.ttf", 18)
    time_passed = 0

    mixer.music.load("sounds/waiting.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)  # Loop the waiting music

    running = True
    while running:
        time_passed += 0.025
        wave_offset = math.sin(time_passed) * 5  # Create a wave effect

        WIN.blit(BG, (0, 0))
        start_text = font.render("Fruit Basket - Press SPACE to Start", 1, (255, 255, 255))
        window.blit(start_text, (WIDTH/2 - start_text.get_width()/2, HEIGHT/2 - start_text.get_height()/2 + 200 + wave_offset))  # Position text on screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False  # Exit start screen loop

    mixer.music.stop()  # Stop the waiting music

def game_over_screen():
    font = pygame.font.Font("fonts/PressStart2P.ttf", 20)
    time_passed = 0

    running = True
    while running:
        time_passed += 0.025
        wave_offset = math.sin(time_passed) * 5  # Create a wave effect

        WIN.blit(BG, (0, 0))
        game_over_text = font.render("Game Over! Press SPACE to Restart", 1, (255, 255, 255))
        WIN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2 + wave_offset))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False  # Player presses SPACE to restart

    main()  # Restart game without stopping music

# Game loop
def main():
    start_screen(WIN)  # Call before main game loop
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

    # Lives
    lives = 10

    # Basket speed
    basket_vel = BASKET_VEL

    # Fruit speed
    fruit_vel = FRUIT_VEL

    # Fruit spawning
    fruit_add_increment = 1500
    fruit_count = 0
    
    fruits = []

    while run:
        fruit_count += clock.tick(60)  # Set the frame rate to 60 FPS
        elapsed_time = time.time() - start_time

        # Update the basket speed every 15 seconds
        basket_vel = min(12, BASKET_VEL + int(elapsed_time // 15))

        # Update the fruit speed every 30 seconds
        fruit_vel = min(10, FRUIT_VEL + int(elapsed_time // 30))

        # Spawn fruits
        if fruit_count >= fruit_add_increment:
            fruit_x = random.randint(0, WIDTH - FRUIT_WIDTH)
            fruit_type = random.choice(fruit_images)
            fruit = {
                "rect": pygame.Rect(fruit_x, -FRUIT_HEIGHT, FRUIT_WIDTH, FRUIT_HEIGHT),
                "image": fruit_type
                }
            fruits.append(fruit)

            fruit_add_increment = max(600, fruit_add_increment - 50)
            fruit_count = 0

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                play_songs()
            elif event.type == pygame.QUIT:
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
            fruit["rect"].y += fruit_vel  # Move downward

            if fruit["rect"].y > HEIGHT:
                fruits.remove(fruit)  # Remove fruit if it goes off screen
                lives -= 1
            elif fruit["rect"].colliderect(basket_rect):
                random.choice(collect_sound).set_volume(random.uniform(0.2, 0.5))
                random.choice(collect_sound).play()
                points += 1
                fruits.remove(fruit)

        if lives <= 0:
            game_over_screen()
            break


        draw(loading_basket_img, basket_rect, elapsed_time, points, lives, fruits)

    pygame.quit()


if __name__ == "__main__":
    main()