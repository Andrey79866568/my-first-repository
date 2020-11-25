import pygame

w, n = input().split()


def draw_ci(color, cent, radius):
    pygame.draw.circle(screen, color, cent, radius)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Мишень')
    # размеры окна:
    flag = True
    try:
        assert '.' not in w and '.' not in n
        w = int(w)
        n = int(n)
        assert w * n * 2 < 800
    except AssertionError:
        print('Неправильный формат ввода')
        flag = False
    except ValueError:
        print('Неправильный формат ввода')
        flag = False
    if flag:
        colors = ['red', 'green', 'blue']
        size = width, height = w * n * 2, w * n * 2
        center = w * n, w * n
        rad = w * n
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        # формирование кадра:
        # команды рисования на холсте
        for i in range(n):
            draw_ci(colors[i % 3], center, rad - i * w)
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
    pygame.quit()
