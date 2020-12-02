import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    rad = 20
    color = pygame.Color('red')
    fps = 95
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    clock = pygame.time.Clock()
    running = True
    pygame.draw.circle(screen, color, (x, y), rad)
    pygame.display.flip()
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            clock.tick()
            while abs(x1 - x) > 3 or abs(y1 - y) > 3:
                dex = x1 - x
                dey = y1 - y
                vx = int(dex / abs(dex)) * 100
                vy = int(dey / abs(dey)) * 100
                time = clock.tick(fps)
                if abs(dex) > 3:
                    x += vx * time / 1000
                if abs(dey) > 3:
                    y += vy * time / 1000
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, color, (x, y), rad)
                pygame.display.flip()
    pygame.quit()
