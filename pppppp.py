import pygame


def draw_rect(x, y):
    color = pygame.Color('red')
    pygame.draw.rect(screen, color, (x, y, 30, 15))


if __name__ == '__main__':
    # инициализация pygame:
    pygame.init()
    pygame.display.set_caption('Кирпичи')
    # размеры окна:
    size = width, height = 300, 200
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('#ffffff'))
    # формирование кадра:
    x1 = 0
    y1 = 0
    for i in range(12):
        for j in range(10):
            draw_rect(x1 + j * 30 + 2 * j, y1 + i * 15 + 2 * i)
        if not(i % 2):
            x1 = -15
        else:
            x1 = 0
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
