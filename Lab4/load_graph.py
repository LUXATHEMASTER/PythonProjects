from vertex import Vertex
#Create a vrtex dictionary
vertex_dict={}

def load_graph(name):
    in_file = open(name, "r")    #Load information from a file
    for line in in_file:
        s=line.split(";")        #Split the line
        cord=s[2].split(",")
        vertex=Vertex(s[0],int(cord[0]),int(cord[1]),list=[],list2=[])       #Create a vertex object
        vertex_dict[s[0]]=vertex


    in_file.close()                     #Close file

    file = open(name, "r")              #Open file

    for line in file:
        list=[]
        list2=[]     #Create an empty list
        s=line.strip(" ")
        s = line.split(";")
        s[1] = s[1].split(",")


        for item in  s[1]:
            item=item.strip(" ")
            list.append(vertex_dict[item])
            list2.append(vertex_dict[item].name)

        vertex_dict[s[0]].list2=list2    #Add list to object
        vertex_dict[s[0]].list = list    #Add list to object


    file.close()                            #Close file
    return vertex_dict                      #Return Dictionary



