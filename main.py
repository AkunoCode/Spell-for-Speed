import sys
import pygame

pygame.init()
# ELEMENTS -------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Spell for Speed")
title_img = pygame.image.load("Images/Title.png")


clock = pygame.time.Clock()

font_big = pygame.font.Font('Images/Pixel.ttf', 50)
font_small = pygame.font.Font('Images/Pixel.ttf', 25)

def write_text(text, color,font, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj, textrect)

# Game Loop ------------------------------------------------------------------------------------------------------------------
def main_menu():
    """
    Home menu for the game, Clicking the button will lead to the word setting menu.

    """

    word = "Lucas"
    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill((0,0,0))
        screen.blit(title_img,(350,75))

        mouse_click = False
          
        # Events Section
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # the left moust button is 1
                    mouse_click = True
        button2 = pygame.Rect(500,400,200,50)
        if button2.collidepoint((mx,my)):
            button2 = pygame.Rect(495,395,210,60)
            if mouse_click:
                word_set() # Will return the value for word which can then be used for later.
        
        # Draw section
        pygame.draw.rect(screen,(255,0,0), button2)
        
        pygame.display.update()

def word_set():
    """
    Word setting menu for the game. Will enable the player to set the word to be spelled for the game.
    The word will carry through the main game loop.

    """
    running = True
    word = "Lucas"
    record = False
    text_rect = pygame.Rect(350,250,500,55)

    while running:
        mx, my = pygame.mouse.get_pos()

        screen.fill((0,0,0))

        # Event Section
        mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect.collidepoint(event.pos): # the left moust button is 1
                    record = True
                    word = ""
                if event.button == 1: # the left moust button is 1
                    mouse_click = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if record:
                    if event.key == pygame.K_BACKSPACE:
                        word = word[:-1]
                    elif event.key == pygame.K_RETURN:
                        record = not record
                    else:
                        word += event.unicode # to get what button is being pressed.
                if event.key == pygame.K_ESCAPE:
                    return word
        
        button1 = pygame.Rect(500,350,200,50)
        if button1.collidepoint((mx,my)):
            button1 = pygame.Rect(495,345,210,60)
            if mouse_click:
                gameplay(word)
        
        # Draw Section
        write_text("Word Setting",(255,255,255),font_big, 440,75)
        write_text("Set the word to be spelled for the game round.",(255,255,255),font_small, 300,175)
        
        pygame.draw.rect(screen,(67, 181, 124), button1)

        if record: # The text box
            pygame.draw.rect(screen,(89, 89, 89),text_rect,)
        else:
            pygame.draw.rect(screen,(255,255,255),text_rect,)
        
        text = font_big.render(word,True,(255,255,255))
        screen.blit(text,(text_rect.x +5, text_rect.y -15))

        text_rect.w = max(500,text.get_width() + 10)
        
        pygame.display.update()


def gameplay(word):
    """
    Main game loop. The player will type and spell the word in order to progress.
    """
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