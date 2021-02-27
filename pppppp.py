import pygame

screen = pygame.display.set_mode((850, 850))
clock = pygame.time.Clock()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 40

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        screen.fill((0, 0, 0))
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.circle(screen, (0, 0, 255),
                                       (self.left + j * self.cell_size + self.cell_size // 2,
                                        self.top + i * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2 - 2)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (self.left + j * self.cell_size + self.cell_size // 2,
                                        self.top + i * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2 - 2)
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if x - self.left <= 0 or y - self.top <= 0 \
                or x - self.left >= self.width * self.cell_size\
                or y - self.top >= self.height * self.cell_size:
            return None
        return (y - self.top) // self.cell_size, (x - self.left) // self.cell_size


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.red = None

    def get_click(self, mouse_pos):
        self.on_click(self.get_cell(mouse_pos))

    def on_click(self, cell):
        if cell is not None:
            row = cell[0]
            col = cell[1]
            if self.board[row][col] == 0:
                if self.red is not None:
                    if self.has_path(*self.red, row, col):
                        self.red = None
                else:
                    self.board[row][col] = 1
            elif self.board[row][col] == 1:
                if self.red is None:
                    self.board[row][col] = 2
                    self.red = (row, col)
            elif self.board[row][col] == 2:
                self.board[row][col] = 1
                self.red = None
            self.render()

    def has_path(self, x1, y1, x2, y2):
        field = [[-1] * (len(self.board[0]) + 2)]
        field += list(map(lambda string: [-1] + list(map(lambda x: 0 if x in {0, 2} else -1, string)) + [-1], self.board))
        field += [field[0]]

        level = self.set_values(field, 1, x1, y1, x2, y2)

        if level is not None:
            x, y = x2, y2
            path = [(x2, y2)]
            while level > 1:
                for i, j in [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]:
                    if field[i + 1][j + 1] < level and field[i + 1][j + 1] not in {-1, 0}:
                        print(level)
                        level = field[i + 1][j + 1]
                        x, y = i, j
                path.append((x, y))

            self.board[x1][y1] = 0
            for x, y in reversed(path):
                self.board[x][y] = 2
                self.render()
                pygame.display.flip()
                clock.tick(20)
                self.board[x][y] = 0

            self.board[x2][y2] = 1
            return True

    def set_values(self, field, level, x1, y1, x2, y2):
        if (x1, y1) == (x2, y2):
            return level
        elif field[x1 + 1][y1 + 1] == 0 or field[x1 + 1][y1 + 1] > level:
            field[x1 + 1][y1 + 1] = level
            for i, j in [(x1 + 1, y1), (x1, y1 - 1), (x1 - 1, y1), (x1, y1 + 1)]:
                res1 = self.set_values(field, level + 1, i, j, x2, y2)
                if res1 is not None:
                    return res1


lines = Lines(20, 20)
lines.render()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            lines.get_click(event.pos)
    pygame.display.flip()
