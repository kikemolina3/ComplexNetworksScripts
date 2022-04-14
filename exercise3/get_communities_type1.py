import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import os
from definitions import files


def write_clu_file(community_list, filename):

    return 0


if __name__ == "__main__":
    for f in files:
        print('########################')
        print(f.get('net'))

        g = nx.read_pajek(os.getcwd() + '\\' + f.get('folder') + '\\' + f.get('net'))
        aux = dict(g.nodes(data='id'))
        for k, v in aux.iteritems():
            aux[k] = int(v)
        g = nx.relabel_nodes(g, aux)
        communities = greedy_modularity_communities(g)
        x = [list(x) for x in communities]
        t = {}
        for i in x:
            for j in i:
                t[j] = x.index(i) + 1
        with open(os.getcwd() + '\\type1\\'+ f.get('net')[:-4] + ".clu", 'w') as clue:
            clue.write('*Vertices ' + str(nx.number_of_nodes(g)) + '\n')
            for k, v in t.iteritems():
                clue.write(str(v) + '\n')
        # print(t)
