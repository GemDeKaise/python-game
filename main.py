from itertools import count
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import time
import pygame
import time
import random

pygame.init()

#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
dark_blue = (0, 0, 200)
dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

#DISPLAY
display_width = 500
display_height = 800
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("No Way Anul 2")

#IMAGES
basket_img = pygame.image.load('basket1.png')
basket_img = pygame.transform.scale(basket_img, (150, 100))
bg = pygame.image.load('123.jpg')
bg1 = pygame.image.load('nota-5.jpg')
bg2 = pygame.image.load('10.jpg')
restanta_img = pygame.image.load('restanta.png')
restanta_img = pygame.transform.scale(restanta_img, (150, 100))

clock = pygame.time.Clock()

class Basket(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.hitbox = (self.x+30, self.y + 40, 100, 60)
    def draw(self, window):
        window.blit(basket_img, (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, 150, 80)
    
class Note(object):
    def __init__(self, x, y, f_type):
        self.x = x
        self.y = y
        self.f_type = f_type
        self.hitbox = (self.x, self.y, 100, 100)
    def draw(self, window):
        if self.f_type == 0:
            nota = pygame.image.load('nota5.png')
            self.vel = 10
        if self.f_type == 1:
            nota = pygame.image.load('nota10.png')
            self.vel = 10
        if self.f_type == 3:
            nota = pygame.image.load('bere1.png')
            self.vel = 10
        nota = pygame.transform.scale(nota, (100, 100))
        window.blit(nota, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)
        

class Restante(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.hitbox = (self.x, self.y, 100, 100)
    def draw(self, window):
        window.blit(restanta_img, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, x, y, size):
    regText = pygame.font.Font("freesansbold.ttf", size)
    textSurf, textRect = text_objects(msg, regText)
    textRect.center = (x, y)
    window.blit(textSurf, textRect)

def button(msg, m, b, x, y, width, height, inactive_color, active_color, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+width > mouse[0] > x and y+height > mouse[1] > y):
        pygame.draw.rect(window, active_color, (x, y, width, height))
        if (click[0] == 1 and action != None):
            if (action == "play"):
                if (m == 0):
                    main(0,3)
                if (m == 1):
                    main(200,b)
                if (m == 2):
                    main(500,b)					
            elif (action == "quit"):
                pygame.quit()
                quit()
            elif (action == "back"):
                game_intro()
    else:
        pygame.draw.rect(window, inactive_color, (x, y, width, height))
    message_to_screen(msg, (x + (width/2)), (y + (height/2)), 20)

def help_page():
    b = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white) #help page background here
        message_to_screen("NE VEDEM LA TOAMNA", 250, 200, 30)
        message_to_screen("Ce sa faci, n-ai ce sa faci.", 250, 270, 20)
        message_to_screen("Mai pierzi mai castigi", 250, 300, 20)
        message_to_screen("PICAT", 250, 420, 80)
        button("Back", 0, 0, 100, 600, 75, 50, dark_green, bright_blue, "back")
        button("Mai baga o fisa", 0, 3, 300, 600, 150, 50, dark_green, bright_blue, "play")
        pygame.display.update()
        clock.tick(15)

def nota_10(b):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        window.blit(bg2, (0,0))
        message_to_screen("Felicitari Domnule Student", 250, 400, 30)
        message_to_screen("Esti cam tocilar.", 250, 450, 20)
        message_to_screen("DAR AZI BEM!!!", 250, 500, 20)
        #message_to_screen("dar macar nu te a futut in cur", 250, 330, 20)
        #message_to_screen("Daca mai luai si tu un...", 250, 360, 20)
        #message_to_screen("5", 250, 420, 80)
        button("Esti nebun..vrei 11?", 2, b, 200, 600, 300, 50, dark_green, bright_red, "play")
        button("Sunt multumit asa", 1, 0, 200, 700, 250, 50, dark_green, bright_green, "quit")
        pygame.display.update()
        clock.tick(15)

def nota_5(b):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        window.blit(bg1, (0,0))
        message_to_screen("Felicitari Domnule Student", 250, 400, 30)
        message_to_screen("Iti place sa traiesti periculos.", 250, 450, 20)
        message_to_screen("DAR AZI AI TRECUT!!!", 250, 500, 20)
        #message_to_screen("dar macar nu te a futut in cur", 250, 330, 20)
        #message_to_screen("Daca mai luai si tu un...", 250, 360, 20)
        #message_to_screen("5", 250, 420, 80)
        button("Vrei marire?", 1, b, 200, 600, 300, 50, dark_green, bright_red, "play")
        button("Ma multumesc cu 5-ul", 1, 0, 200, 700, 250, 50, dark_green, bright_green, "quit")
        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(bg, (0,0))
        message_to_screen("Prinde 5-ul", 250, 50, 50)
        button("Start", 0, 3, 200, 630, 100, 75, dark_green, bright_green, "play")
        button("Quit", 0, 3, 400, 700, 75, 50, dark_red, bright_red, "quit")
        pygame.display.update()
        clock.tick(15)
    
def main(m,beri):
    nivel = m // 50 + 1 
    print(m)
    score = m + 1
    daniel_score1 = beri
    note = []
    restante = []
    nota1_add_counter = 0
    note_add_counter = 0
    restanta_add_counter = 0
    add_nota_rate = 30 - nivel * 2
    if add_nota_rate <= 5:
        add_nota_rate = 5
    add_restanta_rate = 120 - nivel * 4
    basket = Basket(display_width * 0.35, display_height - 160)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.x > basket.vel - 5:
            basket.x -= basket.vel
        elif keys[pygame.K_RIGHT] and basket.x < 500 - 150 - basket.vel:
            basket.x += basket.vel  
        window.blit(bg, (0,0))
        note_add_counter += 1
        restanta_add_counter += 1
        if note_add_counter == add_nota_rate:
            note_add_counter = 0
            f_startx = random.randrange(100, display_width - 100)
            f_starty = 0
            f_type = random.randint(0, 1)
            if f_type == 1:
               f_type = random.randint(0, 1)
            if score % 73 == 0:
               f_type = 3
            new_nota = Note(f_startx, f_starty, f_type)
            note.append(new_nota)

        if restanta_add_counter == add_restanta_rate:
            restanta_add_counter = 0
            b_startx = random.randrange(100, display_width - 100)
            b_starty = 0
            new_restanta = Restante(b_startx, b_starty)
            restante.append(new_restanta)
        for item in note:
            item.draw(window)
            item.y += item.vel
        for item in note[:]:
            if (item.hitbox[0] >= basket.hitbox[0] - 20) and (item.hitbox[0] <= basket.hitbox[0] + 70):
                if basket.hitbox[1] - 120 <= item.hitbox[1] <= basket.hitbox[1] - 40:
                    note.remove(item)
                    score += 1				
                    if item.f_type == 0: # 5
                        score += 0
                    if item.f_type == 1: # 10
                        score += 1
                    if item.f_type == 3: # 10
                        daniel_score1 += 1					
        
        for item in restante:
            item.draw(window)
            item.y += item.vel
        for item in restante[:]:
            if (item.hitbox[0] >= basket.hitbox[0]) and (item.hitbox[0] <= basket.hitbox[0] + 50):
                if basket.hitbox[1] - 120 <= item.hitbox[1] <= basket.hitbox[1] - 40:
                    restante.remove(item)
                    daniel_score1 -= 1;														
                    play = True
        message_to_screen("Score: "+str(score), 50, 30, 20)
        message_to_screen("Mai ai: "+str((daniel_score1)) + " Beri", 400, 30, 25)
        message_to_screen("nivel -  " + str(nivel // 2), 220, 30, 25)

        if daniel_score1 == 0:
            help_page()
            play = False
        if score == 199 or score == 200:
            nota_5(daniel_score1)
        if score == 499 or score == 500:
            nota_10(daniel_score1)
        if score % 100 == 0 or score % 100 == 1:
            main(score, daniel_score1)
            play = False

        basket.draw(window)
        pygame.display.update()
        clock.tick(60)
  

game_intro()
main(0,3)
