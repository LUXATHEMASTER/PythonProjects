from cs1lib import *
from cities_population import *                         #import most populous cities list
from time import sleep

drawn=[]
info=[]
i=0



def load_map():
    img = load_image("new_map.png")  # Load image
    draw_image(img, 0, 0)

def visualize(list,num):                                #function to draw cities on the world map

    global i

    if i <50:
        drawn.append(list[i])               #append list of drawn cities
        info.append(list[i].name)

        i+=1

    for index in range (len(drawn)): #Draw markings on the map to show cities
        set_fill_color(0, 0, 1)

        draw_rectangle(360+2*(drawn[index].longitude),180-2*(drawn[index].latitude),5,5)

    set_fill_color(1, 0, 0)
    set_stroke_color(1,1,1)
    set_font_bold()
    set_font_italic()
    draw_text(list[i].name, 360 + 2 * (list[i].longitude), 180 - 2 * (list[i].latitude))  # Draw name of city
    draw_rectangle(360 + 2 * (list[i].longitude), 180 - 2 * (list[i].latitude), 5, 5)

def main():
    # Draw image
    load_map()
    sleep(1)
    visualize(Cities,len(drawn))                                   #Call visualize to draw cities

start_graphics(main, width = 720, height = 360)