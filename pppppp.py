import pygame

n = input()


def draw_ci(p1, p2, p3, p4):
    color = pygame.Color('orange')
    pygame.draw.polygon(screen, color, (p1, p2, p3, p4))


if __name__ == '__main__':
    # инициализация pygame:
    pygame.init()
    pygame.display.set_caption('Ромбики')
    # размеры окна:
    flag = True
    try:
        assert '.' not in n
        n = int(n)
        assert n < 300
    except AssertionError:
        print('Неправильный формат ввода')
        flag = False
    except ValueError:
        print('Неправильный формат ввода')
        flag = False
    if flag:
        size = width, height = 300, 300
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('yellow'))
        # формирование кадра:
        k = width // n
        a = n // 2
        x = 0
        y = 0
        for i in range(k):
            for j in range(k):
                draw_ci((x, y + a), (x + a, y), (x + 2 * a, y + a), (x + a, y + 2 * a))
                x += a * 2
            x = 0
            y += a * 2
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
    pygame.quit()
