
import sys
import pygame
import random


class Flappy:

    def __init__(self, picture="bird.png"):

        self.bird_picture = pygame.image.load(picture)
        self.bird_rect = self.bird_picture.get_rect().move(300, 230)
        self.natural_movement = [0, 4]
        self.space_movement = [0, -9]
        self.movement_delay = 1000
        self.movement_last = 0
        self.space_pressed = 0

    def move_it(self, time):

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.space_pressed = 1

        if self.movement_last < (time + self.movement_delay):

            self.movement_last = time + self.movement_delay

            if self.space_pressed == 1:
                self.space_pressed = 0
                if not self.bird_rect[1] < 0:
                    self.bird_rect = self.bird_rect.move(self.space_movement)

            else:
                if not self.bird_rect[1] > 436:
                    self.bird_rect = self.bird_rect.move(self.natural_movement)

    def check_ifcollide(self, pipe_rect):

        if pygame.Rect.colliderect(self.bird_rect, pipe_rect):
            sys.exit()


class Pipe:

    def __init__(self, pipe_low="pipe_low.png", pipe_high="pipe_high.png"):

        self.deviation = random.randint(0, 232)
        self.pipe_low = pygame.image.load(pipe_low)
        self.pipe_low_rect = self.pipe_low.get_rect()
        self.pipe_high = pygame.image.load(pipe_high)
        self.pipe_high_rect = self.pipe_high.get_rect()
        self.movement = [-1, 0]
        self.middle_space = 100
        self.pipe_high_rect = self.pipe_high_rect.move(950, -self.deviation)
        self.pipe_low_rect = \
            self.pipe_low_rect.move(950, 297 - self.deviation + 150)

    def move_pipe(self):
        self.pipe_high_rect = self.pipe_high_rect.move(self.movement)
        self.pipe_low_rect = self.pipe_low_rect.move(self.movement)


class Backround:

    def __init__(self, backround="backround.png"):

        self.picture = pygame.image.load(backround)
        self.rect = self.picture.get_rect()
        self.movement = [-1, 0]

    def move_backround(self):
        self.rect = self.rect.move(self.movement)

    def get_inline(self):
        self.rect = self.rect.move(900, 0)


def main():

    pygame.init()
    screen_size = width, height = 900, 500
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_icon(pygame.image.load("bird.png"))
    pygame.display.set_icon(pygame.image.load("bird.png"))
    running = True
    flappy_bird = Flappy()
    backround_list = [Backround()]
    pipe_list = [Pipe()]

    while running:
        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if backround_list[0].rect[0] == -900:
            backround_list.pop(0)

        if backround_list[0].rect[0] == 0:
            backround_list.append(Backround())
            backround_list[-1].get_inline()

        if pipe_list[0].pipe_high_rect[0] < -90:
            pipe_list.pop(0)

        if pipe_list[-1].pipe_high_rect[0] < 700:
            pipe_list.append(Pipe())

        flappy_bird.move_it(time)

        for i in pipe_list:
            flappy_bird.check_ifcollide(i.pipe_high_rect)
            flappy_bird.check_ifcollide(i.pipe_low_rect)

        for i in backround_list:
            i.move_backround()
            screen.blit(i.picture, i.rect)

        for i in pipe_list:
            i.move_pipe()
            screen.blit(i.pipe_low, i.pipe_low_rect)
            screen.blit(i.pipe_high, i.pipe_high_rect)

        screen.blit(flappy_bird.bird_picture, flappy_bird.bird_rect)

        pygame.time.Clock().tick(50)
        pygame.display.flip()


if __name__ == "__main__":
    main()
