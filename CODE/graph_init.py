
import csv

matrix = []
nodes = []

with open('matrix.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cStr = ",".join(row)
        cStr2 = cStr.split(',')
        A = [int(x) for x in cStr2]
        matrix.append(A)
        del cStr2, A
        
with open('nodes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader: 
        nodes.append(row)

nodesStr = "".join(nodes[0])
nodes = nodesStr.split(',')

class graph:
    def __init__(self, nodes, graph2):
        self.nodes = nodes
        self.graph = graph2
       
    def get_Connections(self):
        formed_nodes = []
        nodes_and_weigths = []
        self.conns_nodes_weights = []
        for y in range(len(self.graph)):
            for x in range(len(self.graph[0])):
                if self.graph[y][x] != 0:
                    formed_nodes.append([self.nodes[y], self.nodes[x]])
                    nodes_and_weigths.append([formed_nodes[y], self.graph[y],[x]])
            
            if len(nodes_and_weigths) != 0:
                self.conns_nodes_weights.append([formed_nodes[y], nodes_and_weigths])
        return formed_nodes
    
g = graph(nodes, matrix)
print(len(matrix))
print(len(nodes))

print(g.get_Connections())