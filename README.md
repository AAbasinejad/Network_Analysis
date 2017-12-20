# CS-Network
Repository for Homework __4__ of Algorithmic Methods for Data Mining - *__Group 1__*.

__Introduction__: Carry out some information from Computer Scientists network by applying the [Graph methods](https://networkx.github.io/).

__Data__: In this project we've used the [DBLP](http://dblp.uni-trier.de/) dataset. during the project we worked on two json file, [*__full_dblp__*](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/full_dblp.json.zip ) json file, which needs to be parsed and contains the entire network, and  [*__reduced_dblp__*](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/reduced_dblp.json.zip) json file for testing and debugging, which needs to be parsed and contains a portion of the network.

In root directory run:

`python main.py <reduced_data> <exercise_number> <exercise_letter>`

* __First Argument__: it can be *reduced* if you want to use the __reduced_dblp__ dataset or *full* if you want to use __full_dblp__.
* __Second Argument__: it can be *1* (just to make graph), *2* (just to run second part of the task) or *3* (just to run Third part of the task)
* __Third Argument__: it can be *a* or *b* (only if the second Argument is *2* and *3*, for each part of them)

__Modules__:

* [*__`main.py`__* ](https://github.com/AAbasinejad/CS-Network/blob/master/main.py): 

This file is the main corpus of the project, and it is to initialize and call another functions, which will explain in following.

* [*__`Graph.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Graph.py):

By processing JSON file create a graph, G, whose nodes are the authors. Two nodes are connected if they have at least one publication in common. Each edge is weighted in the following way:
<d1>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?w(a_1,a_2)&space;=&space;1&space;-&space;J(p_1,&space;p_2)" title="Weight Formula" width="200"/>
</p>
</d1>

> where a1, a2 are authors, p1 and p2 are the set of publication of the two authors and, J(p1 , p2) represents the jaccard similarity between these two sets of publications.
```python
def create_graph(inf_data): #which is to create a graph's nodes without edges, (this function must be called with a loaded #json dataset file as a argument)
def add_edges(inf_data,graph): #which is used to create weighted graph's edges, (this must be called with a loaded json 
#dataset and the results nodes of previous function.
```
in following way:
``` python
with open('reduced_dblp.json') as json_data
    data = json.load(json_data)
G = Graph.create_graph(data)
Graph.add_edges(data,G)
```

* [*__`Arisnumber.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Arisnumber.py): 

This file contain a class named `class Shortest_Path():` which is used to find the weight of the shortest path that connects the input author with [Aris](http://aris.me/) and the group number of each node of graph, using a given set of author. this class contain several function:
```python
def __init__(self, graph): # for Initialization
def create_dict_connection(self): # Function to make a dictionary that nodes appears as keys and tuples of connected nodes to 
#each key as values in this form: ("connected node", "weight")
def path_list(path,lst_path): # this function is to made a list which contain a path between each two connected node.
def dijkstrapath(self,start): # to calculate the shortes distance between an author and the others nodes, using heap.
def GroupNumber(self,set_id_author): # Dictionary with all shortest paths for the nodes of the input set.
```

* [*__`GenericFunctions.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/GenericFunctions.py):

File contains just three generic functions, `clean_name` to cleaning the names, `jaccard_similarity` to calculate jaccard_similarity between two lists, `Id_name` to convert the author's id in corresponding author's name.

* [*__`Hopdistance.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/Hopdistance.py): 

Contain a class named `Hop_Dist` This class finds all nodes that have hop distance at most equal to an integer d, starting from an input node, which both given by the user. It also contain several functions:
```python
def connect(self,lst_node,step): # Recursive function to calculate the hop distance, when the number of step is more than 1
def hop_distance(self,step, node): # Function to calculate the hop distance of a specific input author for the 3 main situations
```

* [*__`plot.py`__*](https://github.com/AAbasinejad/CS-Network/blob/master/plot.py): 

Contain several functions to Plot results of the project using `matplotlib.pyplot` and `matplotlib.patches`. (Detaied Explaination about Plot will be added)

