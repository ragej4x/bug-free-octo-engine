import player, pygame as pg

class Animation_class:
    def __init__(self) -> None:
        #LOAD IMG FILE
        self.idle_left = pg.image.load('data/female-idle.png')
        self.idle_right = pg.transform.flip(self.idle_left, True, False)        
        self.idle_back = pg.image.load('data/female-idle-back.png')
        self.idle_front = pg.image.load('data/female-idle-front.png')

        self.run_left = pg.image.load('data/female-run.png')
        self.run_right = pg.transform.flip(self.run_left, True, False)
        self.run_back = pg.image.load('data/female-run-back.png')
        self.run_front = pg.image.load('data/female-run-front.png')


        self.anim_surface = pg.Surface((24, 24))
        self.idle_left_frame_counter = 0
        self.idle_right_frame_counter = 0
        self.idle_back_frame_counter = 0
        self.idle_front_frame_counter = 0

        self.run_left_frame_counter = 0
        self.run_right_frame_counter = 0
        self.run_back_frame_counter = 0
        self.run_front_frame_counter = 0

        self.idle_frame = []
        self.run_frame = []

        self.frame_speed = 0.15

        #CALCULATE HOW MANY FRAME IN SPRITESHEET
        for i in range(5):
            i = -24 * i
            self.idle_frame.append(i)
            
        for i in range(7):
            i = -24 * i
            self.run_frame.append(i)


    def update_idle_left(self, x, y, display):
        self.anim_surface.blit(self.idle_left,(self.idle_frame[int(self.idle_left_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.idle_left_frame_counter += self.frame_speed
        if self.idle_left_frame_counter > 4:
            self.idle_left_frame_counter = 0

    def update_idle_right(self, x, y, display):
        self.anim_surface.blit(self.idle_right,(self.idle_frame[int(self.idle_right_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))
        self.idle_right_frame_counter += self.frame_speed
        if self.idle_right_frame_counter > 4:
            self.idle_right_frame_counter = 0


    def update_idle_back(self, x, y, display):
        self.anim_surface.blit(self.idle_back,(self.idle_frame[int(self.idle_back_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.idle_back_frame_counter += self.frame_speed
        if self.idle_back_frame_counter > 4:
            self.idle_back_frame_counter = 0


    def update_idle_front(self, x, y, display):
        self.anim_surface.blit(self.idle_front,(self.idle_frame[int(self.idle_front_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.idle_front_frame_counter += self.frame_speed
        if self.idle_front_frame_counter > 4:
            self.idle_front_frame_counter = 0

#RUN

    def update_run_left(self, x, y, display):
        self.anim_surface.blit(self.run_left,(self.run_frame[int(self.run_left_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.run_left_frame_counter += self.frame_speed
        if self.run_left_frame_counter > 6:
            self.run_left_frame_counter = 0

    def update_run_right(self, x, y, display):
        self.anim_surface.blit(self.run_right,(self.run_frame[int(self.run_right_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.run_right_frame_counter += self.frame_speed
        if self.run_right_frame_counter > 6:
            self.run_right_frame_counter = 0

    def update_run_back(self, x, y, display):
        self.anim_surface.blit(self.run_back,(self.run_frame[int(self.run_back_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.run_back_frame_counter += self.frame_speed
        if self.run_back_frame_counter > 6:
            self.run_back_frame_counter = 0

    def update_run_front(self, x, y, display):
        self.anim_surface.blit(self.run_front,(self.run_frame[int(self.run_front_frame_counter)], 0))
        display.blit(self.anim_surface,(x,y))

        self.run_front_frame_counter += self.frame_speed
        if self.run_front_frame_counter > 6:
            self.run_front_frame_counter = 0