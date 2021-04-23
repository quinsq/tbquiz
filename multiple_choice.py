import pygame
import sys
import random

class Multiple_Choice:
    def __init__(self, quiz):

        self.settings = quiz.settings
        self.screen = quiz.screen

        self.input_rect = pygame.Rect(50,50,140,32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('dodgerblue2')
        #color = color_passive
        self.base_font = pygame.font.Font(None,32)
        self.questions_mc = [
            ('Which beverage do you prefer?'),
            ('Which of the following pet do you identify with the most?')
        ]

        self.current_question = None
        self.question_index = 0
        self.answers_mc = []

    def question_shuffle(self):
        q = self.questions_mc[0]
        self.questions_mc.remove(q)
        self.current_question = q
        self.question_index += 1
        return q

    def pop_question(self):
        q = self.questions[0]
        self.questions.remove(q)
        self.current_question = q
        return q

    def get_result(self):
        return 'Your answer is {self.answer}'

class Multiple_Choice2:  #Durchführung der Fragen
    def __init__(self,quiz):
        self.settings = quiz.settings
        self.screen = quiz.screen

        self.input_rect = pygame.Rect(50,50,140,32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('dodgerblue2')
        #color = color_passive
        self.base_font = pygame.font.Font(None,32)
        self.rects = []

        for n in range(4):
            rect = pygame.Rect(50, (n * 70) + 100, 500, 50)
            self.rects.append(rect)

        self.choices = [["Apple Juice", "Lemonade", "Water", "Coffee"], ["Guinea Pig", "Dog", "Cat", "Canary"]]  # Choices for questions set up in class before


    def start(self, Multiple_Choice):
        self.background = pygame.Surface((640, 480))
        self.background.fill(pygame.Color('lightgrey'))
        self.multiple_choice = Multiple_Choice
        question, answer = multiple_choice.pop_question()
        #SimpleScene.FONT.render_to(self.background, (120, 50), question, pygame.Color('black'))
        #SimpleScene.FONT.render_to(self.background, (119, 49), question, pygame.Color('white'))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        n = 0
        for rect in self.rects:
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, pygame.Color('darkgrey'), rect)
            pygame.draw.rect(screen, pygame.Color('darkgrey'),
                             rect, 5)


            for i in range(len(self.choices)):
                if self.multiple_choice.question_index ==  i + 1:
                    self.base_font.render_to(screen, (rect.x+30, rect.y+20), str(self.choices[i][n]), pygame.Color('black'))
                    self.base_font.render_to(screen, (rect.x+29, rect.y+19), str(self.choices[i][n]), pygame.Color('white'))
            n+=1

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                n = 1
                for rect in self.rects:
                    if rect.collidepoint(event.pos):
                        self.multiple_choice.answer(n)
                        if self.multiple_choice.questions:
                            return ('GAME', self.multiple_choice)
                        else:
                            return ('RESULT', self.multiple_choice.get_result())
                    n += 1
