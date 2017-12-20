from collections import defaultdict
import networkx as nx
import heapq

# Class to find Aris number and the group number of each node of graph, using a given set of author
class Shortest_Path():
    
    def __init__(self, graph):  
        self.graph=graph
        
# Function to have a dictionary wich there is nodes as key and tuples of connected nodes to each key
# in this form: ("connected node", "weight")
    def create_dict_connection(self):
        edges=nx.to_edgelist(self.graph.to_directed())
        dic = defaultdict(list)
        for id_1,id_2,weight in edges:
            dic[id_1].append((id_2,weight['weight']))
        return dic
    
# Function to obtain a good output of the shortest path   
    def path_list(path,lst_path):
        if path==():
            return lst_path[::-1]
        lst_path.append(path[0])
        return Shortest_Path.path_list(path[1],lst_path)
    
# Function to calculate the shortes distance between an author and the others nodes, using heap;
# it returns a dictionary with the shortest path and the corresponding weight
    def dijkstrapath(self,start):    
        weight_dic=self.create_dict_connection()
# Initialize queue
        queue= [(0,start,())]
# Set of visited nodes
        visited=set()
        dict_path={}
        while queue:
# Take the element with the least weight from the queue
            weight,vertex1,path = heapq.heappop(queue)
            if vertex1 not in visited:
                visited.add(vertex1)
                path = (vertex1, path)
                dict_path[vertex1]=(weight, Shortest_Path.path_list(path,[]))   
# Take into account the linked nodes with the v1 node
                for vertex2, c in weight_dic.get(vertex1,()):
                    if vertex2 not in visited:
# Push every nodes, which is not in my visited set, in my queue
                        heapq.heappush(queue, (weight+c, vertex2, path))
        return dict_path

    def GroupNumber(self,set_id_author):
# Dictionary with all shrtest paths for the nodes of the input set
        dict_set={node_set:self.dijkstrapath(node_set) for node_set in set_id_author}
# Dictionary of all shortest path between each node of the graph and the nodes of the set
        total_group_number=defaultdict(list)
        for node_set in set_id_author:    
            for node in self.graph.nodes():
                if node not in dict_set[node_set].keys():
                    continue
                elif node!= node_set:
                    total_group_number[node].append(dict_set[node_set][node])  
# Modify the previous dictionary with only the shortest path with the minimum weight     
        for node in total_group_number.keys():
            if len(total_group_number[node])!=0:
                total_group_number[node].sort(key=lambda x:x[0])
                total_group_number[node]=total_group_number[node][0]
                
        return total_group_number
