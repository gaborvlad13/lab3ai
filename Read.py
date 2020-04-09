import networkx as nx;
def readGML(fileName):
    net={}
    G=nx.read_gml(fileName);
    n=len(G.nodes())
    net['noNodes']=n
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(0)
    sol = list(G.nodes())
    for element in G.edges():
        mat[sol.index(element[0])][sol.index(element[-1])]=1
    net['mat']=mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    return net
