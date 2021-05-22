import pygame

import sys

import logging

from settings import Settings
from button import Button
from question2 import Question
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

        self.play_button = Button(self, "play")
        self.question = Question(self)
        self.mc = Multiple_Choice2(self)
        self.round_name = False # App starts with name-question
        self.round_mc = False # Multiple choice can be activated


        #rounds = {
         #   'NAME': Question('Please enter your name and confirm it by pressing "Enter"'),
          #  'MULTIPLE CHOICE': Multiple_Choice()
        #}
        #round = rounds['TITLE']


    def run_game(self): # Main Method
        clock = pygame.time.Clock()
        done = False
        self.round_name = False # App starts with name-question
        self.round_mc = False # Multiple choice can be activated


        while True:

            if not self.round_name or self.round_mc:
                self._check_events()
                self._update_screen()

            if self.round_name:
                self.question.get_name()
                if self.round_name == False:
                    print('why')

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
