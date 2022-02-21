import pygame

pygame.init()

win=pygame.display.set_mode((750,425))
pygame.display.set_caption("Name of my window")
win.fill((0,0,0))

pygame.display.flip()

input()