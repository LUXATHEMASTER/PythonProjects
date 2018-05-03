#Body
#Louis Murerwa
# F0034jj
#02/08/2018
from cs1lib import *
from system import *
class Body:
    #Initialize the instance variables
    def __init__(self, mass, x, y, v_x, v_y,pixel_radius,r=0, g=1, b=1):
        self.x=x
        self.y=y
        self.v_x=v_x
        self.v_y=v_y
        self.mass=mass
        self.pixel_radius=pixel_radius
        self.r=r
        self.g=g
        self.b=b


    #This method draws the the objects
    def draw(self,cx,cy,pixels_per_meter):

        self.cx = pixels_per_meter * self.x
        self.cy = pixels_per_meter * self.y
        self.cx= self.cx + cx
        self.cy = self.cy + cy

        set_fill_color(self.r,self.g,self.b)                #set body color
        draw_circle(self.cx,self.cy,self.pixel_radius)      #draw body

    #This method updates the positions of the objects
    def update_position(self, timestep):

        self.x = self.x + self.v_x * timestep               #update planet position
        self.y = self.y + self.v_y * timestep

    #This method updates the velocity of the object
    def update_velocity(self, a_x, a_y, timestep):          #update planet velocity

        self.v_x=self.v_x+a_x*timestep
        self.v_y=self.v_y+a_y*timestep



