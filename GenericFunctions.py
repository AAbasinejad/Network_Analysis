import re
import html

# Function to clean the name
def clean_name(name):
    name=html.unescape(name)
    return re.sub(r'[0-9]+','',name)

# Function to calculate jaccard similarity
def jaccard_similarity(lst1,lst2):
    intersection_cardinality = len(set.intersection(*[set(lst1), set(lst2)]))
    union_cardinality = len(set.union(*[set(lst1), set(lst2)]))
    return (intersection_cardinality/float(union_cardinality))

# Function to convert the author's id in corresponding author's name
def Id_name(graph,node_auth):
    for node in graph.nodes():
         if node == node_auth:
             return graph.node[node]['name_author']
         
    
    