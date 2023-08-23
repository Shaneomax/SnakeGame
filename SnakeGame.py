import pygame
import random

WIDTH = 600
HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = "right"
        self.speed = 10

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == "up":
            y -= self.speed
        elif self.direction == "down":
            y += self.speed
        elif self.direction == "left":
            x -= self.speed
        elif self.direction == "right":
            x += self.speed

        new_head = (x, y)
        self.body.insert(0, new_head)

        if new_head in self.body[1:]:
            self.game_over()

        self.body.pop()

    def game_over(self):
        print("Game over!")
        pygame.quit()
        exit()

    def draw(self, screen):
        for position in self.body:
            x, y = position
            pygame.draw.rect(screen, BLUE, (x, y, 10, 10))

class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10))

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x, y, 10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake.direction = "down"
                elif event.key == pygame.K_LEFT:
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    snake.direction = "right"

        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)

        pygame.display.update()
        snake.move()

        if snake.body[0] == food.position:
            snake.body.append(food.position)
            food = Food()

    pygame.quit()

if __name__ == "__main__":
    main()
