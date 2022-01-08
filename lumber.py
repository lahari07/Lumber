"""
file: lumber.py
description: A program to draw trees at a selected point on
             the screen and later, draw the harvested logs
language: python3
author: Lahari Chepuri(lc8104 @ RIT.EDU)
author: Smita Subhadarshinee Mishra(sm8528 @ RIT.EDU)
"""

import turtle
import random
import yard

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
MAIN_DIVIDING_LINE_X = -1 * WINDOW_WIDTH
MAIN_DIVIDING_LINE_Y = -1 * WINDOW_HEIGHT / 2
HARVEST_DIVIDING_LINE_X = 0
HARVEST_DIVIDING_LINE_Y = -1 * WINDOW_HEIGHT / 2
LOG_OBJECT = yard.LumberYard()

def init():
    """
    Initializes the turtle and the screen size
    :pre: pos (0, 0), heading east, pen down
    :post: pos (0, 0), heading east, pen up
    :return: None
    """
    window = turtle.Screen()
    window.setworldcoordinates( -WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                                WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 )
    window.setup( width = 1.0, height = 1.0, startx = None, starty = None )
    window.bgcolor( "pink" )
    turtle.title( "Python Turtle Graphics" )
    turtle.penup()
    turtle.speed( 0 )
    turtle.setpos( 0, 0 )
    turtle.showturtle()

def defineScreen():
    """
    Divides the screen into planting section a
    harvesting section
    Later, divides the harvesting section into
    sort and harvest and unsorted harvest section
    :pre: pos (0, 0), heading east, pen down
    :post: pos (0, 0), heading east, pen up
    :return: None
    """
    turtle.forward( MAIN_DIVIDING_LINE_X )
    turtle.left( 90 )
    turtle.forward( MAIN_DIVIDING_LINE_Y )
    turtle.right( 90 )
    turtle.pendown()
    turtle.forward( WINDOW_WIDTH * 2 )
    turtle.penup()
    turtle.setpos( MAIN_DIVIDING_LINE_X + 20, MAIN_DIVIDING_LINE_Y - 20 )
    turtle.write( 'Harvest and Sort', font = "normal" )
    turtle.setpos( MAIN_DIVIDING_LINE_X, MAIN_DIVIDING_LINE_Y )
    turtle.forward( WINDOW_WIDTH * 2 )
    turtle.left( 180 )
    turtle.forward( 100 )
    turtle.left( 90 )
    turtle.forward( 20 )
    turtle.right( 90 )
    turtle.write( 'Harvest Unsorted', font = "normal" )
    turtle.setpos( 0, 0 )
    turtle.right( 180 )

def drawPineTree( side_length ):
    """
    Draws the top of the Pine Tree
    :pre: relative pos top of the trunk, heading east, pen down
    :post: relative pos top of the trunk, heading down, pen up
    :return: None
    """
    turtle.back( side_length / 2 )
    turtle.pendown()
    turtle.color( "green" )
    turtle.fillcolor( "green" )
    turtle.begin_fill()
    for i in range( 0, 3 ):
        turtle.forward( side_length )
        turtle.left( 120 )
    turtle.end_fill()
    turtle.penup()
    turtle.color( "black" )
    turtle.forward( side_length / 2 )
    turtle.right( 90 )

def drawMapleTree( radius ):
    """
    Draws the top of the Maple Tree
    :pre:  relative pos top of the trunk, heading east, pen down
    :post: relative pos top of the trunk, heading down, pen up
    :return: None
    """
    turtle.pendown()
    turtle.color( "green" )
    turtle.fillcolor( "green" )
    turtle.begin_fill()
    turtle.circle( radius )
    turtle.end_fill()
    turtle.penup()
    turtle.color( "black" )
    turtle.right( 90 )

def drawOakTree( length_of_side ):
    """
    Draws the top of the Oak Tree
    :pre: relative pos top of the trunk, heading east, pen down
    :post: relative pos top of the trunk, heading down, pen up
    :return: None
    """
    turtle.pendown()
    for i in range( 0, 12 ):
        drawPineTree( length_of_side )
        turtle.left( 120 )
    turtle.right( 90 )
    turtle.penup()
    turtle.color( "black" )

