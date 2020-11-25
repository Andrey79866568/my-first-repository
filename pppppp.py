import pygame


def draw():
    screen.fill((0, 0, 0))
    color = pygame.Color('#ffffff')
    pygame.draw.line(screen, color, (0, 0), (width, height), 5)
    pygame.draw.line(screen, color, (width, 0), (0, height), 5)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Крест')
    # размеры окна:
    size = width, height = 800, 600
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