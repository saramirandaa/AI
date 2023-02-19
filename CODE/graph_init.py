import csv

connections = []
graph = []
nodes = []

with open('data.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: 
        connections.append(row)

with open('nodes.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader: 
        nodes.append(row)
graph.append(connections) 
   



# class graph:
#     def __init__(self, nodes, graph):
#         self.nodes = nodes
#         self.graph = graph
       
#     def get_Connections(self):
#         formed_nodes = []
#         nodes_and_weigths = []
#         self.conns_nodes_weights = []
#         for y in range(len(self.graph)):
#             for x in range(len(self.graph[0])):
#                 if self.graph[y][x] != 0:
#                     formed_nodes.append([self.nodes[y], self.nodes[x]])
#                     nodes_and_weigths.append([formed_nodes[y], self.graph[y],[x]])
            
#             if len(nodes_and_weigths) != 0:
#                 self.conns_nodes_weights.append([formed_nodes[y], nodes_and_weigths])
#         return formed_nodes
    
# clase  = graph(nodes, graph)
# conns = clase.get_Connections()
# print(conns)