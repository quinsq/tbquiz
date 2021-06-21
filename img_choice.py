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
        self.score = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if img1_rect.collidepoint(event.pos):#self.img1_clicked:
                    #print('yay')#pass #return score
                    self.score = 1

                elif img2_rect.collidepoint(event.pos):#self.img2_clicked:
                    #print('eureka!')
                    self.score = 2

                print(self.score)
                #ImageButton.check_answer(event.pos)

        self.screen.fill((30,30,30))
        self.screen.blit(image1, img1_rect)
        self.screen.blit(image2, img2_rect)
#        pygame.display.update()


#if __name__ == '__main__':
    #main()
