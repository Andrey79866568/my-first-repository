import pygame
from copy import deepcopy

screen = pygame.display.set_mode((850, 850))


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 20

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
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        self.on_click(self.get_cell(mouse_pos))

    def get_cell(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if x - self.left <= 0 or y - self.top <= 0 \
                or x - self.left >= self.width * self.cell_size\
                or y - self.top >= self.height * self.cell_size:
            return None
        return (y - self.top) // self.cell_size, (x - self.left) // self.cell_size

    def on_click(self, cell):
        if cell is not None:
            row = cell[0]
            col = cell[1]
            self.board[row][col] = 1
            self.render()


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def next_move(self):
        board1 = deepcopy(self.board)
        for row in range(self.height):
            for col in range(self.width):
                count = 0
                for i in range(3):
                    for j in range(3):
                        if i == 1 and j == 1:
                            continue
                        if self.board[(row + i - 1) % self.height][(col + j - 1) % self.width] == 1:
                            count += 1
                if self.board[row][col] == 1 and count not in {2, 3}:
                    board1[row][col] = 0
                elif self.board[row][col] == 0 and count == 3:
                    board1[row][col] = 1
        self.board = board1
        self.render()


board = Life(40, 40)
processing = False
fps = 4
time = 0
clock = pygame.time.Clock()
board.render()
running = True
while running:
    time += clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif (
                event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT or
                event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]
        ) and not processing:
            board.get_click(event.pos)
        elif (
                event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or
                event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT
        ):
            processing = ~processing

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_WHEELUP:
                fps *= 1.5
            elif event.button == pygame.BUTTON_WHEELDOWN:
                fps /= 1.5

    if processing and time >= 1000 / fps:
        board.next_move()
        time = 0

    pygame.display.flip()
