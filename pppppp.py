import pygame
from math import sin, cos, pi


def vent(a, color):
    # 1
    pygame.draw.polygon(screen, color,
                        ((w // 2, h // 2),
                         (int(x + le * sin(23 * pi / 12 + a)), int(y - le * cos(23 * pi / 12 + a))),
                         (int(x + le * sin(pi / 12 + a)), int(y - le * cos(pi / 12 + a)))))
    # 2
    pygame.draw.polygon(screen, color,
                        ((w // 2, h // 2),
                         (int(x + le * sin(7 * pi / 12 + a)), int(y - le * cos(7 * pi / 12 + a))),
                         (int(x + le * sin(3 * pi / 4 + a)), int(y - le * cos(3 * pi / 4 + a)))))
    # 3
    pygame.draw.polygon(screen, color,
                        ((w // 2, h // 2),
                         (int(x + le * sin(5 * pi / 4 + a)), int(y - le * cos(5 * pi / 4 + a))),
                         (int(x + le * sin(17 * pi / 12 + a)), int(y - le * cos(17 * pi / 12 + a)))))
    # center
    pygame.draw.circle(screen, color, (w // 2, h // 2), 10)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = w, h = 201, 201
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    x = w // 2
    le = 70 * sin(5 * pi / 12)
    y = h // 2
    v = 0
    alp = 0
    clock = pygame.time.Clock()
    fps = 1000
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    v += 5 * pi / 18
                elif event.button == 3:
                    v -= 5 * pi / 18
        alp += clock.tick(fps) * v / 1000
        screen.fill((0, 0, 0))
        vent(alp, '#ffffff')
        pygame.display.flip()
    pygame.quit()
