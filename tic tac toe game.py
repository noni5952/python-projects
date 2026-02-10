import pygame
import random

# Initialize Pygame
pygame.init()

# Game dimensions and settings (example values)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temple Run Clone")
FPS = 60
clock = pygame.time.Clock()

# Colors (example values)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Player properties (example values)
player_size = [30, 50]
player_x = 50
player_y = HEIGHT - player_size[1] - 50  # Position above ground
player_y_vel = 0
gravity = 1
jumping = False

# Obstacle/Coin lists and speed
obstacles = []
coins = []
game_speed = 5

# Font for score
font = pygame.font.Font(None, 36)
score = 0

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, *player_size)) #

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, 30, 50)) # Example size

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not jumping:
            player_y_vel = -15
            jumping = True

    # Apply gravity
    player_y_vel += gravity
    player_y += player_y_vel
    
    # Ground collision
    if player_y >= HEIGHT - player_size[1] - 50:
        player_y = HEIGHT - player_size[1] - 50
        jumping = False
    
    # Spawn obstacles (simplified logic)
    if random.randint(1, 100) < 2:
        obstacles.append([WIDTH, HEIGHT - 50 - 50]) # Add obstacle at right edge
    
    # Move and draw obstacles, check collision
    for obstacle in obstacles[:]:
        obstacle[0] -= game_speed
        draw_obstacle(*obstacle)
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], 30, 50) # Example size
        player_rect = pygame.Rect(player_x, player_y, *player_size)
        if player_rect.colliderect(obstacle_rect):
            running = False # Game over
        if obstacle[0] < -30:
            obstacles.remove(obstacle)

    # Draw player and ground
    draw_player(player_x, player_y)
    pygame.draw.rect(screen, (139, 69, 19), (0, HEIGHT - 50, WIDTH, 50)) # Ground

    # Score display
    score += 0.1 # Increase score over time
    score_text = font.render(f"Score: {int(score)}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
