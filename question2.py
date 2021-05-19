import pygame
import sys



class Question:  #(stark inspiriert von https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame)
    """functions for every single question."""

    def __init__(self,quiz): #self is an instance of the main game.
        self.settings = quiz.settings
        self.screen = quiz.screen

        self.input_rect = pygame.Rect(50,50,140,32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('dodgerblue2')
        #color = color_passive
        self.base_font = pygame.font.Font(None,32)
        self.user_text = ''
        self.active = False
        self.round_name = False #quiz.round_name
        self.round_mc = False #quiz.round_mc

    def get_name(self):
        names = []
        self.name = self.user_text
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
               # quiz.done == True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.input_rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
               # self.color = self.color_active if self.active else self.color_passive

            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.user_text)
                        self.user_text = ''
                        names.append(self.name)
                        print(names)
                        #loop break or keyup event?
                        self.round_name = False
                        self.round_mc = True
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

        for name in names:
            with open(self.filename, 'a') as file_object:
                file_object.write(name)
                file_object.write(": ")
                #file_object.write(str(score))
                file_object.write("\n")
                
        self.screen.fill((30, 30, 30))
                # Render the current text.
        txt_surface = self.base_font.render(self.user_text, True, self.color_active)
        # Resize the box if the text is too long.
        self.width = max(200, txt_surface.get_width()+10)
        self.input_rect.w = self.width
        # Blit the text.
        self.screen.blit(txt_surface, (self.input_rect.x+5, self.input_rect.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(self.screen, self.color_active, self.input_rect, 2)

        pygame.display.flip()
