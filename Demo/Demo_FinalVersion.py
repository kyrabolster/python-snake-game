import pygame
import sys
import random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(fruit, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)  # right
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 80, 157), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.is_game_over = False
        self.is_game_run = False

    def update(self):
        if self.is_game_run == True:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    def draw_elements(self):
        self.draw_checkerboard()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

        if self.is_game_over == True:
            self.draw_game_over()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.is_game_over = True
        self.is_game_run = False

    def draw_checkerboard(self):
        checkerboard_color = (211, 153, 255)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        checkerboard_rect = pygame.Rect(
                            col * cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(
                            screen, checkerboard_color, checkerboard_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        checkerboard_rect = pygame.Rect(
                            col * cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(
                            screen, checkerboard_color, checkerboard_rect)

    def draw_score(self):
        score_text = "Score: " + str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = (cell_size * cell_number) - 60
        score_y = (cell_size * cell_number) - 40
        score_rect = score_surface.get_rect(center=(score_x, score_y))

        screen.blit(score_surface, score_rect)

    def draw_game_over(self):
        game_over_text = "Game Over :("
        game_over_surface = game_over_font.render(
            game_over_text, True, (pygame.Color('red')))
        game_over_x = (cell_size * cell_number) / 2
        game_over_y = (cell_size * cell_number) / 4 + 100
        game_over_rect = game_over_surface.get_rect(
            center=(game_over_x, game_over_y))
        screen.blit(game_over_surface, game_over_rect)

        game_score_text = "Your score is: " + str(len(self.snake.body)-3)
        game_score_x = (cell_size * cell_number) / 2
        game_score_y = (cell_size * cell_number / 4) + 160
        game_score_surface = game_over_font.render(
            game_score_text, True, (pygame.Color('black')))
        game_score_rect = game_score_surface.get_rect(
            center=(game_score_x, game_score_y))
        screen.blit(game_score_surface, game_score_rect)

        restart_text = "Press any key to restart"
        restart_x = (cell_size * cell_number) / 2
        restart_y = (cell_size * cell_number / 4) + 230
        restart_surface = game_font.render(
            restart_text, True, (pygame.Color('black')))
        restart_rect = restart_surface.get_rect(center=(restart_x, restart_y))
        screen.blit(restart_surface, restart_rect)

    def reset_game(self):
        self.snake.reset()
        self.fruit.randomize()
        self.is_game_over = False


pygame.init()

cell_size = 35
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = pygame.image.load('Graphics/strawberry.png').convert_alpha()
game_font = pygame.font.Font(None, 25)
game_over_font = pygame.font.Font(None, 70)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)  # milliseconds

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if main_game.is_game_over == True:
                main_game.reset_game()
            if main_game.is_game_run == False and (event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT):
                main_game.is_game_run = True
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((224, 170, 255))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
