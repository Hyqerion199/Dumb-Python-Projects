import pygame
import sys
import random

# Game constants
TILE_SIZE = 40
GRID_SIZE = 10
WINDOW_WIDTH = GRID_SIZE * TILE_SIZE
WINDOW_HEIGHT = GRID_SIZE * TILE_SIZE

# Color constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Zone for check around clicked tile
AROUND = [-1, 0, 1]

def check_around(x, y, grid):
    num = 0
    for i in AROUND:
        for j in AROUND:
            if i == 0 and j == 0:
                continue
            elif -1<x+i<GRID_SIZE and -1<y+j<GRID_SIZE and grid[x+i][y+j] == -1:
                num += 1
    return num

def reveal_around(x, y, grid, revealed):
    for i in AROUND:
        for j in AROUND:
            if i == 0 and j == 0:
                continue
            elif -1<x+i<GRID_SIZE and -1<y+j<GRID_SIZE and grid[x+i][y+j] != -1:
                revealed[x+i][y+j] = 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize the game grid
    grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
    revealed = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

    # Place the mines and calculate numbers
    for _ in range(int(GRID_SIZE*GRID_SIZE/10)):
        x, y = random.randint(0,GRID_SIZE-1), random.randint(0,GRID_SIZE-1)
        grid[x][y] = -1

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] != -1:
                grid[x][y] = check_around(x, y, grid)

    # Drawing the grid
    def draw_grid():
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if revealed[x][y] == 0:
                    pygame.draw.rect(screen, BLACK, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                else:
                    pygame.draw.rect(screen, GRAY, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    if grid[x][y] == -1:
                        pygame.draw.rect(screen, RED, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Game is running until the user closes it
    running = True
    won = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // TILE_SIZE, event.pos[1] // TILE_SIZE
                if revealed[x][y] == 0:
                    if grid[x][y] != -1:
                        revealed[x][y] = 1
                        if grid[x][y] == 0:
                            reveal_around(x, y, grid, revealed)
                    else:
                        # Mine clicked
                        for i in range(GRID_SIZE):
                            for j in range(GRID_SIZE):
                                revealed[i][j] = 1
                        print('Sorry, you lost!')
                        running = False
        unsolved = sum(line.count(0) for line in revealed)
        if unsolved == int(GRID_SIZE*GRID_SIZE/10):
            print("Congrats, you won!")
            won = True
            running = False

        draw_grid()
        pygame.display.flip()  # Changed 'handler()' to 'flip()'
        clock.tick(60)

    pygame.quit()
    if won:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()