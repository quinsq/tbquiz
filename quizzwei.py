import pygame

import sys

import logging

from settings import Settings
from button import Button
from question2 import Question
from img_choice import Image
#from multiple_choice import Multiple_Choice
from multiple_choice import Multiple_Choice2


class Quiz:
    """overall class to manage game assets and behaviour."""

    def __init__(self):
        """intialize game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #self.screen = attribute, available in all methods of the class
        pygame.display.set_caption("quiz")

        self.round_name = False # App starts with name-question
        self.round_img = False
        self.round_mc = False # Multiple choice can be activated
        self.play_button = Button(self, "play")
        self.question = Question(self)
        self.image = Image(self)
        self.mc = Multiple_Choice2(self)



        #rounds = {
         #   'NAME': Question('Please enter your name and confirm it by pressing "Enter"'),
          #  'MULTIPLE CHOICE': Multiple_Choice()
        #}
        #round = rounds['TITLE']


    def run_game(self): # Main Method
        clock = pygame.time.Clock()
        done = False
        self.round_name = False # App starts with name-question
        self.round_img = False
        self.round_mc = False # Multiple choice can be activated


        while True:

            if not self.round_name or self.round_mc or self.round_img:
                self._check_events()
                self._update_screen()

            if self.round_name:
                self.question.get_name()
                self._next_round()
                if self.round_name == False:
                    print('why')
                    self._next_round()

            if self.round_img:
                self.image.__init__(self)

            if self.round_mc:
                print('self.round_mc')
                self.mc.start()
                self.mc.draw()
            pygame.display.flip()

            clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked:
            self.round_name = True

    def _next_round (self):

        self.next_round_rect = pygame.Rect(600,550,140,32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('dodgerblue2')
        self.base_font = pygame.font.Font(None,32)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
               # quiz.done == True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect
                        # If the user clicked on the input_box rect.
                if self.next_round_rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    print('!')
                    self.round_name = False
                    self.round_img = True

        self.screen.fill((30, 30, 30))
        next_round_surface = self.base_font.render('onwards!', True, (0,0,0))

        self.screen.blit(next_round_surface, (self.next_round_rect.x,self.next_round_rect.y))
        pygame.draw.rect(self.screen,self.color_active,self.next_round_rect)

        pygame.display.flip()

    def _update_screen(self):
        """update images on the screen, and flip to new screen."""
        #redraw screen during each pass through loop.
        self.screen.fill(self.settings.bg_color)

        #draw the play button if game is inactive.
        if not self.round_name:
            self.play_button.draw_button()

        #make most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game.
    quiz = Quiz()
    quiz.run_game()
