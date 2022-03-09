from sqlite3 import IntegrityError
import networkx as nx
import os, os.path, sys
import numpy
# for folder in os.listdir(os.getcwd() + '\\exercise1'):
#     for net in os.listdir(os.getcwd() + "\\exercise1\\" + folder):
#         g = nx.read_pajek(os.getcwd() + "\\exercise1\\" + folder + "\\" + net)
#         print("****STARTING GRAPH " + net +"****")
#         ### PART 1 - MAIN DESCRIPTORS ###
#         # Number of nodes
#         print("\tNumber of nodes: " + str(nx.number_of_nodes(g)))
#         # Number of edges
#         print("\tNumber of edges: " + str(nx.number_of_edges(g)))
#         # Minimum, maximum, and average degree
#         min=sys.maxint
#         max=0
#         average=0
#         # nodes=nx.nodes(g)
#         degrees = [val for (node, val) in g.degree()]
#         for n in degrees:
#             if n < min:
#                 min = n
#             if n > max:
#                 max = n
#             average+=n
#         average /= float(nx.number_of_nodes(g))
#         print("\tMaximum degree: " + str(max))
#         print("\tMinimum degree: " + str(min))
#         print("\tAverage degree: " + str(average))
#         # Average clustering coefficient (average of the clustering coefficient of each node)
#         # print("\tAverage clustering coefficient: " + str(nx.average_clustering(g)))
#         # # Assortativity
#         print("\tAssortavility: " + str(nx.degree_assortativity_coefficient(g)))
#         # Average path length (average distance between all pairs of nodes)
#         # PROBLEMS!! I think that's a ntwrkx bug...
#         try:
#             print("\tAverage path length: " + str(nx.average_shortest_path_length(g)))
#         except Exception:
#             pass
#         # # Diameter (maximum distance between nodes in the network)
#         print("\tDiameter: " + str(nx.diameter(g)))

### PART 2 - DESCRIPTORS OF NODES IN AIRPORTS NET
g = nx.read_pajek('exercise1/real/airports_UW.net')
g = nx.Graph(g)
name_airports=[u'PAR', u'LON', u'FRA', u'AMS', u'MOW', u'NYC', u'ATL', u'BCN', u'WAW', u'CHC', u'DJE', u'ADA', u'AGU', u'TBO', u'ZVA']
for name in name_airports:
    print("*****STARTING NODE    " + name + " ******")
    # # Degree
    # print("\tDegree: " + str(nx.degree(g, name)))
    # # Strength
    # print("\tStrength: " + str(nx.degree(g, name, weight='weight')))
    # # Clustering coefficient
    print("\tClustering coefficient: " + str(nx.clustering(g,name)))
    # # Average path length (average distance to the rest of the nodes)
    # length_dict = nx.single_source_shortest_path_length(g, name)
    # print("\tAverage path length: " + str(sum(list(length_dict.values()))/float(len(length_dict))))#need to be reduced
    # # Maximum path length (maximum distance to the rest of the nodes)
    # print("\tMinimum path length: " + str(min(list(length_dict.values()))))
    # # Betweenness
    # print("\tBetweenness: " + str(nx.betweenness_centrality(g).get(name)))
    # Eigenvector centrality
    print("\tEigenvector centrality: " + str(nx.eigenvector_centrality(g).get(name)))
    # PageRank
    print("\tPageRank: " + str(nx.pagerank(g).get(name)))
    