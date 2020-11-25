import pygame

x, n = input().split()


def draw_rect(black, x_r, y_r):
    if black:
        color = pygame.Color('#000000')
    else:
        color = pygame.Color('#ffffff')
    pygame.draw.rect(screen, color, (x_r, y_r, a, a))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Крест')
    # размеры окна:
    flag = True
    try:
        assert '.' not in x and '.' not in n
        x = int(x)
        n = int(n)
        assert x % n == 0
        assert x < 800
    except AssertionError:
        print('Неправильный формат ввода')
        flag = False
    except ValueError:
        print('Неправильный формат ввода')
        flag = False
    if flag:
        a = x // n
        black_str = True
        start_black = True
        size = width, height = x, x
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        # формирование кадра:
        # команды рисования на холсте
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                draw_rect(black_str, width - j * a, height - i * a)
                black_str = not black_str
            start_black = not start_black
            if start_black:
                black_str = True
            else:
                black_str = False
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
    pygame.quit()
