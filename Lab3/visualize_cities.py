from cs1lib import *
from cities_population import *                         #import most populous cities list
from time import sleep

drawn_cities=[]                                         #list of drawn cities

i=0
def load_map():
    img = load_image("world.png")  # Load image
    draw_image(img, 0, 0)

def visualize(list):                                #function to draw cities on the world map

    global i
    if i< 50:
        drawn_cities.append(list[i])
        i+=1

    set_fill_color(0, 0, 1)
    for index in range (len(drawn_cities)):

       draw_rectangle(360+2*(drawn_cities[index].longitude),180-2*(drawn_cities[index].latitude),5,5)#Draw markings on the map to show cities

    set_fill_color(1, 0, 0)
    draw_rectangle(360 + 2 * (list[i].longitude), 180 - 2 * (list[i].latitude), 5, 5)#draw current city in a difrent color

def main():
    load_map()
    visualize(Cities)
    sleep(1)                #Call visualize to draw cities

start_graphics(main, width = 720, height = 360)

