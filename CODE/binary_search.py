#Importacion del grafo desde csv
import csv
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
 
plt.title("Graph Image")
image = mpimg.imread("graph.png")
plt.imshow(image)
plt.show()

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
                    formed_nodes.append([self.nodes[y], self.nodes[x]])
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
 

#Breadth First Search -> FIFO queue
def Bidirectional_search(tree, start, end):
    pass

def Breadth_Search(tree, start, end):
    queue = []
    current_node = start
    while tree:
        queue = tree.pop(0)
        if current_node == end:
            return queue
        node_childs = [node_tuple[1] for node_tuple in tree if node_tuple[0] == current_node]
        print('node_childs', node_childs)
        


    
def main():
    g = graph(nodes, matrix)
    print(len(g.get_Tuples()))
    Breadth_Search(g.get_Tuples(), "Cancun", "Valladolid")
    
    
main()