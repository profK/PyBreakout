# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'


import pgzrun
import pymunk
from Circle import Circle
from Rectangle import Rectangle
from Paddle import Paddle


WIDTH = 800
HEIGHT = 600
BLOCKS_IN_ROW = 8
NUM_ROWS = 6
SIDE_PADDING = 50
TOP_PADDING = 50
BLOCK_PADDING = 5



def update():
    if keyboard.left :
        paddle.move(-5,0)
    if keyboard.right :
        paddle.move(5,0)
    space.step(1 / 50.0)


def draw():
    screen.fill((0, 0, 0))
    for actor in actorList:
        actor.draw(screen)
    clock.tick(50)



def InitGame() -> list :
    #calculate block sizes and positioning
    actorList: list = list()
    block_horizontal_size : int = \
        ((WIDTH-(2*SIDE_PADDING))/(BLOCKS_IN_ROW))-BLOCK_PADDING
    block_vertical_size = \
        (((HEIGHT/2)-TOP_PADDING)/NUM_ROWS)- BLOCK_PADDING
    block_plus_pad_width: int = block_horizontal_size+BLOCK_PADDING
    block_plus_pad_height: int = block_vertical_size + BLOCK_PADDING
    for y in range(0,NUM_ROWS) :
        for x in range (0,BLOCKS_IN_ROW) :
            xcenter: int = SIDE_PADDING+(x*block_plus_pad_width)+(block_plus_pad_width/2)
            ycenter: int = TOP_PADDING+(y*block_plus_pad_height)+(block_plus_pad_height/2)
            block: Rectangle = Rectangle(space,(xcenter,ycenter),(block_horizontal_size,block_vertical_size), True)
            actorList.append(block)
    # add paddle
    return actorList


# Press the green button in the gutter to run the script.

space = pymunk.Space()  # 2
actorList: list = InitGame()
paddle:Paddle = Paddle(space,(WIDTH/2,HEIGHT-15),(80,20))
actorList.append(paddle)
leftDown: bool = False
rightDown: bool = False
#No gravity for this game
#space.gravity = (0.0, 900.0)

pgzrun.go()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
