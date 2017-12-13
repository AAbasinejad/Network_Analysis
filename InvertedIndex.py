import json
fred = open('reduced_dblp.json', 'r')
reduceddata = fred.read()
fred.close()
dataset_reduced = json.loads(reduceddata)
def InvertedInd(data):
    invind = {}
    for item in dataset_reduced:
        for a in item['authors']:
            aid = a['author_id']
            if aid in invind.keys():
                invind[aid] += [item['id_publication_int']]
            else:
                invind[aid] = [item['id_publication_int']]
    return invind

InvInd = InvertedInd(dataset_reduced) 
                
