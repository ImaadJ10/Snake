import pygame
import random

pygame.init()

# Game constants
GAME_WIDTH = 500
GAME_HEIGHT = 500
BLOCK_SIZE = 25
DISPLAY_COLOR = (36, 37, 38)
SNAKE_COLOR = (128, 128, 128)
APPLE_COLOR = (169, 169, 169)
DELAY = 10
SCORE_FONT = pygame.font.SysFont("Helvetica", 30)
LOSE_FONT = pygame.font.SysFont("Helvetica", 50)

# Initializes timer
timer = pygame.time.Clock()

# Initializes game display
display = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
display.fill(DISPLAY_COLOR)

pygame.display.set_caption("Snake Game by Imaad Junaidi")
            
def run_game():
    # Position variables
    snake_blocks = 5
    x0 = 0
    y0 = 0
    snake_x = []
    snake_y = []
    apple_x = int(random.randrange(0, (GAME_WIDTH / BLOCK_SIZE))) * BLOCK_SIZE
    apple_y = int(random.randrange(0, (GAME_HEIGHT / BLOCK_SIZE))) * BLOCK_SIZE

    # Other game settings
    direction = 'R'
    score = 0
    game_over = False
    game_end = False

    while not game_over:

        # Runs when player loses game
        while game_end:
            display.fill(DISPLAY_COLOR)
            score_text = SCORE_FONT.render("Score: " + str(score), True, SNAKE_COLOR)
            score_rect = score_text.get_rect(center=(GAME_WIDTH / 2, 20))
            display.blit(score_text, score_rect)
            lose_text = LOSE_FONT.render("You Lose!", True, SNAKE_COLOR)
            lose_rect = lose_text.get_rect(center=(GAME_WIDTH / 2, GAME_HEIGHT / 2))
            display.blit(lose_text, lose_rect)
            retry_text = SCORE_FONT.render("Press Space to Play Again", True, SNAKE_COLOR)
            retry_rect = retry_text.get_rect(center=(GAME_WIDTH / 2, (GAME_HEIGHT / 2) + 50))
            display.blit(retry_text, retry_rect)
            pygame.display.update()
            for key_event in pygame.event.get():
                if key_event.type == pygame.QUIT:
                    game_end = False
                    game_over = True
                if key_event.type == pygame.KEYDOWN:
                    if key_event.key == pygame.K_SPACE:
                        run_game()

        # Mouse/keyboard input settings
        for key_event in pygame.event.get():
            if key_event.type == pygame.QUIT:
                game_over = True
            if key_event.type == pygame.KEYDOWN:
                if key_event.key == pygame.K_UP:
                    if direction != 'D':
                        direction = 'U' 
                elif key_event.key == pygame.K_DOWN:
                    if direction != 'U':
                        direction = 'D'
                elif key_event.key == pygame.K_LEFT:
                    if direction != 'R':
                        direction = 'L'
                elif key_event.key == pygame.K_RIGHT:
                    if direction != 'L':
                        direction = 'R'

        # Controls movement of snake
        if direction == 'U':
            y0 -= BLOCK_SIZE
        elif direction == 'D':
            y0 += BLOCK_SIZE
        elif direction == 'R':
            x0 += BLOCK_SIZE
        elif direction == 'L':
            x0 -= BLOCK_SIZE

        display.fill(DISPLAY_COLOR)

        # Prints score at the top of the game display
        score_text = SCORE_FONT.render("Score: " + str(score), True, SNAKE_COLOR)
        score_rect = score_text.get_rect(center=(GAME_WIDTH / 2, 20))
        display.blit(score_text, score_rect)
        pygame.display.update()

        # Initializes first apple
        pygame.draw.rect(display, APPLE_COLOR, [apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE])

        # Adds new positions to snake coordinates
        snake_x.append(x0)
        snake_y.append(y0)

        # Clears "tails" of snake that are left behind
        if len(snake_x) > snake_blocks and len(snake_y) > snake_blocks:
            del snake_x[0]
            del snake_y[0]

        # Draws snake body part at each snake coordinate
        for x, y in zip(snake_x, snake_y):
            pygame.draw.rect(display, SNAKE_COLOR, [x, y, BLOCK_SIZE, BLOCK_SIZE])

        # Checks if snake has collided with itself
        for x, y in zip(snake_x[:-1], snake_y[:-1]):
            if x == x0 and y == y0:
                game_end = True
    
        # Checks if snake collided with walls
        if x0 > GAME_WIDTH or x0 < 0 or y0 > GAME_HEIGHT or y0 < 0:
            game_end = True
    
        # Checks to see if snake has "eaten" an apple
        if x0 == apple_x and y0 == apple_y:
            snake_blocks += 1
            score += 1
            # Places apple where there are no snake body parts
            while True:
                apple_x = int(random.randrange(0, (GAME_WIDTH / BLOCK_SIZE))) * BLOCK_SIZE
                apple_y = int(random.randrange(0, (GAME_HEIGHT / BLOCK_SIZE))) * BLOCK_SIZE
                if not any(apple_x == x for x in snake_x) and not any(apple_y == y for y in snake_y):
                    pygame.draw.rect(display, APPLE_COLOR, [apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE])
                    break

        pygame.display.update()

        timer.tick(DELAY)
 
    pygame.quit()
    quit()

run_game()