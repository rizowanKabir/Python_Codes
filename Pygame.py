import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Car Racing")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
DARK = (30,30,30)
YELLOW = (255,200,0)
RED = (220,50,50)
BLUE = (50,150,255)

# Road settings
road_line_y = 0
road_speed = 6

# Player
player_w, player_h = 50, 100
player_x = WIDTH//2 - player_w//2
player_y = HEIGHT - player_h - 20
player_speed = 7

# Enemy settings
enemy_w, enemy_h = 50, 100
enemies = []
enemy_speed = 6

font = pygame.font.SysFont("arial", 30)
big_font = pygame.font.SysFont("arial", 60)

score = 0
game_over = False


def spawn_enemy():
    x = random.randint(60, WIDTH - 60 - enemy_w)
    y = random.randint(-600, -100)
    enemies.append(pygame.Rect(x, y, enemy_w, enemy_h))


for _ in range(3):
    spawn_enemy()


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


running = True
while running:
    clock.tick(60)
    screen.fill(DARK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset game
                enemies.clear()
                for _ in range(3):
                    spawn_enemy()
                score = 0
                enemy_speed = 6
                game_over = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 50 - player_w:
            player_x += player_speed

    # Draw road
    pygame.draw.rect(screen, (60,60,60), (50, 0, WIDTH-100, HEIGHT))

    road_line_y += road_speed
    if road_line_y >= 40:
        road_line_y = 0

    for i in range(-40, HEIGHT, 40):
        pygame.draw.rect(screen, YELLOW, (WIDTH//2-5, i + road_line_y, 10, 25))

    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)

    if not game_over:
        for enemy in enemies:
            enemy.y += enemy_speed

            if enemy.y > HEIGHT:
                enemy.y = random.randint(-600, -100)
                enemy.x = random.randint(60, WIDTH - 60 - enemy_w)
                score += 1

            if player_rect.colliderect(enemy):
                game_over = True

        if score % 5 == 0 and score != 0:
            enemy_speed = 6 + score * 0.2

    # Draw cars
    pygame.draw.rect(screen, BLUE, player_rect, border_radius=8)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy, border_radius=8)

    draw_text(f"Score: {score}", font, WHITE, 20, 20)

    if game_over:
        draw_text("GAME OVER", big_font, RED, WIDTH//2 - 170, HEIGHT//2 - 50)
        draw_text("Press R to Restart", font, WHITE, WIDTH//2 - 120, HEIGHT//2 + 20)

    pygame.display.update()

pygame.quit()