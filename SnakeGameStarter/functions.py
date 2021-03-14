# these are some functions we will ask you to
# copy and paste into your demo to save time

def randomize(self):
    self.x = random.randint(0, cell_number - 1)
    self.y = random.randint(0, cell_number - 1)
    self.pos = pygame.math.Vector2(self.x, self.y)


def draw_snake(self):
    for block in self.body:
        x_pos = int(block.x * cell_size)
        y_pos = int(block.y * cell_size)
        block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen, (0, 80, 157), block_rect)


def check_fail(self):
    if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
        self.game_over()


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
