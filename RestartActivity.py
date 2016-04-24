#coding=utf-8

from activity import *

class RestartActivity(Activity):
    def __init__(self, screen, background_fn):
        Activity.__init__(self, screen, background_fn)
        self.game_restart_btn = load_image(constants.game_over_bg_fn)
        self.wel_font = load_font(constants.wel_font_fn, constants.font_size)
        self.game_restart = self.wel_font.render("Restart now", True, (0, 0, 0))
        self.game_quit = self.wel_font.render("Quit", True, (0, 0, 0))
        self.small_font = load_font(r"wel_font.ttf", 28)
        self.author = self.small_font.render("Author:Xie Jun Dong", True, (0, 0, 0))

    def setup(self):
        self.screen.blit(self.game_restart, (78, 58))
        self.screen.blit(self.game_quit, (600, 240))
        self.screen.blit(self.author, (640, 400))

    def handle_events(self):
        for event in self.get_event():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.game_quit.get_rect(x=600, y=240).collidepoint(pos):
                    pygame.quit()
                    exit()
                elif self.game_restart.get_rect(x=78, y=58).collidepoint(pos):
                    pygame.event.post(pygame.event.Event(constants.WELCOME_SCREEN_EVENT))
                    self.quit = True
                    break
