import time

import pygame

import sys

# install pygame first. try understanding the code as well.
#  I was focusing more on the interface which i am still working on so i have not paid much attention to this part
# but i know it works. if there's any problem, let me know
pygame.init()



sound = pygame.mixer.Sound("beep.wav")



letters_and_numbers_codes = {"A": [1,2], "B": [2,1,1,1], "C": [2,1,2,1], "D": [2,1,1], "E": [1],"F": [1,1,2,1],
                             "G": [2,2,1],"H":[1,1,1,1], "I":[1,1], "J":[1,2,2,2], "K":[2,1,2], "L":[1,2,1,1], "M":[2,2], "N":[2,1],
                             "O":[2,2,2], "P":[1,2,2,1], "Q": [2,2,1,2], "R":[1,2,1], "S": [1,1,1], "T":[2],"U":[1,1,2],
                             "V":[1,1,1,2], "W":[1,2,2], "X":[2,1,1,2], "Y":[2,1,2,2], "Z":[2,2,1,1], "1":[1,2,2,2,2],
                             "2":[1,1,2,2,2], "3":[1,1,1,2,2], "4":[1,1,1,1,2], "5":[1,1,1,1,1], "6":[2,2,1,1,1], "7":[2,2,2,1,1],
                             "8":[2,2,2,1,1], "9":[2,2,2,2,1], "0":[2,2,2,2,2]}

def s(n):
    pygame.mixer.Sound.play(sound, n)


def open_file(f):
    with open(f, 'r') as input:
        return input.read()

                



def play_morse(text):

    for i in text:

        i = i.upper()

        print(i)
        if i not in letters_and_numbers_codes:

            if i == "\n":
                time.sleep(3)
            elif i == " ":
                time.sleep(2)
            else:
                time.sleep(1.5)

            continue

        time.sleep(1)
        for n in letters_and_numbers_codes[i]:
            s(n)
            time.sleep(0.5)





    return text


def play_from_file(f):
    text = open_file(f)
    play_morse(text)


def play_from_input(text):

    play_morse(text)



def main_file():
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
                        play_from_file(text)
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
def main_input():


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


                        play_from_input(text)




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




size = width, height = 650, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('MORSE')



my_image = pygame.image.load('bg.jpg')

input_button = pygame.image.load("type.png")

file_button = pygame.image.load("f-1.png")

myfont = pygame.font.SysFont('Comic Sans MS', 30)


def button_input(x, y, w,h, i, a, action="none"):
    click = pygame.mouse.get_pressed()
    type = pygame.draw.rect(screen, i, (x, y, w, h));


    mouse = pygame.mouse.get_pos()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, a, (x, y, w, h));
        if click[0] == 1 and action != "none":
            action()


def start():
    global ballrect


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()




        screen.fill([255, 255, 215])
        screen.blit(my_image, (0, 0))




        button_input(50, 390, 230, 120, (255, 255, 215), (114, 13, 87), main_input)

        button_input(415, 380, 200, 130, (255, 255, 215), (114, 113, 87), main_file)

        screen.blit(input_button, (50, 320))

        screen.blit(file_button, (450,365))

        pygame.display.flip()



start()
