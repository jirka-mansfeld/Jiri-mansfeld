import pygame
from pygame.locals import *

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Snake:

    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        #direction se nam bude starat o smer pohybu hada
        self.direction = "down"

    def draw(self):
        """
        vykresleni hada
        """
        # fill() maze obrazovku, aby nezustali ostatni bloky na obrazovce

        #blit() vytvari blok hada na obrazovce
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
            #flip() aktualizuje display pri kliknutí na klavesnici


    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"


    def walk(self):
        #update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE

        self.draw()