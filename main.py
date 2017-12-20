import json
import Graph 
import Hopdistance as hd
import plot
import Arisnumber as an
import pandas as pd
import sys
import networkx as nx
import warnings

warnings.filterwarnings("ignore")

# List of options to run a specific part of the program
lst_contr=sys.argv

if lst_contr[1]=='reduce':
    print('Creating dataset...\n')
# Open a file json
    with open('reduced_dblp.json') as json_data:
        data = json.load(json_data)
elif lst_contr[1]=='full':
    print('Creating dataset...\n')
# Open a file json
    with open('full_dblp.json') as json_data:
        data = json.load(json_data)
else:
    print('Try again!\n')
    
# Create a weighted graph
print('Creating Graph...\n')
G= Graph.create_graph(data)
Graph.add_edges(data,G)
print('The graph is made, it has %s nodes and %s edges.\n'%(G.number_of_nodes(),G.number_of_edges()))

if lst_contr[2]=='2' and lst_contr[3]=='a':
# Set of all conferences of the dataset
    set_conf={conf for conf_lst in nx.get_node_attributes(G,'id_conference_int').values() for conf in conf_lst}
    while True:
        try:
            conf=int(input('Insert a conference id:\n'))
            if conf not in set_conf:
                raise KeyError
            break
        except KeyError:
            print('No conference in dataset\n')
        except:
            print('Invalid Value\n')            
# Subgraph of authors who have published at a specific conference
    conf_sub=list({node for node in G.nodes() if conf in G.node[node]['id_conference_int']})
    G_sub=G.subgraph(conf_sub)
# Plot of the graph
    print('Close the current plot to see the Statistics plot of Degree Centrality, Closeness Centrality and Betweeness Centrality\n')
    plot.create_graph_by_conf(G_sub,conf)
# Plot of Degree Centrality, Closeness Centrality and Betweeness Centrality
    plot.statistics_by_conf(G_sub,conf)
    
elif lst_contr[2]=='2' and lst_contr[3]=='b':
    while True:
        try:
            node,d=list(map(int,input('Insert node and number of edges:\n').split()))
            G[node]
            if d>20:
                raise KeyError
            break
# Control on the number of edges
        except KeyError:
            if d>20:
                print('The distance is too much\n')
            else:
                print('The node is not in the graph\n')
        except:
            print('Invalid Value\n')
# Subgraph of authors who have hop distance at most equal to d
    hp_dist=hd.Hop_Dist(G)
    G_hop=G.subgraph(hp_dist.hop_distance(d,node))
# Plot the graph
    plot.create_graph_by_auth(node,G_hop)


if lst_contr[2]=='3' and lst_contr[3]=='a':
# Find Aris' id
    aris_id=[name for name,attr in G.nodes(data=True) if attr['name_author']=='aris anagnostopoulos'][0]
    while True:
        try:
            id_author_start=int(input('Insert authors id:\n'))
            G[node]
        except KeyError:
            print('The node is not in the graph\n')
        except:
            print('Invalid Value\n')
# Find the wheight and the path of the shortest path that connect
# a specific author with Aris
    path=an.Shortest_Path(G)
# Plot the shortest distance
    plot.create_plot_shorter_path(G,path.dijkstrapath(id_author_start)[aris_id])

elif lst_contr[2]=='3' and lst_contr[3]=='b':
    set_id=set()
    print('Insert at most 21 nodes, press enter for less than 21 nodes')
    while True:
        try:
            inp_node=input('Insert node number %s:\n'%(len(set_id)+1))
            if len(set_id)==21 or inp_node=='':
                print('There are %s nodes in the subset\n'%len(set_id))
                break
            G[int(inp_node)]
            set_id.add(int(inp_node))
        except KeyError:
            print('The node is not in the graph\n')
        except:
            print('Invalid Value\n')
# Create a DataFrame with all the group number for each nodes of the graph
    path=an.Shortest_Path(G)  
    tab_groupnumber=pd.DataFrame.from_dict(path.GroupNumber(set_id),orient='index')
    tab_groupnumber.columns=['Weight','Shortest Path']
    tab_groupnumber.to_csv('tab_groupnumber.csv',encoding='utf-8')
    print(tab_groupnumber)
