from settings import *
from tetrice import tetris
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('TETRICE') 
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetrice = tetris(self)

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0  
        self.fast_user_event = pg.USEREVENT + 1  
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        self.clock.tick(FPS)
        self.tetrice.update()

    def draw(self):
        self.screen.fill(color = FIELD_COLOR)
        self.tetrice.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetrice.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        while True:
            game_active = True
            self.check_events()
            self.update()
            self.draw()
            


if __name__ == '__main__':
    app = App()
    app.run()                         
