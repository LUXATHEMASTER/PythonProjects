class Vertex:
    def __init__(self,list,text):
        self.list=list
        self.data=text


def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)
            v=Vertex(adjacent_vertices,text)
            vertex_dict[vertex_name]=v.list, v.data #Create a dictionary
    file.close()

    return vertex_dict

story_dict = load_story("stories.txt")


def game():

    global story_dict


    start_vertex=story_dict['START'] #Print initial story
    print(story_dict['START'][1])

    while start_vertex[0]!= []:      #loop over vertex
        answer = input("Can you put your input")        #Provide input
        print("Your input is:", answer)
        vertex_list=start_vertex[0]



        if answer == "a":
            start_vertex=story_dict[vertex_list[0]]
            print (start_vertex[1])


        elif answer == "b":
            start_vertex = story_dict[vertex_list[1]]

            print(start_vertex[1])

        elif answer == "c":
            start_vertex = story_dict[vertex_list[2]]

            print(start_vertex[1])

game() #Start game






