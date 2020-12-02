import pygame

color = pygame.Color(128, 255, 0)
hsv = color.hsva
color.hsva = (hsv[0] + 90, hsv[1], hsv[2])
print(color)
