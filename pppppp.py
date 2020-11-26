import pygame

n = input()


def draw_ci(x_st, y_st):
    color = pygame.Color('#ffffff')
    pygame.draw.ellipse(screen, color, (x_st, y_st, width - 2 * x_st, width - 2 * y_st), 1)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Сфера')
    # размеры окна:
    flag = True
    try:
        assert '.' not in n
        n = int(n)
    except AssertionError:
        print('Неправильный формат ввода')
        flag = False
    except ValueError:
        print('Неправильный формат ввода')
        flag = False
    if flag:
        size = width, height = 300, 300
        delt = (width / n) / 2
        x = 0
        y = 0
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        # формирование кадра:
        # команды рисования на холсте
        for i in range(n):
            draw_ci(x, y)
            x += delt
        x = 0
        for i in range(n):
            draw_ci(x, y)
            y += delt
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
    pygame.quit()
