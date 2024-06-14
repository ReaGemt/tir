import pygame
import random

pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Заголовок окна и иконка
pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Инициализация шрифта
font = pygame.font.Font(None, 38)

# Настройки игры
clock = pygame.time.Clock()
game_duration = 30  # 30 seconds for the game

def update_target_position():
    global target_x, target_y
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Обновление для сброса переменных
def reset_game():
    global target_x, target_y, score, start_time, color, running, game_over
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    score = 0
    start_time = pygame.time.get_ticks()
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    running = True
    game_over = False

# Кнопка
def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, (0, 0, 0), [x, y, width, height])
    button_text = font.render(text, True, (255, 255, 255))
    screen.blit(button_text, (x + (width - button_text.get_width()) // 2, y + (height - button_text.get_height()) // 2))
    return pygame.Rect(x, y, width, height)

# Инициализация игровых переменных
reset_game()

while True:
    while running:
        screen.fill(color)

        current_time = pygame.time.get_ticks()
        time_elapsed = (current_time - start_time) // 1000
        remaining_time = max(0, game_duration - time_elapsed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                    score += 1
                    update_target_position()

        screen.blit(target_img, (target_x, target_y))

        text = font.render(f"Очки: {score} Время: {int(remaining_time)}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

        if remaining_time <= 0:
            running = False
            game_over = True

    while game_over:
        screen.fill((0, 0, 0))
        final_text = font.render(f"Ваш счёт: {score}", True, (255, 255, 255))
        screen.blit(final_text, (SCREEN_WIDTH // 2 - final_text.get_width() // 2, SCREEN_HEIGHT // 2 - final_text.get_height() // 2))

        button_rect = draw_button("Начать заново", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    reset_game()
                    game_over = False

        clock.tick(60)
