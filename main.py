import sys
import pygame

pygame.init()
# ELEMENTS -------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Spell Race")
pygame.image.load()


clock = pygame.time.Clock()

font_big = pygame.font.Font('freesansbold.ttf', 50)
font_small = pygame.font.Font('freesansbold.ttf', 25)

def write_text(text, color,font, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj, textrect)

mouse_click = False

# PLAYER ---------------------------------------------------------------------------------------------
def main_menu():
    word = "Lucas"
    while True:

        screen.fill((0,0,0))

        write_text("Main Menu",(255, 255, 255),font_big, 465,75)
        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(500,300,200,50)
        if button1.collidepoint((mx,my)):
            button1 = pygame.Rect(500,300,210,60)
            if mouse_click:
                gameplay(word)
        button2 = pygame.Rect(500,400,200,50)
        if button2.collidepoint((mx,my)):
            button2 = pygame.Rect(500,400,210,60)
            if mouse_click:
                word = word_set() # Will return the value for word which can then be used for later.
        pygame.draw.rect(screen,(67, 181, 124), button1)
        pygame.draw.rect(screen,(255,0,0), button2)

        mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # the left moust button is 1
                    mouse_click = True
        
        pygame.display.update()

def word_set():
    running = True
    word = ""
    record = False
    while running:
        
        screen.fill((0,0,0))

        write_text("Word Setting",(255,255,255),font_big, 440,75)
        write_text("Please press enter to set the word for the game and press esc to save.",(255,255,255),font_small, 175,175)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if record:
                    word += event.unicode # to get what button is being pressed.
                if event.key == pygame.K_RETURN:
                    record = not record
                if event.key == pygame.K_ESCAPE:
                    return word
        
        write_text(word,(255,255,255), font_big, 460,250)
        pygame.display.update()


def gameplay(word):
    running = True
    while running:
        
        screen.fill((0,0,0))

        write_text("Gameplay Screen",(255,255,255),font_big, 440,75)
        print(word)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    
        pygame.display.update()
                

main_menu()