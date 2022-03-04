import networkx as nx
g = nx.read_pajek('circle9.net')
nx.number_of_nodes(g)

### PART 1 - MAIN DESCRIPTORS ###
# Number of nodes
nx.number_of_nodes(g)
# Number of edges
nx.number_of_edges(g)
# Minimum, maximum, and average degree
for n in nx.nodes(g):
    nx.degree()
    ...
# Average clustering coefficient (average of the clustering coefficient of each node)
nx.average_clustering(g)
# Assortativity
nx.degree_assortativity_coefficient(g)
# Average path length (average distance between all pairs of nodes)
nx.average_shortest_path_length(g)
# Diameter (maximum distance between nodes in the network)
nx.diameter(g)

### PART 2 - DESCRIPTORS OF NODES IN AIRPORTS NET
name_airports=['PAR', 'LON', 'FRA', 'AMS', 'MOW', 'NYC', 'ATL', 'BCN', 'WAW', 'CHC', 'DJE', 'ADA', 'AGU', 'TBO', 'ZVA']
for name in name_airports:
    # n = ...get node by name
    # Degree
    nx.degree(g, n)
    # Strength
    nx.degree(g, weight='weight')
    # Clustering coefficient
    nx.clustering(g, n)
    # Average path length (average distance to the rest of the nodes)
    nx.single_source_shortest_path_length(g, n)#need to be reduced
    # Maximum path length (maximum distance to the rest of the nodes)
    nx.single_source_shortest_path_length(g, n)#need to be reduced
    # Betweenness
    nx.betweenness_centrality(g)#???? - catch value for n
    # Eigenvector centrality
    nx.eigenvector_centrality(g)#???? - catch value for n
    # PageRank
    nx.pagerank(g)#???? - catch value for n