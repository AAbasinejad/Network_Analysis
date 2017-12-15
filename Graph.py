import json
import re
import html
import itertools
import networkx as nx

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

