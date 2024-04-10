import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird attributes
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
BIRD_X = 50
BIRD_Y = 300
GRAVITY = 0.5
JUMP_FORCE = 10

# Pipe attributes
PIPE_WIDTH = 50
PIPE_GAP = 200
PIPE_VELOCITY = 3

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load images
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill((255, 255, 0))

# Function to draw the bird
def draw_bird(x, y):
    screen.blit(bird_image, (x, y))

# Function to draw pipes
def draw_pipe(x, y, pipe_height, gap):
    top_pipe_height = y - gap // 2
    bottom_pipe_height = SCREEN_HEIGHT - (y + gap // 2)

    pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(x, 0, PIPE_WIDTH, top_pipe_height))
    pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(x, SCREEN_HEIGHT - bottom_pipe_height, PIPE_WIDTH, bottom_pipe_height))

# Function to check collision
def is_collision(bird_x, bird_y, pipe_x, pipe_top_height, pipe_bottom_height):
    if bird_x + BIRD_WIDTH > pipe_x and bird_x < pipe_x + PIPE_WIDTH:
        if bird_y < pipe_top_height or bird_y + BIRD_HEIGHT > pipe_top_height + PIPE_GAP:
            return True
    return False

# Main game loop
def main():
    running = True
    while running:
        bird_y_change = 0
        bird_y = BIRD_Y

        pipe_x = SCREEN_WIDTH
        pipe_gap_start = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)

        score = 0

        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_y_change = -JUMP_FORCE

            # Bird movement
            bird_y += bird_y_change
            bird_y_change += GRAVITY

            # Pipe movement
            pipe_x -= PIPE_VELOCITY

            # Collision detection
            if is_collision(BIRD_X, bird_y, pipe_x, pipe_gap_start, pipe_gap_start + PIPE_GAP) or bird_y >= SCREEN_HEIGHT or bird_y <= 0:
                game_over = True

            # Score update
            if pipe_x + PIPE_WIDTH < BIRD_X and pipe_x + PIPE_WIDTH + PIPE_VELOCITY >= BIRD_X:
                score += 1

            if pipe_x + PIPE_WIDTH < 0:
                pipe_x = SCREEN_WIDTH
                pipe_gap_start = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)

            # Clear the screen
            screen.fill(WHITE)

            # Draw objects
            draw_bird(BIRD_X, bird_y)
            draw_pipe(pipe_x, pipe_gap_start, SCREEN_HEIGHT, PIPE_GAP)

            # Display score
            font = pygame.font.Font(None, 36)
            text = font.render("Score: " + str(score), True, BLACK)
            screen.blit(text, (10, 10))

            # Update the display
            pygame.display.update()

            # Cap the frame rate
            clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
