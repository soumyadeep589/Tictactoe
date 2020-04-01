import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
class Player(object):
    def __init__(self):
        
rect1 = Rectangle(0, 0, 160, 160)
rect2 = Rectangle(170, 0, 160, 160)
rect3 = Rectangle(340, 0, 160, 160)
rect4 = Rectangle(0, 170, 160, 160)
rect5 = Rectangle(170, 170, 160, 160)
rect6 = Rectangle(340, 170, 160, 160)
rect7 = Rectangle(0, 340, 160, 160)
rect8 = Rectangle(170, 340, 160, 160)
rect9 = Rectangle(340, 340, 160, 160)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT]:
    #     x -= vel
    # if keys[pygame.K_RIGHT]:
    #     x += vel
    # if keys[pygame.K_UP]:
    #     y -= vel
    # if keys[pygame.K_DOWN]:
    #     y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (rect1.x, rect1.y, rect1.width, rect1.height))
    pygame.draw.rect(win, (255, 255, 255), (rect2.x, rect2.y, rect2.width, rect2.height))
    pygame.draw.rect(win, (255, 255, 255), (rect3.x, rect3.y, rect3.width, rect3.height))
    pygame.draw.rect(win, (255, 255, 255), (rect4.x, rect4.y, rect4.width, rect4.height))
    pygame.draw.rect(win, (255, 255, 255), (rect5.x, rect5.y, rect5.width, rect5.height))
    pygame.draw.rect(win, (255, 255, 255), (rect6.x, rect6.y, rect6.width, rect6.height))
    pygame.draw.rect(win, (255, 255, 255), (rect7.x, rect7.y, rect7.width, rect7.height))
    pygame.draw.rect(win, (255, 255, 255), (rect8.x, rect8.y, rect8.width, rect8.height))
    pygame.draw.rect(win, (255, 255, 255), (rect9.x, rect9.y, rect9.width, rect9.height))
    
    pygame.display.update()
pygame.quit()
