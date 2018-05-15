import time

import pygame

import sys

class Morse:
    def __init__(self):
        
        pygame.init()

        size = width, height = 650, 500
        speed = [2, 2]
        black = 0, 0, 0

        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('MORSE')



        self.my_image = pygame.image.load('images/bg.jpg')

        self.input_button = pygame.image.load("images/type.png")

        self.file_button = pygame.image.load("images/f-1.png")

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Some Text', False, (0, 0, 0));



        self.sound = pygame.mixer.Sound("audio/beep.wav")



        self.letters_and_numbers_codes = {"A": [1,2], "B": [2,1,1,1], "C": [2,1,2,1], "D": [2,1,1], "E": [1],"F": [1,1,2,1],
                                     "G": [2,2,1],"H":[1,1,1,1], "I":[1,1], "J":[1,2,2,2], "K":[2,1,2], "L":[1,2,1,1], "M":[2,2], "N":[2,1],
                                     "O":[2,2,2], "P":[1,2,2,1], "Q": [2,2,1,2], "R":[1,2,1], "S": [1,1,1], "T":[2],"U":[1,1,2],
                                     "V":[1,1,1,2], "W":[1,2,2], "X":[2,1,1,2], "Y":[2,1,2,2], "Z":[2,2,1,1], "1":[1,2,2,2,2],
                                     "2":[1,1,2,2,2], "3":[1,1,1,2,2], "4":[1,1,1,1,2], "5":[1,1,1,1,1], "6":[2,2,1,1,1], "7":[2,2,2,1,1],
                                     "8":[2,2,2,1,1], "9":[2,2,2,2,1], "0":[2,2,2,2,2]}

    def s(self, n):
        pygame.mixer.Sound.play(self.sound, n)


    def open_file(self, f):
        f = '/Users/ + f'
        with open(f, 'r') as input:
            return input.read()

                    



    def play_morse(self, text):

        for i in text:

            i = i.upper()

            print(i)
            if i not in self.letters_and_numbers_codes:

                if i == "\n":
                    time.sleep(3)
                elif i == " ":
                    time.sleep(2)
                else:
                    time.sleep(1.5)

                continue

            time.sleep(1)
            for n in self.letters_and_numbers_codes[i]:
                self.s(n)
                time.sleep(0.5)





        return text


    def play_from_file(self, f):
        text = open_file(f)
        self.play_morse(text)


    def play_from_input(self, text):

        self.play_morse(text)



    def main_file(self):
        screen = pygame.display.set_mode((650, 500))

        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = pygame.Color('black')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False
        pygame.font.init()
        myfont = pygame.font.SysFont('Callibri', 50)
        textsurface = myfont.render('Enter the file location', False, (0, 0, 0));



        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active

                    else:
                        active = False
                    # Change the current color of the input box.

                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                            self.play_from_file(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill((255, 255, 215))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)

            screen.blit(textsurface, (50, 0))

            pygame.display.flip()
            # clock.tick(30)




    screen = pygame.display.set_mode((650, 500))
    def main_input(self):


        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = pygame.Color('black')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''

        done = False
        pygame.font.init()
        myfont = pygame.font.SysFont('Callibri', 50)
        textsurface = myfont.render('Press enter to submit for morse', False, (0, 0, 0));



        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active

                    else:
                        active = False
                    # Change the current color of the input box.

                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text)


                            self.play_from_input(text)




                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill((255, 255, 215))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(self.screen, color, input_box, 2)

            self.screen.blit(textsurface, (50, 0))

            pygame.display.flip()
            # clock.tick(30)




    


    def button_input(self,x, y, w,h, i, a, action="none"):
        click = pygame.mouse.get_pressed()
        type = pygame.draw.rect(self.screen, i, (x, y, w, h));


        mouse = pygame.mouse.get_pos()


        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen, a, (x, y, w, h));
            if click[0] == 1 and action != "none":
                action()


    def start(self):



        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()




            self.screen.fill([255, 255, 215])
            self.screen.blit(self.my_image, (0, 0))




            self.button_input(50, 390, 230, 120, (255, 255, 215), (114, 13, 87), self.main_input)

            self.button_input(415, 380, 200, 130, (255, 255, 215), (114, 113, 87), self.main_file)

            self.screen.blit(self.input_button, (50, 320))

            self.screen.blit(self.file_button, (450,365))

            pygame.display.flip()



Morse().start()

