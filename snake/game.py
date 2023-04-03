import pygame
from pygame.locals import *
from snake import Snake
import time
from apple import Apple


SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((800, 800))
        self.surface.fill((BACKGROUND_COLOR))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/1_snake_game_resources_{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #snake colliding with apple
        if self.collision(self.snake.x[0], self.snake.y[0],
                          self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        #snake colliding with itself
        for i in range(1, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0],
                              self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game over"

        # snake going out of edge
        if self.snake.x[0] not in range(0, 800) or self.snake.y[0] not in range(0, 800):
            self.play_sound("crash")
            raise "Game over"

       

    def collision(self, x1, y1, x2, y2):
        """
        snazime se zjistit, jestli had a jablko do sebe naraztili.
        vzdycky potrebujeme pridat parametry x1, y1 a x2, y2 : jedno had
        a druhe je jablko
        """
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (600, 10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again, press Enter. To exit, press Escape.", True, (255, 255, 255))
        self.surface.blit(line2, (100, 350))
        # flip refreshing ui
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)

    def difficulty(self):
        if self.snake.length < 10:
            time.sleep(0.2)
        elif self.snake.length < 15:
            time.sleep(0.15)
        else:
            time.sleep(0.1)


    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            self.difficulty()


