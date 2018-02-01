# Network Analysis 
__Introduction__: Carry out an analysis of a Network of Computer Scientists by applying the [Graph methods](https://networkx.github.io/) in python.

__Data__: In this project we have used the [DBLP](http://dblp.uni-trier.de/) dataset which contains information about Computer Scientists articles, and we worked on two json file: [*__full_dblp__*](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/full_dblp.json.zip ) json file, which needs to be parsed and contains the entire network, and  [*__reduced_dblp__*](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/reduced_dblp.json.zip) json file for testing and debugging, which needs to be parsed and contains a portion of the network, also `Python 3.x` was used in this project.

In root directory run:

`python main.py <data> <exercise_number> <exercise_letter>`

* *__data__*: It can be *reduce* if you want to use the __reduced_dblp__ dataset or *full* if you want to use __full_dblp__.
* *__exercise_number__*: It can be *1* (just to make graph), *2* (just to run second part of the task) or *3* (just to run Third part of the task)
* *__exercise_letter__*: It can be *a* or *b* (only if the second Argument is *2* and *3*, for each part of them)

specific libraries which have to be installed:
```python
import pandas as pd
import networkx as nx
import numpy

```

__Modules__:

* [*__`main.py`__* ](https://github.com/AAbasinejad/CS-Network/blob/master/main.py): 

This module is the main corpus of the project, and initialises and calls other functions, listed later in this README file.

* [*__`Graph.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Graph.py):

By processing JSON file, it creates a graph, G, whose nodes are the authors and The edges identify whether two authors share at least one common publication. Each edge is weighted in the following way:
<d1>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?w(a_1,a_2)&space;=&space;1&space;-&space;J(p_1,&space;p_2)" title="Weight Formula" width="200"/>
</p>
</d1>

> where a1, a2 are authors, p1 and p2 are the set of publication of the two authors and, J(p1 , p2) represents the jaccard similarity between these two sets of publications.

Functions definition:
```python
def create_graph(inf_data): #this function creates a graph's nodes without edges, (this function must be called with a #loaded json dataset file as a argument)
def add_edges(inf_data,graph): #this function is used to create weighted graph's edges, (this must be called with a loaded json 
#dataset and the results nodes of previous function.
```

* [*__`Arisnumber.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Arisnumber.py): 

This module contains a class named `class Shortest_Path():` which is used to find the weight of the shortest path that connects the input author with [Aris](http://aris.me/) and the group number of each node of graph, using a given set of author.

Functions definition:
```python
def __init__(self, graph): # for Initialization
def create_dict_connection(self): # Function to make a dictionary that nodes appears as keys and tuples of connected nodes 
#as values in this form: ("connected node", "weight")
def path_list(path,lst_path): # This function makes a list containing the path between pair of connected nodes.
def dijkstrapath(self,start): # This function calculates the shortest distance between an author and the other nodes, by using Dijkstra.
def GroupNumber(self,set_id_author): # Dictionary with all shortest paths for the nodes of the input set.
```

* [*__`GenericFunctions.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/GenericFunctions.py):

This file contains just three generic functions which are called in other modules.

Functions definition:
```python
def clean_name(name): # This function cleans the names 
def jaccard_similarity(lst1,lst2): # This function is to calculate jaccard_similarity between two lists
def Id_name(graph,node_auth): # This function is to convert the authors' ids into their corresponding names
```
* [*__`Hopdistance.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Hopdistance.py): 

This module contains a class named `Hop_Dist`, which, given an input node and an integer d, finds all nodes that have hop distance at most equal to d. It contains several functions:
```python
def connect(self,lst_node,step): # Recursive function to calculate the hop distance, when the number of step is more than 1
def hop_distance(self,step, node): # Function to calculate the hop distance of a specific input author for the 3 main situations
```

* [*__`plot.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/plot.py): 

This module contains several functions to plot results of the project.

Functions definition:

```python
def create_graph_by_conf(G_def, conf): # This function plots the subgraph of the nodes (authors) participating in the same
#conference. The colors of the node represent the hop distance from the main node, the size of the node is directly 
#proportional to the number of the edges of each node.
def statistics_by_conf(G_sub, conf): # This function creates a histogram that rapresnt illustrating the three types of 
#centrality analysed, i.e. betweenness centrality, degree centrality and closeness centality. The subgraph shows every 
#author who participated to the input conference.
def create_graph_by_auth(node,G_def): # This funcion creates a plot showing the main node (i.e. the input author), and 
#the adjacent nodes (with hop distance equal to the input d previously mentioned). the colours of the nodes illustrate the different level of distance from the main one, whilst their size rapresents the number of edges.
def create_plot_shorter_path(G,tup_node): # This function creates a plot of the shortest path between any two nodes. 
#Each node's label is the name of the author, whilst the cost of the shortest path is shown in the title.
```
