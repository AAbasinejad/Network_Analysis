import re
import html
# Function to clean the name
def clean_name(name):
    name=html.unescape(name)
    return re.sub(r'[0-9]+','',name)

# Function to calculate jaccard similarity
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return (intersection_cardinality/float(union_cardinality))

def connect(lst_node,graph,di):
    if di==0:
        return lst_node
    connection=list({key for elem in lst_node for key in graph[elem].keys()})
    lst_node+=connection
    return connect(connection,graph,di-1)

def hope_distance(step, nde, grph):
    def_connection=[nde]
    if step==0:
        lst_connect=def_connection
    elif step==1:
        connection=list({key for key in grph[nde].keys()})
        lst_connect=def_connection+connection
    else:
        lst_connect=connect(def_connection,grph,step)  
    return(lst_connect)