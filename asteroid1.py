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

# state -> image (IO)

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(earthimage, (state[0], state[1]))
    dw.draw(moonimage, (state[2], state[3]))
    dw.draw(astimage, (state[4], state[5]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    if ((state[0]-15) <= state[4] and state[4] <= (state[0]+15)):
        return(state[0], state[1], 250 + (125*m.cos((m.pi/2)+((state[7] * m.pi)/180))), 250 + (125*m.sin((m.pi/2)+((state[7] * m.pi)/180))), 0, state[5], 0, (state[7] + state[8]), state[8] + 1)
    else:
        return(state[0], state[1], 250 + (125*m.cos((m.pi/2)+((state[7] * m.pi)/180))), 250 + (125*m.sin((m.pi/2)+((state[7] * m.pi)/180))), state[4] + state[6], state[5], state[6], (state[7] + state[8]), state[8])

################################################################

# state -> bool
def endState(state):
    if (state[8] == 6):
        return True
    elif ((state[2]-40) <= state[4] and state[4] <= (state[2]+40) and (state[3]-40) <= state[5] and state[5] <= (state[3]+40)):
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
       if (state[6] == 0):
           nstate6 = (randint(10,15))/5
           return((state[0], state[1], state[2], state[3], state[4], state[5], nstate6, state[7], state[8]))
       else:
           return(state)
    else:
        return(state)

################################################################

# World state will be (xearth, yearth, xmoon, ymoon, xast, yast, vast,
# count, increment)

initState = (250, 250, 250, 125, 0, 250, 0, 0, 3)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
