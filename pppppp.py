import pygame

def draw():
    screen.fill((0, 0, 0))
    color = pygame.Color('#ff0000ff')
    pygame.draw.rect(screen, color, (1, 1, width - 2, height - 2))


if __name__ == '__main__':
    x, y = input().split()
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Крест')
    # размеры окна:
    assert '.' not in x and '.' not in y
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError('Это далеко не числа. Ты там прогу не попутал?!\n:)')
    assert x < 1200 and y < 800
    size = width, height = x, y
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    draw()
    # ...
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
