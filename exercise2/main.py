import networkx as nx
import matplotlib.pyplot as plt
import random
from numpy.random import choice
import numpy as np

random.seed(10)

#ER networks
N_list = [10, 50, 100, 1000]
factor=5000

# Random graph generation specifiying 
#   N: number of nodes
#   K: number of (random) edges
def ER_graph(N, k):
    g = nx.empty_graph(N)
    for _ in range(k):
        while True:
            node1=random.randint(0,N-1)
            node2=random.randint(0,N-1)
            if not g.has_edge(node1,node2):
                g.add_edge(node1, node2)
                break
    return g

if __name__=='__main__':
# -------------- ER networks ---------------------
    for N in N_list:
        max_k=N*(N-1)/2
        list_k=[max_k/(N*2), max_k/N, max_k*2/N]
        for k in list_k:
            g = ER_graph(N, k)  
            pos=nx.random_layout(g) 
            nx.draw(g,pos,node_size=factor/N)
            plt.show()

# --------------- BA networks --------------------
    list=[{'N': 100, 'm0': 10, 'm':4},{'N': 500, 'm0': 50, 'm':10},{'N': 1000, 'm0': 100, 'm':13}]
    for dict in list:
        #GENERATE RANDOM GRAPH
        N=dict.get('N')
        m0=dict.get('m0')
        m=dict.get('m')
        K=m0*(m0-1)*20/N
        g=ER_graph(m0,K)
        #BEGIN TO GROW THE GRAPH
        for node_to_add in range(m0, N):
            for edge in range (0,m):
                while True:
                    nodes = [node for (node, val) in g.degree()]
                    degrees = [val for (node, val) in g.degree()]
                    suma=sum(degrees)
                    degrees=np.array(degrees)/float(suma)
                    selected_node=choice(nodes, 1, p=degrees)[0]
                    print(type(selected_node))
                    if not g.has_edge(selected_node,node_to_add):
                        g.add_edge(selected_node, node_to_add)
                        break
        #SHOW GRAPH DATA
        pos=nx.random_layout(g) 
        nx.draw(g,pos,node_size=factor/N)
        plt.show()
        print(g.degree())




