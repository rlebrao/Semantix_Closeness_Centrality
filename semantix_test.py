import operator
dataset = open("edges.dat", "r")
graph = {}
for line in dataset:
    firstCollumn, secondCollumn = line.split()
    if firstCollumn not in graph:
        graph[firstCollumn] = {}
        graph[firstCollumn][secondCollumn] = {}
    else:
        graph[firstCollumn][secondCollumn] = {}

    if secondCollumn not in graph:
        graph[secondCollumn] = {}
        graph[secondCollumn][firstCollumn] = {}
    else:
        graph[secondCollumn][firstCollumn] = {}

def ClosenessCentrality(grafo, u=None):
    closeness_centrality = {}
    vertex = []
    i = 0
    for key, value in grafo.items():
        vertex.append(key)
    
    for n in vertex:
        dictShortestPath = findShortestPath(grafo,n)
        totalPath = sum(dictShortestPath.values())
        if totalPath > 0.0 and len(grafo) > 1:
            closeness_centrality[n] = (len(dictShortestPath)-1.0) / totalPath
            s = (len(dictShortestPath)-1.0) / ( len(grafo) - 1 )
            closeness_centrality[n] *= s
        else:
            closeness_centrality[n] = 0.0
    if u is not None:
        return closeness_centrality[u]
    else:
        return closeness_centrality

def findShortestPath(graph,source):
    visited={}                  
    level=0               
    nextlevel={source:1}  
    while nextlevel:
        actuallevel=nextlevel  
        nextlevel={}         
        for v in actuallevel:
            if v not in visited:
                visited[v]=level 
                nextlevel.update(graph[v]) 
        level=level+1
    return visited  
ccValue = ClosenessCentrality(graph)
sort = sorted(ccValue.items(),key=operator.itemgetter(-1))
for i in sort:
    print(i)
exit()
