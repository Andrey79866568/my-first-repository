import pygame


'''
class Cell:
    def __init__(self, coord, size, color=False):
        self.coord = coord
        self.color = color
        self.size = size

    def change_color(self):
        self.color = not self.color
    
    def draw(self):
        pygame.draw.rect(screen, 'white', (self.coord[0], self.coord[1], self.size, self.size), 1)
'''


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['black'] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x = self.left
        y = self.top
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, self.board[i][j], (x, y, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, 'white', (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            x = self.left
            y += self.cell_size

    def get_cell(self, mouse_pos):
        x, y = (mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return -1
        return x, y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.board[y][x] == 'black':
            self.board[y][x] = 'red'
        elif self.board[y][x] == 'red':
            self.board[y][x] = 'blue'
        elif self.board[y][x] == 'blue':
            self.board[y][x] = 'black'


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    board = Board(7, 7)
    board.set_view(10, 10, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
