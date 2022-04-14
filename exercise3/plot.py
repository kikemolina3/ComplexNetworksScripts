import networkx as nx
import os, os.path, sys
import matplotlib.pyplot as plt
from networkx.utils import open_file
from collections import defaultdict
import random
from numpy.random import choice
import numpy as np

from definitions import colors, files

@open_file(0, mode='rb')
def read_pajek_clu(path, encoding='UTF-8'):
    lines = (line.decode(encoding) for line in path)
    return parse_pajek_clu(lines)


def parse_pajek_clu(lines):
    communities = None
    if isinstance(lines, str):
        lines = iter(lines.split('\n'))
    lines = iter([line.rstrip('\n') for line in lines])

    while lines:
        try:
            l = next(lines)
        except:  # EOF
            break
        if l.lower().startswith("*vertices"):
            l, nnodes = l.split()
            communities = defaultdict(list)
            for vertice in range(1, int(nnodes) + 1):
                l = next(lines)
                community = int(l)
                communities.setdefault(community, []).append(vertice)
        else:
            break

    return [v for k, v in dict(communities).items()]


if __name__ == "__main__":

    for f in files:
        g = nx.read_pajek(os.getcwd() + '\\' + f.get('folder') + '\\' + f.get('net'))
        aux = dict(g.nodes(data='id'))
        for k, v in aux.iteritems():
            aux[k] = int(v)
        g = nx.relabel_nodes(g, aux)
        if f.get('coords'):
            list_x = nx.get_node_attributes(g, 'x')
            list_y = nx.get_node_attributes(g, 'y')
            pos = {}
            for k, v in dict.iteritems(list_x):
                pos[k] = np.array([v, list_y[k]])
        else:
            pos = nx.spring_layout(g)
        print(pos)
        for c in f.get('clu'):
            clu = read_pajek_clu(os.getcwd() + '\\' + f.get('folder') + '\\' + c)
            fig, axe = plt.subplots(figsize=(12, 7))
            axe.set_title(f.get('net') + ' - ' + c, loc='right')
            nx.draw(g, pos,  edge_color='k', with_labels=True, font_weight='light',
                    node_size=280, width=0.7, font_size=8)
            for community in clu:
                nx.draw_networkx_nodes(g, pos, nodelist=community, node_color=colors[clu.index(community)])
            plt.show()
        for c in range(1, 4):
            clu_filename = f.get('net')[:-4] + '.clu'
            clu = read_pajek_clu(os.getcwd() + '\\type' + str(c) + '\\' + clu_filename)
            fig, axe = plt.subplots(figsize=(12, 7))
            axe.set_title(f.get('net') + ' - ' + clu_filename[:-4] + '-type' + str(c) + '.clu', loc='right')
            nx.draw(g, pos, edge_color='k', with_labels=True, font_weight='light',
                    node_size=280, width=0.7, font_size=8)
            for community in clu:
                nx.draw_networkx_nodes(g, pos, nodelist=community, node_color=colors[clu.index(community)])
            plt.show()
