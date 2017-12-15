import json
import networkx as nx
import CreationGraph as cg
import functions as f

#Open a file json
with open('reduced_dblp.json') as json_data:
    data = json.load(json_data)
    
# Create a weighted graph
G= cg.create_graph(data)
cg.add_edges(data,G)

# Subgraph
conf=int(input('Insert an id of a conference:\n'))
conf_sub=list({node for node in G.nodes() if conf in G.node[node]['id_conference_int']})
G_sub=G.subgraph(conf_sub)


#Stat functions to study graphs Part 1
#Degree
Deg_centrality=nx.degree_centrality(G_sub)
#Closeness
Clos_centrality=nx.closeness_centrality(G_sub)
# Betweenness
Betw_centrality=nx.betweenness_centrality(G_sub)
Edge_betw_centrality=nx.edge_betweenness_centrality(G_sub)

# Stat Part 2
node,d=list(map(int,input('Insert node and number of edges:\n').split()))
G_def=G.subgraph(f.hope_distance(d,node,G))

# Parte 3 of homework

id_author=int(input('Insert authors id:\n'))

