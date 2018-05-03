#Solarsystem
#Louis Murerwa
# F0034jj
#02/08/2018

from system import System
from body import Body
from cs1lib import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 1000000       # real seconds per simulation second
PIXELS_PER_METER = 8/1e10 # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1/FRAMERATE # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)



#Bodies
mars = Body(0.642e24,0,227.9e9,24.1e3,0,6,.3,1,1)                    # blue mars
earth = Body(5.9736e24, 0, 149.6e9,29.8e3,0, 14, 0, 0, 1)            # blue earth
mercury=Body(0.330e22 ,0,57.9e9,47.4e3,0,6,0,1,0)                    # green mercury
venus=Body(4.87e24,0,108.2e9,35e3,0,8,1,.2,.6)                       # pink venus
sun=Body(1.989e30,0,0,0,0,24,1,0,0)                                  # red sun

solar_system = System([earth,sun,mercury,venus,mars])# list of bodies

start_graphics(main, 2400, framerate=FRAMERATE)