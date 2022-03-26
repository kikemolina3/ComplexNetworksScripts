import csv
import networkx as nx
import os, os.path, sys
import numpy
import statistics

### PART 1 - DESCRIPTORS OF GRAPHS
FILE1HEADER = ['Graph name', 'Number of nodes', 'Number of edges', 'Minimum degree', 'Maximum degree', 'Average degree', 'Avg clustering coefficient', 'Assortativity', 'Average path length', 'Diameter']
GENERALIST = []
for folder in os.listdir(os.getcwd()):
    for net in os.listdir(os.getcwd() + "\\" + folder):
        GRAPHLIST = []
        g = nx.read_pajek(os.getcwd() + "\\" + folder + "\\" + net)
        g = nx.Graph(g)
        GRAPHLIST.append(net)
        GRAPHLIST.append(str(nx.number_of_nodes(g)))
        GRAPHLIST.append(str(nx.number_of_edges(g)))
        degrees = [val for (node, val) in g.degree()]
        GRAPHLIST.append(str(min(degrees)))
        GRAPHLIST.append(str(max(degrees)))
        GRAPHLIST.append(str(sum(degrees)/float(len(degrees))))
        GRAPHLIST.append(str(nx.average_clustering(g)))
        GRAPHLIST.append(str(nx.degree_assortativity_coefficient(g)))
        GRAPHLIST.append(str(nx.average_shortest_path_length(g)))
        GRAPHLIST.append(str(nx.diameter(g)))
        GENERALIST.append(GRAPHLIST)
with open('part1.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(FILE1HEADER)
    csvwriter.writerows(GENERALIST)

### PART 2 - DESCRIPTORS OF NODES IN AIRPORTS NET
g = nx.read_pajek('real/airports_UW.net')
g = nx.Graph(g)
gW = g.copy()
nx.set_edge_attributes(g, 1, 'weigth')
GENERALIST=[]
FILE2HEADER = ['Node name', 'Degree', 'Strength', 'Clustering coefficient', 'Average path length', 'Maximum path length', 'Betweenness', 'Eigenvector centrality', 'PageRank']
BETWEENNESS = [str(x) for x in list(nx.betweenness_centrality(g).values())]
EIGENVECTORS = [str(x) for x in list(nx.eigenvector_centrality(g).values())]
PAGERANK = [str(x) for x in list(nx.pagerank(g).values())]
NAMES = []  
DEGREES = []
STRENGTHS = []
CLUSTRCOFF = []
AVGPHLNG = []
MAXPHLNG = [] 
for name in nx.nodes(g):
    print(name)
    NAMES.append(name)
    DEGREES.append(str(nx.degree(g, name)))
    STRENGTHS.append(str(nx.degree(gW, name, weight='weight')))
    CLUSTRCOFF.append(str(nx.clustering(g,name)))
    length_dict = nx.single_source_shortest_path_length(g, name)
    AVGPHLNG.append(str(statistics.mean(length_dict.values())))
    MAXPHLNG.append(str(max(list(length_dict.values()))))
GENERALIST = [NAMES, DEGREES, STRENGTHS, CLUSTRCOFF, AVGPHLNG, MAXPHLNG, BETWEENNESS, EIGENVECTORS, PAGERANK]
GENERALIST=list(map(list, zip(*GENERALIST)))
with open('part2.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(FILE2HEADER)
    csvwriter.writerows(GENERALIST)