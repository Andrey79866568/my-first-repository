import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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
                pygame.draw.rect(screen, 'white', (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size
            x = self.left
            y += self.cell_size


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
