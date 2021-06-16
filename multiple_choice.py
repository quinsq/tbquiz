import pygame
import sys
import random
import pygame.font
import pygame.freetype

class NameChoice:

    def __init__(self,quiz):
        self.settings = quiz.settings
        self.screen = quiz.screen
        pygame.freetype.init()
        self.background = pygame.Surface((640, 480))
        self.background.fill(pygame.Color('lightgrey'))
        self.FONT = pygame.freetype.SysFont(None, 32)

        self.FONT.render_to(self.background, (120,50), 'Select your difficulty level', pygame.Color('black'))
        self.FONT.render_to(self.background, (119,49), 'Select your difficulty level', pygame.Color('white'))

        self.rects = []
        x = 120
        y = 120
        for n in range(3):
            rect = pygame.Rect(x, y, 80, 300)
            self.rects.append(rect)
            y += 100

        self.names = [
            	'Zephyr',
                'Riley',
                'Tennessee'
                ]

    def start(self, *args):
        pass

    def draw(self):
        self.screen.blit(self.background, (0,0))
        n = 1
        i=0
        for rect in self.rects:
            #print(rect)
            #i=0
            #while i<len(self.names):
            self.FONT.render_to(self.screen, (rect.x+30, rect.y+30), str(self.names[i]), pygame.Color('black'))
            self.FONT.render_to(self.screen, (rect.x+29, rect.y+29), str(self.names[i]), pygame.Color('white'))
            #self.name[i] += 1
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, pygame.Color('darkgrey'), rect)
            i+=1

            n += 1
