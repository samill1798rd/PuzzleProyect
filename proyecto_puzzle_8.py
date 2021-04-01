# -*- coding: utf-8 -*-
"""Proyecto Puzzle-8 (Código Esqueleto)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hM8Vt7bO-gaqsdbnmz5c3JfmLGd-uo8W

# Proyecto Puzzle-8

**Código esqueleto para el proyecto *Puzzle-8*** del Prof. Carlos Ogando para la asignatura Introducción a la IA en ITLA

**Integrantes del equipo:**
 
*( Introduzca en este espacio los integrantes del equipo, su correo y su matrícula)*
 - Emilio Rosa 2019-7562 20197562@itla.edu.do
"""

"""
Código esqueleto para el proyecto Puzzle-8 del Prof. Carlos Ogando
para la asignatura Introducción a la IA en ITLA.
Python 3
"""

# Librerías

import queue as Q

import time

import math 

#import dist
import distutils

from collections import deque

# Clase que representa el Puzzle-n general
class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
    def __str__(self):
        return str(self.map)    


'''
class PuzzleState(object):

    """docstring para PuzzleState"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n*n != len(config) or n < 2:

            raise Exception("the length of config is not correct!")

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.dimension = n

        self.config = config

        self.children = []

        for i, item in enumerate(self.config):

            if item == 0:

                self.blank_row = i // self.n

                self.blank_col = i % self.n

                break

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):

                line.append(self.config[offset + j])

            print(line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):

        """Expandir el nodo"""

        # Añadir nodos hijos en orden UDLR (Up-Down-Left-Right)

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:

                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:

                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:

                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:

                self.children.append(right_child)

        return self.children
'''
def Nodes(node):
    nextPath = []
    nextPath.append(PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextPath.append(PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextPath.append(PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextPath.append(PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for procPath in nextPath:
        if(procPath.state!=None):
            nodes.append(procPath)
    return nodes

def move(state, direction):    
    newState = state[:]
        
    index = newState.index(0)

    if(index==0):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[0]
            newState[0]=newState[3]
            newState[3]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[0]
            newState[0]=newState[1]
            newState[1]=temp
        return newState      
    if(index==1):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[1]
            newState[1]=newState[4]
            newState[4]=temp
        if(direction==3):
            temp=newState[1]
            newState[1]=newState[0]
            newState[0]=temp
        if(direction==4):
            temp=newState[1]
            newState[1]=newState[2]
            newState[2]=temp
        return newState    
    if(index==2):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[2]
            newState[2]=newState[5]
            newState[5]=temp
        if(direction==3):
            temp=newState[2]
            newState[2]=newState[1]
            newState[1]=temp
        if(direction==4):
            return None
        return newState
    if(index==3):
        if(direction==1):
            temp=newState[3]
            newState[3]=newState[0]
            newState[0]=temp
        if(direction==2):
            temp=newState[3]
            newState[3]=newState[6]
            newState[6]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[3]
            newState[3]=newState[4]
            newState[4]=temp
        return newState
    if(index==4):
        if(direction==1):
            temp=newState[4]
            newState[4]=newState[1]
            newState[1]=temp
        if(direction==2):
            temp=newState[4]
            newState[4]=newState[7]
            newState[7]=temp
        if(direction==3):
            temp=newState[4]
            newState[4]=newState[3]
            newState[3]=temp
        if(direction==4):
            temp=newState[4]
            newState[4]=newState[5]
            newState[5]=temp
        return newState
    if(index==5):
        if(direction==1):
            temp=newState[5]
            newState[5]=newState[2]
            newState[2]=temp
        if(direction==2):
            temp=newState[5]
            newState[5]=newState[8]
            newState[8]=temp
        if(direction==3):
            temp=newState[5]
            newState[5]=newState[4]
            newState[4]=temp
        if(direction==4):
            return None
        return newState
    if(index==6):
        if(direction==1):
            temp=newState[6]
            newState[6]=newState[3]
            newState[3]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[6]
            newState[6]=newState[7]
            newState[7]=temp
        return newState
    if(index==7):
        if(direction==1):
            temp=newState[7]
            newState[7]=newState[4]
            newState[4]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[7]
            newState[7]=newState[6]
            newState[6]=temp
        if(direction==4):
            temp=newState[7]
            newState[7]=newState[8]
            newState[8]=temp
        return newState
    if(index==8):
        if(direction==1):
            temp=newState[8]
            newState[8]=newState[5]
            newState[5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[8]
            newState[8]=newState[7]
            newState[7]=temp
        if(direction==4):
            return None
        return newState


def writeOutput(data):
    """
    Función que escribe output.txt
    (Los estudiantes deben cambiar el método para que opere con los parametros necesarios).
    """
    with open("./output.txt", "w") as file:
        file.write(f"path_to_goal: {data['path_to_goal']}\n")
        file.write(f"cost_of_path: {data['cost_of_path']}\n")
        file.write(f"nodes_expanded: {data['nodes_expanded']}\n")
        file.write(f"search_depth: {data['search_depth']}\n")
        file.write(f"max_search_depth: {data['max_search_depth']}")
    print(data)

def bfs_search(initial_state):
    return 
'''
    global Max, Node, MaxSearch

    visited = set()
    Queue = deque([PuzzleState(initial_state, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        visited.add(node.map)
        if node.state == State:
            Node = node
            return Queue
        paths = subNodes(node)
        for path in paths:
            if path.map not in visited:
                Queue.append(path)
                visited.add(path.map)
                if path.depth > MaxSearch:
                    MaxSearch = MaxSearch + 1
        if len(Queue) > Max:
            QueueSize = len(Queue)
            Max = QueueSize
''' 

def dfs_search(initial_state):

    """DFS search"""

    ### SU CÓDIGO VA AQUÍ ###

class CustomQueue():
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)
        self.queue.sort( key=lambda x: x.key)
    
    def remove(self):
        return self.queue.pop(0)
    
    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0

def A_star_search(initial_state):
    """A * search"""
    output = templateOutput
    visited= set()
    Queue = CustomQueue()
    
    nstr = "".join(  initial_state.__str__() ).replace(',', '').replace(' ', '').replace('[', '').replace(']','')

    key = Heuristica(nstr)

    Queue.insert(PuzzleState(initial_state, None, None, 0, 0, key))
    visited.add(nstr)
    while Queue:
        track = Queue.remove()
        if test_goal(track.state):
            writeOutput( translatePath( track, initial_state, output ))
            print("Termino")
            return Queue
        posiblesPath = Nodes(track)
        output["nodes_expanded"] += 1
        for path in posiblesPath:      
            onePath = path.map[:]
            if onePath not in visited:
                key = Heuristica(path.map)
                path.key = key + path.depth
                Queue.insert(path)
                visited.add(path.map[:])
                if path.cost > output["max_search_depth"]:
                    output["max_search_depth"] += 1

def translatePath(node, initial_state, output):
    output["search_depth"] = node.depth
    while initial_state != node.state:
        if node.move == 1:
            path = 'Up'
        if node.move == 2:
            path = 'Down'
        if node.move == 3:
            path = 'Left'
        if node.move == 4:
            path = 'Right'
        output["path_to_goal"].insert(0, path)
        node = node.parent
    output["cost_of_path"] = len(output["path_to_goal"])
    return output

def Heuristica(node):
    prov = [ [0,1,2,1,2,3,2,3,4], [1,0,1,2,1,2,3,2,3], [2,1,0,3,2,1,4,3,2], 
    [1,2,3,0,1,2,1,2,3], [2,1,2,1,0,1,2,1,2], [3,2,1,2,1,0,3,2,1],
    [2,3,4,1,2,3,0,1,2], [3,2,3,2,1,2,1,0,1], [4,3,2,3,2,1,2,1,0]]
  
    return prov[0][node.index("0")] + prov[1][node.index("1")] + prov[2][node.index("2")] + prov[3][node.index("3")] + prov[4][node.index("4")] + prov[5][node.index("5")] + prov[6][node.index("6")] + prov[7][node.index("7")] + prov[8][node.index("8")] 
    ### CÓDIGO TERMINA AQUÍ ###

def calculate_total_cost(self,costo):
    global operacionCosto
    self.costo = costo
    operacionCosto =+ costo 
    return operacionCosto


def calculate_manhattan_dist(punto1, punto2):
    total = 0
    for i in range(len(punto1)):
        operacion = punto1[i] - punto2[i]
        total = total + abs(operacion)
    return total


def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    return puzzle_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ### SU CÓDIGO VA AQUÍ ###

global templateOutput
templateOutput = {
    "path_to_goal": [],
    "cost_of_path": 0,
    "nodes_expanded": 0,
    "search_depth": 0,
    "max_search_depth": 0
}

# Función Main que leerá las entradas y llamará el algoritmo correspondiente

def main():

    query = input().split(" ")

    sm = query[0].lower()

    begin_state = query[1].split(",")

    hard_state = list(map(int, begin_state))

    #size = int(math.sqrt(len(begin_state)))

    #hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":

        bfs_search(hard_state)

    elif sm == "dfs":

        dfs_search(hard_state)

    elif sm == "ast":

        A_star_search(hard_state)

    else:

        print("Introduzca comandos de argumentos válidos !")

if __name__ == '__main__':

    main()