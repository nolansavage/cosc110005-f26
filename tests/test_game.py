import pygame
import random

# Start pygame
pygame.init()

# -----------------------------
# SETTINGS
# -----------------------------

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tiny Space Station")

clock = pygame.time.Clock()

# Colors
BLACK = (10, 10, 20)
WHITE = (255, 255, 255)
GREEN = (50, 200, 80)
BLUE = (50, 150, 255)
RED = (220, 60, 60)
YELLOW = (255, 220, 50)
GRAY = (100, 100, 100)


# -----------------------------
# PLAYER
# -----------------------------

player = pygame.Rect(375, 275, 30, 30)

player_speed = 5

health = 100
credits = 0


# -----------------------------
# ITEMS
# -----------------------------

# A piece of scrap metal
scrap = pygame.Rect(200, 150, 25, 25)

# Another piece of scrap
scrap2 = pygame.Rect(600, 400, 25, 25)

scrap_collected = 0


# -----------------------------
# ENEMY
# -----------------------------

enemy = pygame.Rect(500, 200, 30, 30)

enemy_speed = 2


# -----------------------------
# GAME LOOP
# -----------------------------

running = True

while running:

    # -------------------------
    # EVENTS
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # -------------------------
    # KEYBOARD
    # -------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= player_speed

    if keys[pygame.K_s]:
        player.y += player_speed

    if keys[pygame.K_a]:
        player.x -= player_speed

    if keys[pygame.K_d]:
        player.x += player_speed


    # -------------------------
    # KEEP PLAYER ON SCREEN
    # -------------------------

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    if player.top < 0:
        player.top = 0

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT


    # -------------------------
    # COLLECT SCRAP
    # -------------------------

    if player.colliderect(scrap):

        scrap.x = -100
        scrap.y = -100

        scrap_collected += 1
        credits += 25

        print("You found scrap!")
        print("Credits:", credits)


    if player.colliderect(scrap2):

        scrap2.x = -100
        scrap2.y = -100

        scrap_collected += 1
        credits += 25

        print("You found scrap!")
        print("Credits:", credits)


    # -------------------------
    # ENEMY MOVEMENT
    # -------------------------

    if enemy.x < player.x:
        enemy.x += enemy_speed

    if enemy.x > player.x:
        enemy.x -= enemy_speed

    if enemy.y < player.y:
        enemy.y += enemy_speed

    if enemy.y > player.y:
        enemy.y -= enemy_speed


    # -------------------------
    # ENEMY DAMAGE
    # -------------------------

    if player.colliderect(enemy):

        health -= 1


    # -------------------------
    # DRAW EVERYTHING
    # -------------------------

    screen.fill(BLACK)

    # Floor
    pygame.draw.rect(
        screen,
        GRAY,
        (50, 50, 700, 500)
    )

    # Player
    pygame.draw.rect(
        screen,
        BLUE,
        player
    )

    # Scrap
    pygame.draw.rect(
        screen,
        YELLOW,
        scrap
    )

    pygame.draw.rect(
        screen,
        YELLOW,
        scrap2
    )

    # Enemy
    pygame.draw.rect(
        screen,
        RED,
        enemy
    )


    # -------------------------
    # HUD
    # -------------------------

    font = pygame.font.Font(None, 32)

    health_text = font.render(
        f"Health: {health}",
        True,
        WHITE
    )

    credits_text = font.render(
        f"Credits: {credits}",
        True,
        WHITE
    )

    scrap_text = font.render(
        f"Scrap: {scrap_collected}",
        True,
        WHITE
    )

    screen.blit(
        health_text,
        (20, 15)
    )

    screen.blit(
        credits_text,
        (180, 15)
    )

    screen.blit(
        scrap_text,
        (350, 15)
    )


    # -------------------------
    # UPDATE SCREEN
    # -------------------------

    pygame.display.flip()

    clock.tick(60)


pygame.quit()