class SingleLinkage:
    
    def __init__(self, x, k):
        '''Cluster points in k clusters'''
        self.data = x
        self.clusters = {i : [i] for i in range(x.shape[0])}
        while len(self.clusters)>k:
            self.merge(self.findClosest()[0],self.findClosest()[1])
        self.clusters={i:sorted(dict(enumerate(self.clusters.values()))[i]) for i,j in dict(enumerate(self.clusters.values())).items()}

    def euc(self, x, y):
        return np.sqrt(np.sum((x-y)**2))
        
    def clustDist(self, i, j):
        '''Returns the distance between cluster i and j,
        by definition: the distance between their closest pair'''
        return min(np.Inf, *[self.euc(self.data[idx], self.data[idy]) for idx in self.clusters[i] for idy in self.clusters[j]])
        
    def findClosest(self):
        '''Returns the indices of the closest clusters'''
        cd = np.Inf
        cc = None
        for i in self.clusters:
            for j in self.clusters:
                if i != j and self.clustDist(i, j) < cd:
                    cc = (i,j)
                    cd = self.clustDist(i, j)
        return cc

    def merge(self, i, j):
        '''Merge cluster i with cluster j'''
        self.clusters[i] += self.clusters[j]
        self.clusters.pop(j)
        
        

