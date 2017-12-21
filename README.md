# CS-Network
Repository for Homework __4__ of Algorithmic Methods for Data Mining - *__Group 1__*.

__Introduction__: Carry out some information from Computer Scientists network by applying the [Graph methods](https://networkx.github.io/).

__Data__: In this project we've used the [DBLP](http://dblp.uni-trier.de/) dataset, and we worked on two json file: [*__full_dblp__*](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/full_dblp.json.zip ) json file, which needs to be parsed and contains the entire network, and  [*__reduced_dblp__*](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/reduced_dblp.json.zip) json file for testing and debugging, which needs to be parsed and contains a portion of the network, also `Pyhton 3.x` was used in this project.

In root directory run:

`python main.py <data> <exercise_number> <exercise_letter>`

* *__data__*: It can be *reduce* if you want to use the __reduced_dblp__ dataset or *full* if you want to use __full_dblp__.
* *__exercise_number__*: It can be *1* (just to make graph), *2* (just to run second part of the task) or *3* (just to run Third part of the task)
* *__exercise_letter__*: It can be *a* or *b* (only if the second Argument is *2* and *3*, for each part of them)

__Modules__:

* [*__`main.py`__* ](https://github.com/AAbasinejad/CS-Network/blob/master/main.py): 

This file is the main corpus of the project, and it is to initialize and call another functions, which will explain in following.

Modules and libraries which has to be imported:
```python
import json
import Graph 
import Hopdistance as hd
import plot
import Arisnumber as an
import pandas as pd
import sys
import networkx as nx
import warnings
```

* [*__`Graph.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Graph.py):

By processing JSON file, it creates a graph, G, whose nodes are the authors and one edge between two nodes is a connection if they have at least one publication in common. Each edge is weighted in the following way:
<d1>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?w(a_1,a_2)&space;=&space;1&space;-&space;J(p_1,&space;p_2)" title="Weight Formula" width="200"/>
</p>
</d1>

> where a1, a2 are authors, p1 and p2 are the set of publication of the two authors and, J(p1 , p2) represents the jaccard similarity between these two sets of publications.


Modules and libraries which has to be imported:
```python
import itertools
import networkx as nx
import GenericFunctions as gf
```
Functions definition:
```python
def create_graph(inf_data): #this function is to create a graph's nodes without edges, (this function must be called with a #loaded json dataset file as a argument)
def add_edges(inf_data,graph): #this function is used to create weighted graph's edges, (this must be called with a loaded json 
#dataset and the results nodes of previous function.
```

* [*__`Arisnumber.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Arisnumber.py): 

This file contains a class named `class Shortest_Path():` which is used to find the weight of the shortest path that connects the input author with [Aris](http://aris.me/) and the group number of each node of graph, using a given set of author.

Modules and libraries which has to be imported:
```python
from collections import defaultdict
import networkx as nx
import heapq
```
Functions definition:
```python
def __init__(self, graph): # for Initialization
def create_dict_connection(self): # Function to make a dictionary that nodes appears as keys and tuples of connected nodes to 
#each key as values in this form: ("connected node", "weight")
def path_list(path,lst_path): # this function is to made a list which contain a path between each two connected node.
def dijkstrapath(self,start): #this function is to calculate the shortest distance between an author and the others nodes, using heap.
def GroupNumber(self,set_id_author): # Dictionary with all shortest paths for the nodes of the input set.
```

* [*__`GenericFunctions.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/GenericFunctions.py):

This file contains just three generic functions which are used in previous and following modules.

Modules and libraries which has to be imported:
```python
import re
import html
```
Functions definition:
```python
def clean_name(name): #this function is to clean the names 
def jaccard_similarity(lst1,lst2): #this function is to calculate jaccard_similarity between two lists
def Id_name(graph,node_auth): #this function is to convert the authors' ids into their corresponding names
```
* [*__`Hopdistance.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Hopdistance.py): 

This file contains a class named `Hop_Dist`, which finds all nodes that have hop distance at most equal to an integer d, starting from an input node, given both of them by the user. It contains several functions:
```python
def connect(self,lst_node,step): # Recursive function to calculate the hop distance, when the number of step is more than 1
def hop_distance(self,step, node): # Function to calculate the hop distance of a specific input author for the 3 main situations
```

* [*__`plot.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/plot.py): 

This file contains several functions to plot results of the project.

Modules and libraries which has to be imported:

```python
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy
import Hopdistance as hd
import GenericFunctions as gf
```
Functions definition:

```python
def create_graph_by_conf(G_def, conf): # this function plot the subgraph of the nodes (authors) participating in the same
#conference. The colors of the node rapresented the hope distance from a principal node, the size of the node is directly 
#proportional at the number of the edges of each node.
def statistics_by_conf(G_sub, conf): # this function create an histogram that rapresnt three different results about the 
#nodes of the subgraph: betweenness centrality, degree centrality and closeness centality. The subgraph represented every 
#nodes (author) that participate at that conference.
def create_graph_by_auth(node,G_def): # this funcion create a plot that represented the principal node (input author) and 
#the nodes that are connected with it until d_i level from the hop distance. the colors of the node represented the 
#difference level of the hop distance and the size of the node rapresent the number of the edges of each nodes.
def create_plot_shorter_path(G,tup_node): # this function create a plot that rapresent the shortest path between two nodes. 
#Each node has a label that represent the name of the author, the cost of the shortest path in the subtitle.
```




