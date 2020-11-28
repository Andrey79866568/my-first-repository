import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 255))
    fps = 95  # количество кадров в секунду
    v = 10
    clock = pygame.time.Clock()
    running = True
    start = False
    x, y = 0, 0
    rad = 1
    while running:  # главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                rad = 1
                screen.fill((0, 0, 255))
                start = True
        rad += v * clock.tick(fps) / 1000
        if start:
            pygame.draw.circle(screen, 'yellow', (x, y), rad)
        # обработка остальных событий
        # ...
        # формирование кадра
        # ...
        pygame.display.flip()  # смена кадра
        # изменение игрового мира
        # ...
        # временная задержка
    pygame.quit()
