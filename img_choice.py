import pygame
import sys

class Image:
    def __init__(self,quiz):
        self.settings = quiz.settings
        self.screen = quiz.screen
        image1 = pygame.image.load('dandelion.jpg')
        image2 = pygame.image.load('dan2.jpg')
        img1_rect = image1.get_rect()
        img2_rect = image2.get_rect()
        img1_rect.center = (187.5,350)
        img2_rect.center = (562.5,350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if img1_rect.collidepoint(event.pos):#self.img1_clicked:
                    print('yay')#pass #return score

                elif img2_rect.collidepoint(event.pos):#self.img2_clicked:
                    print('eureka!')
                #ImageButton.check_answer(event.pos)

        self.screen.fill((0,0,0))
        self.screen.blit(image1, img1_rect)
        self.screen.blit(image2, img2_rect)
        pygame.display.update()

