from src.game_screens.screen import Screen
from src.misc.game_enums import Game_mode, Difficulty
from pygame.locals import QUIT, KEYUP, MOUSEBUTTONUP
from src.ui.button import Button


class Game_Mode_Screen(Screen):
    def __init__(self, pygame, res, surface, game_manager):
        Screen.__init__(self, pygame, res, surface)
        self.game_manager = game_manager
        self.font = res.heading_font
        
        self.buttons['Easy'] =      Button(pygame, res, surface, [20, 290, 150, 50], "Easy")
        self.buttons['Medium'] =    Button(pygame, res, surface, [170, 290, 150, 50], "Medium")
        self.buttons['Hard'] =      Button(pygame, res, surface, [340, 290, 150, 50], "Hard")

        self.buttons['Back'] =      Button(pygame, res, surface, [20, 540, 300, 50], "Back")

    def update(self, events):
        textsurface = self.font.render('Select Difficulty:', True, self.res.WHITE)
        self.surface.blit(self.res.EBG, (0, 0))
        self.surface.blit(textsurface, (20, 220))

        for button in self.buttons:
            self.buttons[button].draw()

        mouseup_event = next(
            (x for x in events if x.type == MOUSEBUTTONUP), None)

        if mouseup_event is not None:
            if self.buttons['Easy'].check_click(mouseup_event.pos):
                self.game_manager.difficulty = Difficulty.EASY
                return Game_mode.GAME

            if self.buttons['Medium'].check_click(mouseup_event.pos):
                self.game_manager.difficulty = Difficulty.MEDIUM
                return Game_mode.GAME

            if self.buttons['Hard'].check_click(mouseup_event.pos):
                self.game_manager.difficulty = Difficulty.HARD
                return Game_mode.GAME

            if self.buttons['Back'].check_click(mouseup_event.pos):
                return Game_mode.MAIN_MENU

        self.pygame.display.flip()

        for event in events:
            if event.type == QUIT:
                return Game_mode.QUIT

        return Game_mode.GAME_MODE
