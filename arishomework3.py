import json
import re
import html
import itertools
import networkx as nx
#import plotly.plotly as py
#from plotly.graph_objs import *

# Function to clean the name
def clean_name(name):
    name=html.unescape(name)
    return re.sub(r'[0-9]+','',name)

# Function to calculate jaccard similarity
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return (intersection_cardinality/float(union_cardinality))

#Function to create a graph's nodes without edges
def create_graph(inf_data):
    graph=nx.Graph()
    for i in range(len(inf_data)):
        for auth in inf_data[i]['authors']:
            if auth['author_id'] not in graph.nodes():
                graph.add_node(auth['author_id'])
                graph[auth['author_id']]['name']=clean_name(auth['author'])
                graph[auth['author_id']]['id_publication_int']=[]
                graph[auth['author_id']]['id_conference_int']=[]
                graph[auth['author_id']]['id_publication_int'].append(inf_data[i]['id_publication_int'])
                graph[auth['author_id']]['id_conference_int'].append(inf_data[i]['id_conference_int'])
            else:
                graph[auth['author_id']]['id_publication_int'].append(inf_data[i]['id_publication_int'])
                graph[auth['author_id']]['id_conference_int'].append(inf_data[i]['id_conference_int'])
    return graph

#Function to create weighted graph's edges
def add_edges(inf_data,graph):
    list_id_name=[[id_name['author_id'] for id_name in elem['authors']] for elem in inf_data if len(elem['authors'])>1]
    # For loops in a set where there are all edges of our graph
    for edge in {subset for elem in list_id_name for subset in itertools.combinations(elem,2)}:
        graph.add_edge(edge[0],edge[1],weight=1-jaccard_similarity(graph[edge[0]]['id_publication_int'],graph[edge[1]]['id_publication_int']))

# Main corpus
        
#Open a file json
with open('reduced_dblp.json') as json_data:
    data = json.load(json_data)
    
# Create a weighted graph
G= create_graph(data)
add_edges(data,G)

# Subgraph
conf=int(input('Insert an id of a conference:\n'))
conf_sub=list({node for node in G.nodes() if conf in G[node]['id_conference_int']})
G_sub=G.subgraph(conf_sub)











