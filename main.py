import game
import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_widht = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_widht)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

score = 0
font = pygame.font.Font(None, 38)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
game_timer = 30  # 30 секунд на игру
def update_target_position():
    global target_x, target_y
    target_x = random.randint(0, SCREEN_WIDTH - target_widht)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)

while running:
    screen.fill(color)

    current_time = pygame.time.get_ticks()
    time_elapsed = (current_time - start_time) // 1000
    game_timer = max(0, 30 - time_elapsed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_widht and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_widht)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y))

    text = font.render(f"Score: {score} Time: {int(game_timer)}", True, (255, 255, 255))
    screen.blit(text,  (10, 10))

    pygame.display.update()
    clock.tick(60)

    if game_timer <= 0:
        running = False
screen.fill((0, 0, 0))
final_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
screen.blit(final_text, (SCREEN_WIDTH // 2 - final_text.get_width() // 2, SCREEN_HEIGHT // 2 - final_text.get_height() // 2))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
