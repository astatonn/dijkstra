from collections import defaultdict, deque
import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import *
import random
from tkinter import messagebox
import time

class Graph(object): 
    def __init__(self): 
        self.nodes = [] 
        self.edges = defaultdict(list) 
        self.distances = {} 


    def add_node(self, value):
        self.nodes.append(value)


    def add_edge(self, from_node, to_node, distance): 
        self.edges[from_node].append(to_node) 
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial): 
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes: 
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination): 
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)


    return visited[destination], list(full_path)

class gui_djikstra(tk.Frame): # GUI 
    def __init__(self, root, graph):
        tk.Frame.__init__(self,root)
        self.root = root
        self.initialize_user_interface(graph)
    
    def initialize_user_interface(self,graph):
        self.root.geometry('600x600')
        self.root.title("Djikstra")
        self.root.resizable(False, False)
        self.x=[]
        self.y=[]
        i=0

        for node in graph.nodes: 
            self.x.append(random.sample (range(550),1))
            self.y.append(random.sample (range(400),1))
            tk.Label(self.root,text=node, background='white', foreground='black', borderwidth = 2, relief="solid", width=3, height=2).place(x=self.x[i], y=self.y[i])
            i+=1
        colors = [ 'misty rose', 'dark slate gray', 'dim gray', 'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',    'indian red', 'saddle brown', 'sandy brown']
        # DESENHO DE LINHAS
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)

        nodes = frozenset(graph.nodes)

        for node in nodes:
            for edge in graph.edges[node]: # CRIA AS ARESTAS NO ALGORITMO
                cor=random.choice(colors)
                self.canvas.create_line(self.x[ord(node) - 65], self.y[ord(node) - 65],self.x[ord(edge) - 65],self.y[ord(edge) - 65], arrow=tk.LAST, width=3, fill = cor)
                colors.remove(cor)

        self.canvas.pack(fill=BOTH, expand=1)
        # FIM DO DESENHO DE LINHAS
        
        initial=Label(self.root, text="ORIGEM")
        initial.pack()
        initial_entry = Entry(self.root, width=2)
        initial_entry.pack()

        final=Label(self.root, text="DESTINO")
        final.pack()
        final_entry = Entry(self.root, width=2)
        final_entry.pack()
        
        b = Button(self.root, text="MENOR CAMINHO", command=lambda:menorcaminho(self,graph,initial_entry.get().upper(),final_entry.get().upper(),self.root))
        b.pack()


        def menorcaminho (self, graph,initial,final,root):
            try:
                
                menor_caminho=shortest_path(graph, initial, final)
                for node in menor_caminho[1]:
                    tk.Label(root,text=node, background='red', foreground='white', borderwidth = 2, relief="solid", width=3, height=2).place(x=self.x[ord(node) - 65], y=self.y[ord(node) - 65])
                    tk.Label(root,text=initial, background='green', foreground='white', borderwidth = 2, relief="solid", width=3, height=2).place(x=self.x[ord(initial) - 65], y=self.y[ord(initial) - 65])
                    tk.Label(root,text=final, background='blue', foreground='white', borderwidth = 2, relief="solid", width=3, height=2).place(x=self.x[ord(final) - 65], y=self.y[ord(final) - 65])
                

                messagebox.showinfo("DJIKSTRA", "O MENOR CAMINHO É: {} \nPESO TOTAL: {}".format(menor_caminho[1], menor_caminho[0]))

                for node in menor_caminho[1]:
                    tk.Label(root,text=node, background='white', foreground='black', borderwidth = 2, relief="solid", width=3, height=2).place(x=self.x[ord(node) - 65], y=self.y[ord(node) - 65])

            
            except:
                messagebox.showinfo("DJIKSTRA", "NÃO EXISTEM CAMINHOS POSSÍVEIS")


if __name__ == '__main__':
    graph = Graph()

    for node in ['A', 'B', 'C', 'D', 'E']:
        graph.add_node(node) # CRIA UM CONJUNTO COM OS NÓS POSSÍVEIS

    graph.add_edge('A','B',10)
    graph.add_edge('A','C', 3)
    graph.add_edge('B','C', 1)
    graph.add_edge('B','D', 2)
    graph.add_edge('C','B', 4)
    graph.add_edge('C','D', 8)
    graph.add_edge('C','E', 2)
    graph.add_edge('D','E', 7)
    

    

    root = tk.Tk()
    run=gui_djikstra(root, graph)

    root.mainloop()