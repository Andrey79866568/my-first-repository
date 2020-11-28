import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    fps = 95  # количество кадров в секунду
    clock = pygame.time.Clock()
    x = 0
    y = 0
    xm1 = 0
    ym1 = 0
    xm2 = 0
    ym2 = 0
    a = 100
    running = True
    drawing = False
    color = pygame.Color('green')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xm1, ym1 = xm2, ym2 = event.pos
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    xm2, ym2 = event.pos
                    pygame.draw.circle(screen, pygame.Color('#ff0000'), (xm2, ym2), 10)
                    x = x + (xm2 - xm1)
                    y = y + (ym2 - ym1)
                    xm1, ym1 = xm2, ym2
        pygame.draw.rect(screen, color, (x, y, a, a))
        clock.tick(fps)
        if drawing:
            pygame.draw.circle(screen, pygame.Color('#ff0000'), (xm2, ym2), 10)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
