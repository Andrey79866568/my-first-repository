import pygame

x, y = input().split()


def draw():
    screen.fill((0, 0, 0))
    color = pygame.Color('#ff0000ff')
    pygame.draw.rect(screen, color, (1, 1, width - 2, height - 2))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Крест')
    # размеры окна:
    flag = True
    try:
        assert '.' not in x and '.' not in y
        x = int(x)
        y = int(y)
        assert x < 1200 and y < 800
    except AssertionError:
        print('Неправильный формат ввода')
        flag = False
    except ValueError:
        print('Неправильный формат ввода')
        flag = False
    if flag:
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