import sys
import pygame


# ADD DIFFICULTY SETTING BY SETTING THE TIME.

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
                        gameplay(word,10)
                    else:
                        word += event.unicode # to get what button is being pressed.
                if event.key == pygame.K_ESCAPE:
                    return word
        
        button1 = pygame.Rect(500,350,200,50)
        if button1.collidepoint((mx,my)):
            button1 = pygame.Rect(495,345,210,60)
            if mouse_click:
                record = not record
                gameplay(word,10)
        
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


def gameplay(word,seconds):
    """
    Main game loop. The player will type and spell the word in order to progress.
    """
    clock = pygame.time.Clock()
    running = True
    missing = [letter for letter in word]
    spelled = ""
    done = False
    player_x = 20
    opponent_x = player_x
    car_speed = (960/len(word))
    opponent_speed = (960/seconds)
    time = 0

    while running:
        
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if not done:
                    if event.unicode == missing[0]:
                        spelled += event.unicode
                        missing.remove(event.unicode)
                        player_x += car_speed
                        if len(missing) == 0:
                            done = True
                            if opponent.x < 980:
                                winner = True
        

        # CARS ----------------------------------------------------------
        player = pygame.Rect(player_x,475,200,100)
        opponent = pygame.Rect(opponent_x,325,200,100)

        # borders
        if player.x >= 980:
            player.x = 980
        if opponent.x >= 980:
            opponent.x = 980
            if player_x < 980:
                done = True
                winner = False
        # ----------------------------------------------------------------

        time += 1
        if done:
            if winner:
                write_text("Yey, you won!",(255,255,255),font_big, 440,75)
            else:
                write_text("You lost :<",(255,255,255),font_big, 440,75)
        else:
            write_text(word,(255,255,255),font_big, 440,75)
            write_text(spelled,(235, 161, 52),font_big, 440,75)
            if time == 1000:
                time = 0
                opponent_x += opponent_speed
        
        pygame.draw.rect(screen,(52, 186, 235), player)
        pygame.draw.rect(screen,(235, 52, 52), opponent)
        

        clock.tick(1000)
        pygame.display.update()
                

main_menu()