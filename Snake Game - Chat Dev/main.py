'''
This is the main file of the Snake game.
'''
import pygame
import sys
import random
from pygame.locals import *
# Initialize the game
pygame.init()
# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE
# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set up the direction constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
# Set up the game clock
clock = pygame.time.Clock()
# Set up the game window
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
# Set up the fonts
font = pygame.font.Font(None, 36)
def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(window_surface, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(window_surface, WHITE, (0, y), (WINDOW_WIDTH, y))
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window_surface, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
def draw_food(food):
    pygame.draw.rect(window_surface, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
def get_random_location():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
def is_collision(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        return True
    for segment in snake[1:]:
        if segment == head:
            return True
    return False
def main():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    food = get_random_location()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == ord('w'):
                    direction = UP
                elif event.key == K_DOWN or event.key == ord('s'):
                    direction = DOWN
                elif event.key == K_LEFT or event.key == ord('a'):
                    direction = LEFT
                elif event.key == K_RIGHT or event.key == ord('d'):
                    direction = RIGHT
        if direction == UP:
            new_head = (snake[0][0], snake[0][1] - 1)
        elif direction == DOWN:
            new_head = (snake[0][0], snake[0][1] + 1)
        elif direction == LEFT:
            new_head = (snake[0][0] - 1, snake[0][1])
        elif direction == RIGHT:
            new_head = (snake[0][0] + 1, snake[0][1])
        snake.insert(0, new_head)
        if snake[0] == food:
            food = get_random_location()
        else:
            snake.pop()
        window_surface.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        pygame.display.update()
        if is_collision(snake):
            pygame.quit()
            sys.exit()
        clock.tick(10)
if __name__ == '__main__':
    main()