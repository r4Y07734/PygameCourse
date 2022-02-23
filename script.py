#music from Music from https://pixabay.com/music/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6094
#image from https://www.hongkiat.com/blog/cartoon-character-design-tutorials/

import pygame
from pygame import mixer

pygame.init()
mixer.init()

win=pygame.display.set_mode((750,425))
pygame.display.set_caption("Pygame course")

character = pygame.image.load("image.jpg")
mixer.music.load("music.mp3")
mixer.music.play()

while True:
    pygame.event.pump()

    win.fill((0,0,0))

    win.blit(character, (0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break

    pygame.display.flip()