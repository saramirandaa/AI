#Importacion del grafo desde csv
import csv
import time

matrix = []
nodes = []

#los valores de la matriz se pasan a una lista de listas
with open('matrix.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cStr = ",".join(row)
        cStr2 = cStr.split(',')
        A = [int(x) for x in cStr2]
        matrix.append(A)
        del cStr2, A
#los valores de los nodos se pasan a un string
with open('nodes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader: 
        nodes.append(row)  
#se convierte de string a lista
nodesStr = "".join(nodes[0])
nodes = nodesStr.split(',')
nodes_copy = nodes.copy()
nodes.clear()
for name in nodes_copy:
    nodes.append(name.upper())

#clase grafo en donde se pasa como parametros los nodos y la matriz
class graph:
    #constructor que nos permite tener los parametros 
    def __init__(self, nodes, graph_matrix):
        self.nodes = nodes
        self.graph = graph_matrix
        
    #metodo que nos devolverá los nodos creados 
    def get_Tuples(self):
        formed_nodes = []
        self.weights = []
        self.nodes_and_weigths = []
        #un for con la longitud de la longitud en y de nuestra matriz
        for y in range(len(self.graph)):
            for x in range(len(self.graph[0])):
                if self.graph[y][x] != 0:
                    #Aqui se forman las conexiones de cada nodo
                    formed_nodes.append((self.nodes[y], self.nodes[x]))
                    self.weights.append(self.graph[y][x])
                    #Aquí se hace una lista con los nodos y su peso
                    self.nodes_and_weigths.append([formed_nodes[y], self.graph[y][x]])   
        return formed_nodes
    
    #metodo que regresa solo los pesos
    def get_weights(self):
        self.get_Tuples()
        return self.weights
    
    #metodo que regresa una lista de los nodos y sus respectivos pesos
    def get_tuples_weights(self):
        self.get_Tuples()
        return self.nodes_and_weigths

class graph_Search_methods():
    def __init__(self, nodes, tree, start, end, depth, graph):
        self.nodes = nodes
        self.graph = graph
        self.__tree = tree
        self.__start = start
        self.__end = end
        self.__depth_level_limit = depth
    def Depth_Search(self):
        print("\t===== DEPTH SEARCH =====")
        stack = [[self.__start]]
    
        while stack:
            branch = stack.pop()
            current_node = branch[-1]
    
            if current_node == self.__end:
                return branch
    
            node_childs = [node_tuple[1] for node_tuple in self.__tree if node_tuple[0] == current_node]
            for child in node_childs[::-1]:
                if child is not None:
                    new_branch = branch.copy()
                    new_branch.append(child)
                    stack.append(new_branch)
                    
    def IterDepthSearch(self):
        print("\t===== DEPTH LIMITED SEARCH =====")
        queue = [[self.__start]]
        depth_level_counter = 0
        
        while queue:
            branch = queue.pop(0)
            current_node = branch[-1]
            
            if current_node == self.__end or depth_level_counter == self.__depth_level_limit:
                if self.__end not in branch:
                    branch.append(self.__end)
                return branch
            
            def check_childs_depth(branch,child):
                if child is not None:
                    new_branch = branch.copy()
                    new_branch.append(child)
                    queue.append(new_branch)
            
            node_childs = [node_tuple[1] for node_tuple in self.__tree if node_tuple[0] == current_node]
            [check_childs_depth(branch, child) for child in node_childs]

            depth_level_counter += 1

    def Breadth_Search(self):
        print("\t===== BREADTH SEARCH =====")
        nodes_visited = []
        queue = [[self.__start]]
        
        while queue:
            branch = queue.pop(0)
            current_node = branch[-1]
            
            if current_node == self.__end:
                return branch

            if current_node not in nodes_visited:
                nodes_visited.append(current_node)
            
            node_childs = [node_tuple[1] for node_tuple in self.__tree if node_tuple[0] == current_node]
            
            for child in node_childs:
                if child == self.__end:
                    branch.append(child)
                    return branch
                    
                if child not in nodes_visited:
                    new_branch = queue.copy()
                    new_branch.append(child)
                    queue.append(new_branch)

        
    def Dijkstra_search(self):
        print("===== DIJKSTRA SEARCH =====")
        start = self.__start
        destiny = self.__end
        
        #  Verificamos que el nodo inicial y el nodo final existan en el grafo
        if start not in self.nodes:
            print("\nERROR . . . The start node does not exist in the graph")
            return
        if destiny not in self.nodes:
            print("\nERROR . . . The destiny node does not exist in the graph")
            return
        # Inicializamos las variables necesarias para el algoritmo
        nodes = set(self.nodes)
        visited = {start: 0}
        path = {}
        unvisited = {node: float("inf") for node in nodes}
        unvisited[start] = 0
        # Mientras haya nodos por visitar
        while unvisited:
            # Seleccionamos el nodo con la menor distancia
            current_node = min(unvisited, key=unvisited.get)
            # Marcamos el nodo como visitado
            visited[current_node] = unvisited[current_node]
            unvisited.pop(current_node)
            # Calculamos la distancia de los nodos vecinos al nodo actual
            for neighbor in self.nodes:
                if self.graph[self.nodes.index(current_node)][self.nodes.index(neighbor)] != 0:
                    distance = visited[current_node] + self.graph[self.nodes.index(current_node)][self.nodes.index(neighbor)]
                    if neighbor not in visited and distance < unvisited[neighbor]:
                        unvisited[neighbor] = distance
                        path[neighbor] = current_node
            # Si el nodo actual es el nodo final, terminamos el algoritmo
            if current_node == destiny:
                break
        #Si no hay un camino
        if destiny not in path:
            print("\nERROR . . . There is no path between", start, "and", destiny)
        else:
            #Imprimir el camino más corto entre el nodo inicial y el nodo final, Además de los pesos entre cada nodo
            print("\nThe shortest path between", start, "and", destiny, "is:")
            print(destiny, end="")
            current_node = destiny
            while current_node != start:
                print(" <--- ", path[current_node], end="")
                current_node = path[current_node]
            print("\n\n ---> The total weight is:", visited[destiny])
            
    def Bidirectional_Search(self):
        print("\t===== BIDIRECTIONAL SEARCH =====")
        nodes_visited = set()
        queue = [[self.__start]]
        queue_rev = [[self.__end]]
        tree_rev = self.__tree[::-1]
    
        while queue and queue_rev:
            # Avanzar desde el inicio
            branch = queue.pop(0)
            current_node = branch[-1]
    
            if current_node == self.__end:
                return branch
    
            if current_node not in nodes_visited:
                nodes_visited.add(current_node)
    
            node_childs = [node_tuple[1] for node_tuple in self.__tree if node_tuple[0] == current_node]
            for child in node_childs:
                if child == self.__end:
                    branch.append(child)
                    return branch
                if child not in nodes_visited:
                    new_branch = branch.copy()
                    new_branch.append(child)
                    queue.append(new_branch)
                    nodes_visited.add(child)
    
            # Avanzar desde el final
            branch_rev = queue_rev.pop(0)
            current_node_rev = branch_rev[-1]
    
            if current_node_rev == self.__start:
                return branch_rev[::-1]
    
            if current_node_rev not in nodes_visited:
                nodes_visited.add(current_node_rev)
    
            node_childs_rev = [node_tuple[1] for node_tuple in tree_rev if node_tuple[0] == current_node_rev]
            for child_rev in node_childs_rev:
                if child_rev == self.__start:
                    branch_rev.append(child_rev)
                    return branch_rev[::-1]
                if child_rev not in nodes_visited:
                    new_branch_rev = branch_rev.copy()
                    new_branch_rev.append(child_rev)
                    queue_rev.append(new_branch_rev)
                    nodes_visited.add(child_rev)
    


def Unweighted(start, end, limit, flag):
    print("\n\n")
    g = graph(nodes, matrix)
    tups = g.get_Tuples()
    search = graph_Search_methods(nodes, tups, start, end, limit, matrix)
    
    #beadth
    start_time = time.time()
    print(search.Breadth_Search())
    end_time = time.time()
    print("SEARCH TIME = ", (end_time - start_time),"\n\n")
    ## depth
    start_time = time.time()
    print(search.Depth_Search())
    end_time = time.time()
    print("SEARCH TIME = ", (end_time - start_time),"\n\n")
    ## Iterative
    start_time = time.time()
    print(search.IterDepthSearch())
    end_time = time.time()
    print("SEARCH TIME = ", (end_time - start_time),"\n\n")
    ## Bidirectional
    start_time = time.time()
    print(search.Bidirectional_Search())
    end_time = time.time()
    print("SEARCH TIME = ", (end_time - start_time),"\n\n")
    
    #---
    if flag == 2:
        start_time = time.time()
        search.Dijkstra_search()
        end_time = time.time()
        print("SEARCH TIME = ", (end_time - start_time),"\n\n")

def Search_Menu():
    print("\n\tWelcome to the Graph Search program")
    start = (input("START: "))
    end = (input("END: "))
    limit = int(input("LIMIT: "))
    start = start.upper()
    end = end.upper()
    print("Choose the type of graph you would like to use:")
    graph = int(input("\tUNWEIGHTED (1), WEIGHTED (2): "))
    if graph == 1:
        Unweighted(start, end, limit, 1)
    elif graph == 2:
        Unweighted(start, end, limit, 2)
    else:
        Search_Menu()
        
def main():
    Search_Menu()

    
main()