import pygame as pg
import random as rd

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND = (112, 112, 112)

SNAKE_SPEED = 30
SNAKE_COLOR = (0, 128, 0)

FRUIT_COLOR = (255, 0, 0)
FRUIT_X = 300
FRUIT_Y = 400

GAME_RUNNING = True

snake_position_x = SCREEN_WIDTH / 2
snake_position_y = SCREEN_HEIGHT / 2
snake_speed_x = 0
snake_speed_y = 0

screen = pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
clock = pg.time.Clock()

def snakeControl(event):
    global snake_speed_x
    global snake_speed_y

    if event.type == pg.KEYDOWN:

        if event.key == pg.K_UP:
            snake_speed_x = 0
            snake_speed_y = -2

        if event.key == pg.K_DOWN:
            snake_speed_x = 0
            snake_speed_y = 2

        if event.key == pg.K_LEFT:
            snake_speed_x = -2
            snake_speed_y = 0

        if event.key == pg.K_RIGHT:
            snake_speed_x = 2
            snake_speed_y = 0

def quitGame(event):
    global GAME_RUNNING
    if event.type == pg.QUIT:
        GAME_RUNNING = False

def main():
    global snake_position_x
    global snake_position_y
    global snake_speed_x
    global snake_speed_y
    while GAME_RUNNING:
        screen.fill(SCREEN_BACKGROUND) 
        pg.draw.rect(screen, SNAKE_COLOR, [200, 150, 10, 10])
        snake_position_x += snake_speed_x
        snake_position_y += snake_speed_y
        pg.display.flip()

        for event in pg.event.get():
            snakeControl(event)
            quitGame(event)

main()