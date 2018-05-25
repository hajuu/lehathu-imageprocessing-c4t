import pygame
import sys, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window_height = 460
window_width = 720
display_surf = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("snake")
fps = 200
fps_clock = pygame.time.Clock()

direction = 'UP'
changeto = direction


class Snake:
    def __init__(self, x, w, h):
        self.w = w
        self.h = h
        self.x = x
        self.y = window_height / 2

    snakePos = [20, 30]  # it works like x and y axis [x,y]
    snakeBody = [[20, 20]]

    def draw(self):
        for pos in self.snakeBody:
            pygame.draw.rect(display_surf, WHITE,
                            pygame.Rect(pos[0], pos[1], 10, 10))

    def right(self):
        if direction == 'RIGHT':
            snakePos[0] += 10

    def left(self):
        if direction == 'LEFT':
            snakePos[0] -= 10

    def up(self):
        if direction == 'UP':
            snakePos[1] += 10

    def down(self):
        if direction == 'DOWN':
            snakePos[1] -= 10

    def update(self):
        snakeBody.insert(0, list(snakePos))

class Game:
    def __init__(self):
        snake_x = 20
        snake_w = 10
        snake_h = 10
        self.snake = Snake(snake_x, snake_w, snake_h)
    def draw_arena(self):
        display_surf.fill((0, 0, 0))
        # pygame.draw.rect(display_surf, BLACK, (10, 10, window_width, window_height))
    def update(self):
        self.draw_arena()
        self.snake.draw()

def main():
    pygame.init()
    game = Game()
    snake = Snake()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # if user hit an button of keyboard
                if event.key == pygame.K_RIGHT or event.key == ord('d'):  # and if that button would be right arrow key
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == ord('w'):
                    changeto = 'DOWN'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    changeto = 'UP'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
            # if event.type == MOUSEMOTION:
            #     game.paddles['user'].move(event.pos)
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        snake.

        game.update()
        # if game.ball.hit_wall():
        #     break
        pygame.display.update()
        # fps_clock.tick(fps)
    # print('Your score:', game.score.score)


if __name__ == '__main__':
    main()
