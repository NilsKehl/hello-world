import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße und Farben
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 255, 255)

# Spieler
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 2

# Hindernisse
obstacle_width = 30
obstacle_height = random.randint(50, 200)
obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
obstacle_y = 0
obstacle_speed = 2

# Punktzahl
score = 0

# Einrichten des Bildschirms
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner")

# Hauptspielschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spielersteuerung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Bewegung des Hindernisses
    obstacle_y += obstacle_speed
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = 0
        obstacle_width = 30
        obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
        obstacle_height = random.randint(50, 200)
        score += 1

    # Kollisionserkennung
    if (
        player_x + player_width > obstacle_x
        and player_x < obstacle_x + obstacle_width
        and player_y < obstacle_y + obstacle_height
    ):
        print("Spiel vorbei! Punktzahl:", score)
        running = False

    # Hintergrund zeichnen
    screen.fill(BACKGROUND_COLOR)

    # Spieler zeichnen
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_width, player_height))

    # Hindernis zeichnen
    pygame.draw.rect(screen, PLAYER_COLOR, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Punktzahl anzeigen
    font = pygame.font.Font(None, 36)
    text = font.render("Punktzahl: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

# Pygame beenden
pygame.quit()
