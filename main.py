import json
import Graph 
import Hopdistance as hd
import plot
import Arisnumber as an
import networkx as nx
import pandas as pd

# Open a file json
with open('reduced_dblp.json') as json_data:
    data = json.load(json_data)
    
# Create a weighted graph
G= Graph.create_graph(data)
Graph.add_edges(data,G)

# Subgraph of authors who published at a specific conference
conf=int(input('Insert a conference id:\n'))

if [conf] not in nx.get_node_attributes(G,'id_conference_int').values():
    print('No conference in dataset')
else:
    conf_sub=list({node for node in G.nodes() if conf in G.node[node]['id_conference_int']})
    G_sub=G.subgraph(conf_sub)
    plot.create_graph_by_conf(G_sub,conf)
    #Stat functions to study graphs Part 1
    plot.statistics_by_conf(G_sub,conf)


# Stat Part 2
# Subgraph of authors who have hop distance at most equal to d
node,d=list(map(int,input('Insert node and number of edges:\n').split()))
if node not in G.nodes():
    print('The node is not in the graph\n')
# Condition on the hop distance 
elif d>20:
    print('The distance is too much\n')
else:
    hp_dist=hd.Hop_Dist(G)
    G_hop=G.subgraph(hp_dist.hop_distance(d,node))
    plot.create_graph_by_auth(node,G_hop)


# Parte 3.a of homework
# Find the wheight and the path of the shortest path that connect
# Find Aris' id
aris_id=[name for name,attr in G.nodes(data=True) if attr['name_author']=='aris anagnostopoulos'][0]
# a specific author with Aris
id_author_start=int(input('Insert authors id:\n'))
if id_author_start not in G.nodes():
    print('The node is not in the graph\n')
else:
    path=an.Shortest_Path(G)
    plot.create_plot_shorter_path(G,path.dijkstrapath(id_author_start)[aris_id])


# Parte 3.b of homework
set_id=set()
print('Insert at most 21 nodes, press enter for less than 21 nodes')
while True:
    inp_node=input('Insert node number %s:\n'%(len(set_id)+1))
    if len(set_id)==21 or inp_node=='':
        print('There are %s nodes in the subset\n'%len(set_id))
        break
    if int(inp_node) not in G.nodes():
        print('The node is not in the graph\n')
        continue
    else:
        set_id.add(int(inp_node))
    
tab_groupnumber=pd.DataFrame.from_dict(path.GroupNumber(set_id),orient='index')
tab_groupnumber.columns=['Weight','Shortest Path']
tab_groupnumber.to_csv('tab_groupnumber.csv',encoding='utf-8')
