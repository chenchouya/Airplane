#coding=utf-8

from activity import *


class HelpActivity(Activity):
    def __init__(self, screen, background_fn):
        Activity.__init__(self, screen, background_fn)

        self.help_font = load_font(constants.wel_font_fn, 30)

        self.caption = self.help_font.render("Help", True, (0, 0, 0))
        self.help1 = self.help_font.render("Move your mouse to control the plane.", True, (0, 0, 0))
        self.help2 = self.help_font.render("Press Key_space to launch a bomb.", True, (0, 0, 0))
        self.help3 = self.help_font.render("Press v to stop.", True, (0, 0, 0))
        self.help_back = self.help_font.render("Back", True, (0, 0, 0))

    def setup(self):
        self.screen.blit(self.caption, (400, 40))
        self.screen.blit(self.help1, (100, 100))
        self.screen.blit(self.help2, (100, 160))
        self.screen.blit(self.help3, (100, 220))
        self.screen.blit(self.help_back, (800, 480))

    def handle_events(self):
        for event in self.get_event():
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.help_back.get_rect(x=800, y=480).collidepoint(pos):
                    pygame.event.post(pygame.event.Event(constants.WELCOME_SCREEN_EVENT))
                    self.quit = True
                    break