import pygame
import sys
from variables import SCREEN_WIDTH, SCREEN_HEIGHT, first_elem_y
from pygame.locals import FULLSCREEN
from game import Game


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                              FULLSCREEN)
        self.font = pygame.font.Font('Pixeled.ttf', 25)
        self.music_button = pygame.Rect(SCREEN_WIDTH / 2 - 125,
                                        SCREEN_HEIGHT / 2 - 140, 250, 75)
        self.music_text_off = self.font.render("music off", 1, (0, 0, 0))
        self.music_text_on = self.font.render("music on", 1, (0, 0, 0))
        self.instr_button = pygame.Rect(SCREEN_WIDTH / 2 - 125,
                                        SCREEN_HEIGHT / 2 - 40, 250, 75)
        self.instr_text = self.font.render("intruction", 1, (0, 0, 0))
        self.back_button = pygame.Rect(SCREEN_WIDTH / 2 - 340,
                                       SCREEN_HEIGHT / 2 + 260, 115, 50)
        self.back_text = self.font.render("back", 1, (0, 0, 0))
        self.music_on = True

    def draw_menu(self):
        self.screen.fill([0, 0, 0])
        title_img = pygame.image.load('images/title.png')
        press_space_img = pygame.image.load('images/press_space.png')
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 95,
                                     first_elem_y - 60))

        pygame.draw.rect(self.screen, (255, 255, 255), self.music_button)
        if self.music_on:
            self.screen.blit(self.music_text_on, (SCREEN_WIDTH / 2 - 90,
                                                  SCREEN_HEIGHT / 2 - 143))
        else:
            self.screen.blit(self.music_text_off, (SCREEN_WIDTH / 2 - 95,
                                                   SCREEN_HEIGHT / 2 - 143))
        pygame.draw.rect(self.screen, (255, 255, 255), self.instr_button)
        self.screen.blit(self.instr_text, (SCREEN_WIDTH / 2 - 105,
                                           SCREEN_HEIGHT / 2 - 43))

        self.screen.blit(press_space_img, (SCREEN_WIDTH / 2 - 300,
                                           SCREEN_HEIGHT / 2 + 150))

    def draw_instruction(self):
        self.screen.fill([0, 0, 0])
        title_img = pygame.image.load('images/title.png')
        instruction_img = pygame.image.load('images/instruction.png')
        self.screen.blit(instruction_img, (SCREEN_WIDTH / 2 - 250,
                                           SCREEN_HEIGHT / 2 - 270))
        self.screen.blit(title_img, (SCREEN_WIDTH / 2 - 95,
                                     first_elem_y - 60))

        pygame.draw.rect(self.screen, (255, 255, 255), self.back_button)
        self.screen.blit(self.back_text, (SCREEN_WIDTH / 2 - 330,
                                          SCREEN_HEIGHT / 2 + 245))

    def run(self):
        started = False
        instruction_on = False
        while True:
            pygame.display.update()
            if not started and not instruction_on:
                self.draw_menu()
            elif not started and instruction_on:
                self.draw_instruction()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_SPACE and not started:
                    game = Game()
                    game.run_game(self.music_on)
                    started = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if not instruction_on:
                        if self.music_button.collidepoint(mouse_pos):
                            self.music_on = not self.music_on
                        if self.instr_button.collidepoint(mouse_pos):
                            instruction_on = True
                            break
                    else:
                        if self.back_button.collidepoint(mouse_pos):
                            instruction_on = False


    # self.size_text = self.font.render("select size:", 1, (255, 255, 255))
    # self.small_size_button = pygame.Rect(SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 70, 250, 50)
    # self.small_size_text = self.font.render("small", 1, (0, 0, 0))
    # self.original_size_button = pygame.Rect(SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 130, 250, 50)
    # self.original_size_text = self.font.render("original", 1, (0, 0, 0))
    # self.big_size_button = pygame.Rect(SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 190, 250, 50)
    # self.big_size_text = self.font.render("big", 1, (0, 0, 0))
    #
    # self.screen.blit(self.size_text, (SCREEN_WIDTH / 2 - 115, SCREEN_HEIGHT / 2))
    #
    # pygame.draw.rect(self.screen, what_color(0), self.small_size_button)
    # self.screen.blit(self.small_size_text, (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 55))
    #
    # pygame.draw.rect(self.screen, what_color(1), self.original_size_button)
    # self.screen.blit(self.original_size_text, (SCREEN_WIDTH / 2 - 80, SCREEN_HEIGHT / 2 + 115))
    #
    # pygame.draw.rect(self.screen, what_color(2), self.big_size_button)
    # self.screen.blit(self.big_size_text, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT / 2 + 175))
