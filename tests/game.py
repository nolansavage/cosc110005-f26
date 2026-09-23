import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Creature Adventure")

# Colors
GREEN = (50, 180, 50)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_x = 400
player_y = 300
player_size = 32
player_speed = 5

# Font
font = pygame.font.SysFont(None, 40)

# Grass area
grass = pygame.Rect(250, 150, 300, 300)

# Encounter variables
message = ""
message_timer = 0

running = True

clock = pygame.time.Clock()

while running:

    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Player rectangle
    player_rect = pygame.Rect(
        player_x,
        player_y,
        player_size,
        player_size
    )

    # Random encounter
    if player_rect.colliderect(grass):

        chance = random.randint(1, 300)

        if chance == 1:
            creatures = [
                "Leafling",
                "Voltusk",
                "Aquaryx",
                "Pyrodon"
            ]

            wild_creature = random.choice(creatures)

            message = f"Wild {wild_creature} appeared!"
            message_timer = 180

    # Drawing
    screen.fill(GREEN)

    # Grass
    pygame.draw.rect(screen, DARK_GREEN, grass)

    # Player
    pygame.draw.rect(
        screen,
        RED,
        (player_x, player_y, player_size, player_size)
    )

    # Encounter message
    if message_timer > 0:

        text = font.render(message, True, WHITE)

        pygame.draw.rect(
            screen,
            BLACK,
            (50, 500, 700, 60)
        )

        screen.blit(text, (60, 515))

        message_timer -= 1

    pygame.display.update()

pygame.quit()