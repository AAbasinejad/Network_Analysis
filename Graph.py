import json
import re
import html
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(inf_data):
    graph=nx.Graph()
    diz_aut={}
    for i in range(len(inf_data)):
        for auth in inf_data[i]["authors"]:
            if auth["author_id"] not in diz_aut.keys():
                diz_aut[(auth["author_id"])]={}
                diz_aut[(auth["author_id"])]["id_publication_int"]=set()
                diz_aut[(auth["author_id"])]["id_conference_int"]=set()
                
                diz_aut[(auth["author_id"])]["id_publication_int"].add(inf_data[i]["id_publication_int"])
                diz_aut[(auth["author_id"])]["id_conference_int"].add(inf_data[i]["id_conference_int"])
                
            else:
                diz_aut[(auth["author_id"])]["id_publication_int"].add(inf_data[i]["id_publication_int"])
                diz_aut[(auth["author_id"])]["id_conference_int"].add(inf_data[i]["id_conference_int"])

    for i in range(len(inf_data)):
        for auth in inf_data[i]["authors"]:
            if auth["author_id"] not in graph.nodes():
                graph.add_node(auth["author_id"], name=clean_name(auth["author"]), id_publication_int=list(diz_aut[auth["author_id"]]['id_publication_int']), id_conference_int=list(diz_aut[auth["author_id"]]['id_conference_int']))

    return graph

#Function to create weighted graph's edges
def add_edges(inf_data,graph):
    list_id_name=[[id_name['author_id'] for id_name in elem['authors']] for elem in inf_data if len(elem['authors'])>1]
    # For loops in a set where there are all edges of our graph
    for edge in {subset for elem in list_id_name for subset in itertools.combinations(elem,2)}:
        graph.add_edge(edge[0],edge[1],weight=1-jaccard_similarity(graph.node[edge[0]]['id_publication_int'],graph.node[edge[1]]['id_publication_int']))


 
'''
        PLOT

'''

def create_graph(node,G_def ):
    first_node=hope_distance(1, node, G_def)
    second_level_node=[i for i in hope_distance(2, node, G_def) if i not in hope_distance(1, node, G_def)]
    third_level_node=[i for i in hope_distance(3, node, G_def) if i not in hope_distance(2, node, G_def)]
    
    node_colours=[]
    for node in G_def.nodes():
        if node in first_node:
            node_colours.append('red')
        elif node in second_level_node:
            node_colours.append('lightcoral')
        elif node in third_level_node:
            node_colours.append('orchid')
        else:
            node_colours.append('dodgerblue')
            
    
    # nodi che hanno più di 4 collegamenti più gradi
    node_2_conn=[node for node in G_def.nodes() if len(G_def[node]) <=2 ] 
    node_2_6_conn=[node for node in G_def.nodes() if len(G_def[node])>2 and len(G_def[node])<=6  ]
    node_6_10_conn=[node for node in G_def.nodes() if len(G_def[node])>6 and len(G_def[node])<=10 ]
    node_10_15_conn=[node for node in G_def.nodes() if len(G_def[node])>10 and len(G_def[node])<=15 ]
    
            
    node_size=[]
    for node in G_def.nodes():
        if node in node_2_conn:
            node_size.append(5)
        elif node in node_2_6_conn:
            node_size.append(10)
        elif node in node_6_10_conn:
            node_size.append(80)
        elif node in node_10_15_conn:
            node_size.append(100)
        else:
            node_size.append(200)
    
    nx.draw(G_def,pos=nx.spring_layout(G_def), 
            cmap=plt.get_cmap('jet'),
            node_color =node_colours,
            node_size = node_size,
            width=0.5,
            style='dotted',
            alpha=0.9)


