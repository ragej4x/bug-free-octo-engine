import pygame as pg
import animation
import camera

class Player_class():
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
        self.speed = 3
        self.player_rect = pg.Rect((self.x, self.y, 24,24))
        
        self.left = True
        self.right = False
        self.down = False
        self.up = False

        #initialize animation
        self.Animation = animation.Animation_class()



    def update(self, display, cameraX, cameraY):
        
        #PLAYER RECT
        self.player_rect = pg.Rect((self.x - cameraX, self.y - cameraY, 24,24))
        pg.draw.rect(display, (200,0,0), self.player_rect )

        dx = 0
        dy = 0


        #movement
        playerMovementInp = pg.key.get_pressed()

        if playerMovementInp[pg.K_a]:
            dx -= self.speed

            self.left = True
            self.right = False
            self.down = False
            self.up = False

            if self.left == True and self.right == False and self.down == False and self.up == False:
                self.Animation.update_run_left(self.x - cameraX, self.y - cameraY, display)


        if playerMovementInp[pg.K_d]:
            dx += self.speed

            self.left = False
            self.right = True
            self.down = False
            self.up = False


            if self.right == True and self.left == False and self.down == False and self.up == False:
                self.Animation.update_run_right(self.x - cameraX, self.y - cameraY, display)


        if playerMovementInp[pg.K_s]:
            dy += self.speed

            self.left = False
            self.right = False
            self.down = True
            self.up = False

            if self.down == True and self.right == False and self.left == False and self.up == False:
                self.Animation.update_run_back(self.x - cameraX, self.y - cameraY, display)
                    
        if playerMovementInp[pg.K_w]:
            dy -= self.speed

            self.left = False
            self.right = False
            self.down = False
            self.up = True

            if self.up == True and self.right == False and self.down == False and self.left == False:
                self.Animation.update_run_front(self.x - cameraX, self.y - cameraY, display)


        #IDLE ANIMATION

        if self.left == True and playerMovementInp[pg.K_a] == False and playerMovementInp[pg.K_d] == False and playerMovementInp[pg.K_w] == False and playerMovementInp[pg.K_s] == False:
            self.Animation.update_idle_left(self.x - cameraX, self.y - cameraY, display)

        if self.right == True and playerMovementInp[pg.K_a] == False and playerMovementInp[pg.K_d] == False and playerMovementInp[pg.K_w] == False and playerMovementInp[pg.K_s] == False:
            self.Animation.update_idle_right(self.x - cameraX, self.y - cameraY, display)

        if self.down == True and playerMovementInp[pg.K_a] == False and playerMovementInp[pg.K_d] == False and playerMovementInp[pg.K_w] == False and playerMovementInp[pg.K_s] == False:
            self.Animation.update_idle_back(self.x - cameraX, self.y - cameraY, display)

        if self.up == True and playerMovementInp[pg.K_a] == False and playerMovementInp[pg.K_d] == False and playerMovementInp[pg.K_w] == False and playerMovementInp[pg.K_s] == False:
            self.Animation.update_idle_front(self.x - cameraX, self.y - cameraY, display)


        #FIX BUG IF BOTH KEY IS PRESSED THE SPEED IS DOUBLING
        if playerMovementInp[pg.K_a] and playerMovementInp[pg.K_w]:
            self.speed = self.speed / self.speed + 0.7

        elif playerMovementInp[pg.K_a] and playerMovementInp[pg.K_s]:
            self.speed = self.speed / self.speed + 0.7

        elif playerMovementInp[pg.K_w] and playerMovementInp[pg.K_d]:
            self.speed = self.speed / self.speed + 0.7

        elif playerMovementInp[pg.K_d] and playerMovementInp[pg.K_s]:
            self.speed = self.speed / self.speed + 0.7

        else:
            self.speed = 3

        #print(self.Animation.run_frame_counter)

        #move
        
        self.x += dx
        self.y += dy