def plantTree( x, y ):
    """
    Draws the tree chosen at random
    :pre: pos (0,0), heading east, pen down
    :post: pos (x,y), heading east, pen up
    :return: None
    """
    turtle.setpos( 0, 0 )
    choose_tree_dict = { 1: drawPineTree, 2: drawMapleTree, 3: drawOakTree }
    tree_type = random.randint( 0, 3 )
    top_of_window = (100, WINDOW_HEIGHT / 2 + 70)
    top_limit = (x, top_of_window[ 1 ] - 50)
    dist_limit_trunkbottom = top_limit[ 1 ] - y
    if not (dist_limit_trunkbottom < 50):
        if dist_limit_trunkbottom > 50 and dist_limit_trunkbottom < 250:
            limit = int( dist_limit_trunkbottom )
            length_of_trunk = random.randint( 50, limit )
        if dist_limit_trunkbottom > 250:
            length_of_trunk = random.randint( 50, 250 )
        turtle.forward( x )
        turtle.left( 90 )
        turtle.forward( y )
        turtle.right( 90 )
        turtle.pendown()
        turtle.left( 90 )
        turtle.color( "brown" )
        turtle.forward( length_of_trunk )
        turtle.color( "black" )
        turtle.left( 90 )
        turtle.penup()
        turtle.right( 180 )
        length_of_tree = 30
        if tree_type == 0:
            turtle.penup()
            drawPineTree( length_of_tree )
            LOG_OBJECT.addLog( length_of_trunk )
        elif tree_type == 1:
            turtle.penup()
            drawOakTree( length_of_tree )
            LOG_OBJECT.addLog( length_of_trunk )
        else:
            turtle.penup()
            drawMapleTree( length_of_tree )
            LOG_OBJECT.addLog( length_of_trunk )
        turtle.penup()
        turtle.forward( length_of_trunk )
        turtle.left( 90 )

def drawLogs( logs ):
    """
    Draws all the Tree logs
    :pre: pos (0,0), heading east, pen down
    :post: relative pos at the center of the top of each log, heading east, pen up
    :return: None
    """
    turtle.color( "black" )
    turtle.fillcolor( "brown" )
    log_height = 10
    sum = 0
    for log in logs:
        turtle.pendown()
        turtle.begin_fill()
        log_length = log
        sum += log_length
        turtle.forward( log_length / 2 )
        turtle.left( 90 )
        turtle.forward( log_height )
        turtle.left( 90 )
        turtle.forward( log_length )
        turtle.left( 90 )
        turtle.forward( log_height )
        turtle.left( 90 )
        turtle.forward( log_length / 2 )
        turtle.end_fill()
        turtle.penup()
        turtle.left( 90 )
        turtle.forward( log_height )
        turtle.right( 90 )
    print( "Total length of all logs put together: ", sum )
    turtle.penup()
    turtle.color( "black" )

def harvestTrees( x, y ):
    """
    Based on the user click, the function decides
    if trees should be sorted and harvested or if the
    trees should be harvested without sorting
    :pre: pos (0,0), heading east, pen down
    :return: None
    """
    turtle.clearscreen()
    logs = LOG_OBJECT.allLogs()
    turtle.setpos( 0, 0 )
    if len( logs ) == 0:
        turtle.write( "0 trees have been planted", font = "normal" )
        turtle.penup()
        turtle.right( 90 )
        turtle.forward( 20 )
        turtle.left( 90 )
        turtle.pendown()
        turtle.write( "and therefore, it is not possible to harvest", font = "normal" )
    else:
        if x < HARVEST_DIVIDING_LINE_X:
            logs = sorted( logs, reverse = True )
            drawLogs( logs )
        elif x > HARVEST_DIVIDING_LINE_X:
            drawLogs( logs )
    turtle.exitonclick()

def plantOrHarvest( x, y ):
    """
    Based on the user click, the function decides
    if trees should be drawn(Planting Trees)
    or if logs should be drawn(Harvesting Trees)
    :return: None
    """
    if y > MAIN_DIVIDING_LINE_Y:
        plantTree( x, y )
    else:
        harvestTrees( x, y )

def main():
    init()
    defineScreen()
    turtle.onscreenclick( plantOrHarvest )
    turtle.mainloop()

if __name__ == "__main__":
    main()