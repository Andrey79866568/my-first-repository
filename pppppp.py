import pygame


w, hue = input().split()


def draw_cube(x, y):
    pass


if __name__ == '__main__':
    flag = True
    try:
        assert '.' not in w and '.' not in hue
        hue = int(hue)
        w = int(w)
        assert 0 <= w <= 100 and not w % 4 and 0 <= hue <= 360
    except AssertionError:
        print('Неправильный формат ввода')
        flag = False
    except ValueError:
        print('Неправильный формат ввода')
        flag = False
    if flag:
        # инициализация pygame:
        pygame.init()
        pygame.display.set_caption('Cube')
        # размеры окна:
        size = width, height = 300, 300
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color('#000000'))
        # формирование кадра:

        color = pygame.Color(255, 255, 255)
        x = width // 2 - w // (3 / 2)
        y = height // 2 - w // (5 / 2)
        color.hsva = (hue, 100, 50)
        pygame.draw.polygon(screen, color, ((x + w, y + w), (x + w, y),
                                            (x + w // (2 / 3), y - w // 2),
                                            (x + w // (2 / 3), y + w // 2)))
        color.hsva = (hue, 100, 75)
        pygame.draw.rect(screen, color, (x, y, w, w))
        color.hsva = (hue, 100, 100)
        pygame.draw.polygon(screen, color, ((x, y), (x + w, y), (x + w // (2 / 3), y - w // 2),
                                            (x + w // 2, y - w // 2)))

        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
