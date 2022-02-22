import pygame

pygame.init()

win=pygame.display.set_mode((750,425))
pygame.display.set_caption("Pygame course")

while True:
    pygame.event.pump()

    win.fill((0,0,0))

    pygame.draw.rect(win, (0,0,255), (10,10,50,50), 0)
    pygame.draw.circle(win, (255,0,0), (95,35), 25, 0)
    pygame.draw.ellipse(win, (0,255,0), (130,20,50,30), 0)
    pygame.draw.line(win, (255,255,0), (190,34), (240,34), 2)
    pygame.draw.polygon(win, (0,255,255), [(275,10), (300,35), (287.5,60), (262.5,60), (250,35)], 0)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break

    pygame.display.flip()