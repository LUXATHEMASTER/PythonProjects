# System
#Louis Murerwa
# F0034jj
#02/08/2018
from body import *
from math import *
class System:

    #This object initializes the values of the system
    def __init__(self, bodies):
        self.bodies=bodies


    #This method draws the objects in the system
    def draw(self, cx, cy, pixels_per_meter):
        index=0
        while index < len(self.bodies):
            self.bodies[index].draw(cx,cy,pixels_per_meter)
            index=index+1

    #This function updates the acceleration of the bodies
    def update(self, timestep):
        for n in range (len(self.bodies)):
            (a_x, a_y) = self.compute_acceleration(n)

            self.bodies[n].update_velocity(a_x, a_y, timestep)
            self.bodies[n].update_position(timestep)


    #compute accelaratin of body at index n
    def compute_acceleration(self, n):
        G=6.67384e-11
        a_x=0
        a_y=0
        for i in range (len(self.bodies)):


            if i != n:

                d_x=self.bodies[i].x-self.bodies[n].x
                d_y=self.bodies[i].y-self.bodies[n].y
                r=sqrt(d_x*d_x+d_y*d_y)                             #calclates distance between bodies
                a = ((G) * (self.bodies[i].mass)) / ((r) ** 2)      #calclates accelaration of body from other bodies

                a_x=((a*d_x)/r)+a_x                                 #calcates the x- accleration of a body

                a_y=((a*d_y)/r)+a_y                                 #calclates the y - accelaration of a body

            elif i==n :
                pass
        return (a_x,a_y)




