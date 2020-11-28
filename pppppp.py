import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    n = 0
    font = pygame.font.Font(None, 200)
    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEOEXPOSE:
            n += 1
        text = font.render(f"{n}", True, pygame.Color('#ffffff'))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
