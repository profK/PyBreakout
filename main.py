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
import random
import math

WIDTH = 800
HEIGHT = 600
BLOCKS_IN_ROW = 8
SIDE_PADDING = 50
BLOCK_PAD = 10
TOP_PADDING = 50
BLOCKS_IN_COLUMN = 6

global space
global paddle
global ball
global score
score: int = 0

collision_types = {
    "ball": 1,
    "brick": 2,
    "bottom": 3,
    "player": 4,
}

def MakeBlocks(space) -> list :
    block_list: list = list()
    block_width: int = \
        ((WIDTH-(SIDE_PADDING*2))/BLOCKS_IN_ROW) \
        -BLOCK_PAD
    block_height = (((HEIGHT/2)-TOP_PADDING)/BLOCKS_IN_COLUMN) \
        -BLOCK_PAD
    block_width_padded : int = block_width + BLOCK_PAD
    block_height_padded : int = block_height + BLOCK_PAD
    for y in range(0,BLOCKS_IN_COLUMN) :
        for x in range (0, BLOCKS_IN_ROW) :
            xcenter: int = (block_width_padded*x) + SIDE_PADDING +\
                           (block_width/2)
            ycenter : int = (block_height_padded*y)+ \
                TOP_PADDING+(block_height/2)
            block: Rectangle = Rectangle(space, \
                                         (xcenter,ycenter), \
                                         (block_width,block_height), \
                                          True)
            block.setCollisionType(collision_types["brick"])
            block_list.append(block)
    return block_list

def StartBall(ball:Circle) :
    angle: float = (random.random()*math.pi)-(math.pi/2)
    angleY:float = math.sin(angle)
    angleX:float = math.cos(angle)
    impulse: tuple = [angleX*500,angleY*500*-1]
    ball.circleBody.apply_impulse_at_local_point(impulse,[0,0])

def AddWalls(actorList: list) :
    topWall: Rectangle = Rectangle(space,(400,10),(800,20),True)
    bottomWall: Rectangle = Rectangle(space,(400,590),(800,20),True)
    leftSide: Rectangle = Rectangle(space,(10,300),(20,600),True)
    rightSide: Rectangle = Rectangle(space,(790,300),(20,600),True)
    bottomWall.setCollisionType(collision_types["bottom"])
    #actorList.append(topWall)
    #actorList.append(bottomWall)
    #actorList.append(leftSide)
    #actorList.append(rightSide)


def draw() :
    screen.fill((0,0,0))
    for actor in actorList :
        actor.draw(screen)
    screen.draw.text(f"{score}",center=(400,30),fontsize=60)
    clock.tick(50)

def update() :
    space.step(1/50)
    if keyboard.left :
        paddle.move(space,-15,0)
    if keyboard.right :
        paddle.move(space,15,0)

def handle_brick_collision(arbiter:pymunk.Arbiter, space:pymunk.Space, data) -> bool :
    brickShape = arbiter.shapes[1]
    for actor in actorList :
        if hasattr(actor,"rectShape") and (actor.rectShape == brickShape) :
            actorList.remove(actor)
            space.remove(brickShape)
            break;
    return True

def handle_brick_collision2(arbiter:pymunk.Arbiter, space:pymunk.Space, data) -> bool :
    global score
    brickShape = arbiter.shapes[1]
    actor = brickShape.rectangle
    actorList.remove(actor)
    space.remove(brickShape)
    score = score +10
    return True

def handle_bottom_collision(arbiter:pymunk.Arbiter, space:pymunk.Space, data) -> bool :
    ballShape = arbiter.shapes[0]
    actor = ballShape.circle
    space.remove(ballShape)
    actorList.remove(actor)
    return True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
space = pymunk.Space()
paddle = Paddle(space,(400,600-20),(70,20))
ball = Circle(space,(400,400),10)
ball.setCollisionType(collision_types["ball"])
collisionHandler = \
    space.add_collision_handler(collision_types["ball"],collision_types["brick"])
collisionHandler.begin = handle_brick_collision2
bottomCollisionHandler = \
    space.add_collision_handler(collision_types["ball"], collision_types["bottom"])
bottomCollisionHandler.begin = handle_bottom_collision
StartBall(ball)
actorList: list = MakeBlocks(space)
actorList.append(ball)
AddWalls(actorList)
actorList.append(paddle)
pgzrun.go()