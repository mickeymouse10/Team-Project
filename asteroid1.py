import runWorld as rw
import drawWorld as dw
import pygame as pg
import math as m
from random import randint

################################################################

# Initialize world
name = "Asteroid- click to destroy the earth"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################

earthimage = dw.loadImage("earth.jpg")
moonimage = dw.loadImage("moon.jpg")
astimage = dw.loadImage("asteroid1.jpg")


# World state will be (xearth, yearth, xmoon, ymoon, xast, yast, vast,
# count, increment)
initState = {
    'xearth': 250,
    'yearth': 250,
    'xmoon': 250,
    'ymoon': 125,
    'xast': 0,
    'yast': 250,
    'vast': 0,
    'count': 0,
    'increment': 3,
    'earth': earthimage,
    'moon': moonimage,
    'ast': astimage
    }

class State():
    xearth = 250
    yearth = 250
    xmoon = 250
    ymoon = 125
    xast = 0
    yast = 250
    vast = 0
    count = 0
    increment = 3
    def setImage(self,img):
        self.earth = earthimage
        self.moon = moonimage
        self.ast = astimage
    def moonMove(self):
        self.count = self.count + self.increment
        self.xmoon = 250 + (125*m.cos((m.pi/2)+((self.count * m.pi)/180)))
        self.ymoon = 250 + (125*m.sin((m.pi/2)+((self.count * m.pi)/180)))
    def astMove(self):
        self.xast = self.xast + self.vast
    def __init__(self,img):
        self.setImage(earthimage)
        self.setImage(moonimage)
        self.setImage(astimage)
        
InitState = State(initState)
    
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(state.earth, (state.xearth, state.yearth))
    dw.draw(state.moon, (state.xmoon, state.ymoon))
    dw.draw(state.ast, (state.xast, state.yast))
# World state will be (xearth, yearth, xmoon, ymoon, xast, yast, vast,
# count, increment)v

################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    if ((state.xearth-15) <= state.xast and state.xast <= (state.xearth+15)):
        state.moonMove()
        state.xast = 0
        state.vast = 0
        state.increment = state.increment + 1
        return state
    else:
        state.moonMove()
        state.astMove()
        return state

################################################################

# state -> bool
def endState(state):
    if (state.increment == 6):
        return True
    elif ((state.xmoon-40) <= state.xast and state.xast <= (state.xmoon+40) and (state.ymoon-40) <= state.yast and state.yast <= (state.ymoon+40)):
        return True
    else:
        return False

################################################################
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
       if (state.vast == 0):
           state.vast = (randint(10,15))/5
    return state

################################################################

# World state will be (xearth, yearth, xmoon, ymoon, xast, yast, vast,
# count, increment)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(InitState, updateDisplay, updateState, handleEvent,
            endState, frameRate)

