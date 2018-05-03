from cs1lib import *

class Vertex:
    rad=10
#Initializes object values
    def __init__(self,name,x,y,list,list2,backpointer=None,mouse=False,visited=False):#Create a vertex class
        self.name=name
        self.x=x
        self.y=y
        self.list=list
        self.list2=list2
        self.mouse=mouse
        self.backpointer=backpointer
        self.visited=visited

#Returns details of objects
    def __str__(self):

       return(self.name+"; Location :"+str(self.x) +","+str(self.y) +"; Adjacent Vertices :"+str(self.list2))

#Draws vertexes
    def draw(self,r,g,b):
        global rad
        set_fill_color(r,g,b)
        draw_circle(self.x,self.y,5)

#Draws edges between vertexes
    def draw_edges(self,r,g,b):
         set_stroke_color(r,g,b)
         for edge in self.list:
             set_stroke_width(4)
             draw_line(self.x,self.y,edge.x,edge.y)

##Draws edges between given vertexes
    def draw_edge1(self, vertex, r, g, b):

        set_stroke_color(r, g, b)
        if vertex!=None:
            draw_line(vertex.x, vertex.y, self.x, self.y)

#Checks if a point is in a vertex range
    def in_range(self,x,y):
        if x>self.x-10 and x<self.x+10 and y>self.y-10 and y<self.y+10:
            return True
        return False