# Class to find the hop distance from a specific input node
class Hop_Dist():
    def __init__(self,graph):
        self.graph=graph
        
# Recursive function to calculate the hop distance, when the number of step is more than 1
    def connect(self,lst_node,step):
        if step==0:
            return lst_node
# Take into account the neighbors of a specific node
        connection=[key_author for author in lst_node for key_author in self.graph.neighbors(author)]
        lst_node+=connection
        return self.connect(connection,step-1)
    
# Function to calculate the hop distance of a specific input author for the main 3 situations
    def hop_distance(self,step, node):
        node_connection=[node]
# Case 0: when the step is zero
        if step==0:
            lst_connect=node_connection
# Case 1: when the step is one
        elif step==1:
            connection=self.graph.neighbors(node)
            lst_connect=node_connection+connection
# Case 3: when the step is more than 1
        else:
            lst_connect=self.connect(node_connection,step)  
        return(lst_connect)




