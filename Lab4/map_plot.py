
from bfs import *
from vertex import *
global pressed_vertex

vertex_dict = load_graph("Extra_credit_map.txt")

def draw_map():         #Draw and Load map
    dmap = load_image("dartmouth_map.png")
    draw_image(dmap,0,0 )




def edge(start,current):        #Draw graph and edges between vertex
    if  vertex_dict[current].mouse:
        draw_grap()
        g=bfs(start,current)
        set_stroke_color(0,0,0)
        #draw name of vertexes
        draw_text(vertex_dict[start].name,vertex_dict[start].x+10,vertex_dict[start].y)
        draw_text(vertex_dict[current].name, vertex_dict[current].x+10, vertex_dict[current].y)
        vertex_dict[start].draw(0,0,1)

        for vertex in g:
            vertex.draw(1,0,0)
            vertex.draw_edge1(vertex.backpointer,1, .1, 1)

#Draw graph
def draw_grap():

    for vertex in vertex_dict:
        vertex_dict[vertex].draw(0, 0, 0)
        vertex_dict[vertex].draw_edges(.1, .1, .1)

#Respond mouse presses
def pressed(mx,my):
    x=mx
    y=my


#Respond to mouse movement
def moved(mx,my):
    global current,draw,presed
    x=mx
    y=my

    for vertex in vertex_dict:
        if presed and vertex_dict[vertex].in_range(x,y) :
            current = vertex

            vertex_dict[current].mouse=True

            edge(start, current)

#Respond to mouse realease
def release(mx,my):
    global start,presed
    x = mx
    y = my
    for vertex in vertex_dict:
        if vertex_dict[vertex].in_range(x,y):
            start=vertex
            presed=True
            return presed
#Main function called by start graphics
def main():
    global map
    if map:
        draw_map()
        draw_grap()
    map=False
    set_fill_color(1,0,1)

presed=False

start_graphics(main,height=811,width=1012, mouse_press= pressed ,mouse_move=moved,mouse_release=release)