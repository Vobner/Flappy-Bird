import sys, pygame, random

class Flappy:

    def __init__(self, picture = "bird.png"):
        
        self.bird_picture = pygame.image.load(picture)
        self.bird_rect = self.bird_picture.get_rect().move(300, 230)
        self.natural_movement = [0,-3]
        self.space_movement = [0,4]
        self.movement_delay = 20
        self.movement_last = 0
        self.space_pressed = 0

        def move(time):
            
            if pygame.key.get_pressed()[K_SPACE]:
                self.space_pressed = 1

            if self.movement_last < (time + self.movement_delay):

                self.movement_last = time + self.movement_delay

                if self.space_pressed == 1:
                    
                    self.bird_rect.move(self.space_movement)
                    self.space_pressed = 0

                else: 
                    
                    self.bird_rect.move(self.natural_movement)

        def check_ifcollide(pipe_rect):

            if pygame.colliderect(self.bird_rect, pipe_rect):
                sys.exit()


        def bird_blitz():
            return self.bird_picture, self.bird_rect        

class Pipe:

    def __init__(self, pipe_low = "pipe_low.png", pipe_high = "pipe_high.png"):

        self.deviation = random.randint(0, 182)
        self.pipe_low = pygame.image.load(pipe_low)
        self.pipe_low_rect = self.pipe_low.get_rect()
        self.pipe_high = pygame.image.load(pipe_high)
        self.pipe_high_rect = self.pipe_high.get_rect()
        self.movement = [-1,0]
        self.middle_space = 100
        if self.deviation >= 91:
           self.pipe_high_rect.move(810, -self.deviation)
           self.pipe_low_rect.move(810, 297 - self.deviation + 100)
        if self.deviation <= 91:
           self.pipe_high_rect.move(810, self.deviation)
           self.pipe_low_rect.move(810, 297 + self.deviation + 100)

    def move_pipe():
        self.pipe_high_rect.move(self.movement)
        self.pipe_low_rect.move(self.movement)

    def pipe_low_blitz():
        return self.pipe_low, self.pipe_low_rect

    def pipe_low_blitz():
        return self.pipe_high, self.pipe_high_rect    

class Backround:

    def __init__(self, backround = "backround.png"):
        
        self.backround = pygame.image.load(backround)
        self.backround_rect = self.backround.get_rect()
        self.movement = [-1,0]

    def move():
        
        self.backround_rect.move(self.movement)
        



        
    



    
    












