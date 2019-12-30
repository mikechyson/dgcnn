from config import model2graph as config
import numpy as np
from utils.utils import distance
import pandas as pd


def index_position(lst, sep):
    pos_dict = dict()
    for no, p in enumerate(lst):
        value = p.split(sep)
        value = [float(v) for v in value]
        # value = np.array(value) #
        pos_dict[no] = value
    return pos_dict


def faces2graph(pos_dict, faces):
    """
    Convert indices list to graph
    :param pos_dict: position directory
    :param faces: 3D object faces
    :return:
    """
    # vertices_list = []
    graph = {}
    for face in faces:
        lst = face.split(config.off_sep)
        num_edges = int(lst[0])
        edges = lst[1:]

        # # for vertices statistics
        # vl = [int(v) for v in edges]
        # # vl=edges
        # vertices_list.extend(vl)

        for e in range(num_edges):
            idx1 = int(edges[e])
            idx2 = int(edges[(e + 1) % num_edges])

            # remove the duplicated lines like (1,0) and (1,0) are the same line.
            # reserving one line line (0,1)
            if idx1 > idx2:
                tmp = idx1
                idx1 = idx2
                idx2 = tmp

            graph['({},{})'.format(idx1, idx2)] = distance(np.array(pos_dict[idx1]), np.array(pos_dict[idx2]))

    # print(vertices_list)
    # table = pd.DataFrame(vertices_list)
    # for row in vertices_list:
    # print(row)
    # print(table.describe())
    # uni = set(vertices_list)

    # for u in sorted(list(uni)):
    #     print("vertex index: {} with count: {}".format(u, vertices_list.count(u)))

    return graph


def faces2graph_list(pos_dict, faces):
    """
    Convert indices list to graph
    :param pos_dict: position directory
    :param faces: 3D object faces
    :return:
    """
    graph = {}
    for face in faces:
        lst = face.split(config.off_sep)
        num_edges = int(lst[0])
        edges = lst[1:]

        for e in range(num_edges):
            idx1 = int(edges[e])
            idx2 = int(edges[(e + 1) % num_edges])

            # remove the duplicated lines like (1,0) and (1,0) are the same line.
            # reserving one line line (0,1)
            if idx1 > idx2:
                tmp = idx1
                idx1 = idx2
                idx2 = tmp

            graph['{},{}'.format(idx1, idx2)] = distance(np.array(pos_dict[idx1]), np.array(pos_dict[idx2]))

    return graph


def save_list(filename, graph):
    with open(filename, 'w') as fh:
        for i in graph:
            print(i, graph[i])
            fh.write(config.graph_sep.join([i, str(graph[i])]))
            fh.write('\n')
