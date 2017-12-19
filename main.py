import json
import networkx as nx
import CreationGraph as cg
import Hopdistance as hd
#import plot
import Arisnumber as an

# Open a file json
with open('reduced_dblp.json') as json_data:
    data = json.load(json_data)
    
# Create a weighted graph
G= cg.create_graph(data)
cg.add_edges(data,G)

# Subgraph of authors who published at a specific conference
conf=int(input('Insert a conference id:\n'))
conf_sub=list({node for node in G.nodes() if conf in G.node[node]['id_conference_int']})
G_sub=G.subgraph(conf_sub)

#Stat functions to study graphs Part 1
#Degree
Deg_centrality=nx.degree_centrality(G_sub)
#Closeness
Clos_centrality=nx.closeness_centrality(G_sub)
# Betweenness
Betw_centrality=nx.betweenness_centrality(G_sub)


# Stat Part 2
# Subgraph of authors who have hop distance at most equal to d
node,d=list(map(int,input('Insert node and number of edges:\n').split()))
hp_dist=hd.Hop_Dist(G)
G_hop=G.subgraph(hp_dist.hop_distance(d,node))


# Parte 3.a of homework
# Find the wheight and the path of the shortest path that connect
# a specific author with Aris
id_author_start=int(input('Insert authors id:\n'))
# Find Aris' id
aris_id=[name for name,attr in G.nodes(data=True) if attr['name_author']=='aris anagnostopoulos'][0]
path=an.Shortest_Path(G)
path.dijkstrapath(id_author_start)[aris_id]

# Parte 3.b of homework
set_id=set()
print('Insert at most 21 nodes, press enter for less than 21 nodes')
while True:
    inp=input('Insert node number %s:\n'%(len(set_id)+1))
    if len(set_id)==21 or inp=='':
        print('There are %s nodes in the subset\n'%len(set_id))
        break
    set_id.add(int(inp))
    
path.GroupNumber(set_id)