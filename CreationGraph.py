import itertools
import networkx as nx
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

# Function to create a graph's nodes without edges
def create_graph(inf_data):
    graph=nx.Graph()
    dict_aut={} 
# These 2 'for' loops create the attributes for each node
    for i in range(len(inf_data)):
        for auth in inf_data[i]["authors"]:
            if auth["author_id"] not in dict_aut.keys():
                dict_aut[(auth["author_id"])]={}
                dict_aut[(auth["author_id"])]["id_publication_int"]=set()
                dict_aut[(auth["author_id"])]["id_conference_int"]=set()
                dict_aut[(auth["author_id"])]["id_publication_int"].add(inf_data[i]["id_publication_int"])
                dict_aut[(auth["author_id"])]["id_conference_int"].add(inf_data[i]["id_conference_int"])
            else:
                dict_aut[(auth["author_id"])]["id_publication_int"].add(inf_data[i]["id_publication_int"])
                dict_aut[(auth["author_id"])]["id_conference_int"].add(inf_data[i]["id_conference_int"])
                
# These 2 'for' loops create the nodes of the graph
    for i in range(len(inf_data)):
        for auth in inf_data[i]["authors"]:
            if auth["author_id"] not in graph.nodes():
                graph.add_node(auth["author_id"], name_author=clean_name(auth["author"]), id_publication_int=list(dict_aut[auth["author_id"]]['id_publication_int']),
                               id_conference_int=list(dict_aut[auth["author_id"]]['id_conference_int']))
    return graph

# Function to create weighted graph's edges
def add_edges(inf_data,graph):
    list_id_name=[[id_name['author_id'] for id_name in elem['authors']] for elem in inf_data if len(elem['authors'])>1]
    # This 'for' loop creates the edges of the graph, taking them from a set of tuples, where there are all possible 
    # combination between nodes which are linked
    for edge in {subset for elem in list_id_name for subset in itertools.combinations(elem,2)}:
        graph.add_edge(edge[0],edge[1],weight=1-jaccard_similarity(graph.node[edge[0]]['id_publication_int'],graph.node[edge[1]]['id_publication_int']))

