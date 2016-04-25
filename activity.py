from common import *

MAXFPS = 500
class Activity:
    def __init__(self, screen, background_fn):
        self.screen = screen
        self.background_fn = background_fn
        self.setup_background()
        self.clock = pygame.time.Clock()
        self.quit = False
        self.changed = False
        self.finished_ =False

    def setup_background(self):
        self.background, self.rect = load_image(self.background_fn)

    def get_event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                self.finished()
                pygame.quit()

                exit()

        return events

    def run(self):
        self.screen.blit(self.background, (0,0))
        self.setup()
        pygame.display.flip()
        while True:
            self.clock.tick(MAXFPS)
            if self.finished_:
                self.finished()
            else:
                pass
            self.handle_events()
            if self.quit:
                break
            if self.changed:
                self.screen.blit(self.background, (0,0))
                self.on_change()
                pygame.display.update()
            self.changed = False

    def setup(self):
        pass

    def handle_events(self):
        pass

    def on_change(self):
        pass

    def finished(self):
        pass

    def wrong(self):
        pass

    def good(self):
        pass

