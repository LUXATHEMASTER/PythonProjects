from vertex import *


def game():
    vertex_dict={}
    for key in vertex_dict:
        start_vertex = vertex_dict["START"]
        value = input("letter")

        while start_vertex != " ":
            if value == "a":
                start_vertex = vertex_dict['adjacent_vertices[1]']
                print(start_vertex.data)


            elif value == "b":
                start_vertex = vertex_dict['adjacent_vertices[2]']
                print(start_vertex.data)

