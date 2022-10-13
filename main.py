from distutils.spawn import spawn
import pygame as pg
import random as rd

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND = (112, 112, 112)

DEFAULT_SIZE = 10

SNAKE_SPEED = 30
SNAKE_COLOR = (0, 128, 0)

FRUIT_COLOR = (255, 0, 0)
fruit_position_x = 0
fruit_position_y = 0
fruit_spawned = False

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
            snake_speed_y = -10

        if event.key == pg.K_DOWN:
            snake_speed_x = 0
            snake_speed_y = 10

        if event.key == pg.K_LEFT:
            snake_speed_x = -10
            snake_speed_y = 0

        if event.key == pg.K_RIGHT:
            snake_speed_x = 10
            snake_speed_y = 0

def quitGame(event):
    global GAME_RUNNING
    if event.type == pg.QUIT:
        GAME_RUNNING = False

def boundaryHitted():
    global GAME_RUNNING
    if (snake_position_x > SCREEN_WIDTH or snake_position_x < 0) or (snake_position_y > SCREEN_HEIGHT or snake_position_y < 0):
        GAME_RUNNING = False

def spawnFruit():
    global fruit_position_x
    global fruit_position_y
    global fruit_spawned
    if not fruit_spawned:
        fruit_position_x = rd.randrange(0, 800, 10)
        fruit_position_y = rd.randrange(0, 600, 10)
    pg.draw.rect(screen, FRUIT_COLOR, [fruit_position_x, fruit_position_y, DEFAULT_SIZE, DEFAULT_SIZE])
    fruit_spawned = True

def fruitEated(snake_x_position, snake_y_position):
    spawnFruit()
    global fruit_position_x
    global fruit_position_y
    global fruit_spawned
    if((fruit_position_x == snake_position_x) and (fruit_position_y == snake_position_y)):
        fruit_spawned = False


def main():
    global snake_position_x
    global snake_position_y
    global snake_speed_x
    global snake_speed_y
    
    while GAME_RUNNING:
        screen.fill(SCREEN_BACKGROUND) 
        snake_position_x += snake_speed_x
        snake_position_y += snake_speed_y
        pg.draw.rect(screen, SNAKE_COLOR, [snake_position_x, snake_position_y, DEFAULT_SIZE, DEFAULT_SIZE])
        fruitEated(snake_position_x, snake_position_y)
        pg.display.update()
        clock.tick(SNAKE_SPEED)

        boundaryHitted()

        for event in pg.event.get():
            snakeControl(event)
            quitGame(event)

main()