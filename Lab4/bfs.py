from collections import deque
from cs1lib import *
from load_graph import *
vertex_dict = load_graph("dartmouth_graph.txt")

def bfs(start,current):#Start searching for a node
    q = deque()     #Create queue
    list = []
    set_stroke_width(4)#Change stroke width
    for vertex in vertex_dict:
        vertex_dict[vertex].backpointer=None        #Assign Backpointers
        vertex_dict[vertex].visited=False

    q.append(start)
    while (len(q))>0 :
        now=q.popleft()     #Deque items from queue
        for vertex in vertex_dict[now].list :

            if vertex.visited==False and vertex.backpointer==None:
                vertex.visited = True
                vertex.backpointer=vertex_dict[now]
                if vertex.name==current:
                    vertex_dict[current].backpointer=vertex_dict[now]
                    break
                q.append(vertex.name)
            vertex_dict[now].visited=True

    while current!=start : #Backchain from current point
        if current==None:
            vertex_dict[start].backpointer = vertex_dict[start]

        else:
            list.append(vertex_dict[current])
            current=vertex_dict[current].backpointer.name


    return list






