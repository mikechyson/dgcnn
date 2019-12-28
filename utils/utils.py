import numpy as np
import json


def index_position(pos, dimension):
    """
    Convert a list of positions into a directory.

    :param pos: position list
    :param dimension: dimension of the space
    :return: a directory whose key is a index start from 0, whose value is the spatial position
    """
    if len(pos) % dimension != 0:
        print('Error! The length of the positions must be a multiply of {}'.format(dimension))
        return None
    pos_dict = dict()
    for i in range(0, len(pos), dimension):
        pos_dict[i // dimension] = pos[i:i + dimension]
    return pos_dict


def distance(point1, point2):
    """
    Compute the distance of two points.
    :param point1:
    :param point2:
    :return:
    """
    return np.linalg.norm(point1 - point2)


def indices2graph(pos_dict, indices, circle):
    """
    Convert indices list to graph
    :param pos_dict: position directory
    :param indices: indices of lines two end points
    :param circle: how man indices from a circle
    :return:
    """
    if len(indices) % circle != 0:
        print('Error! The length of the indices must be a multiply of {}'.format(circle))
        return None

    graph = dict()

    for i in range(0, len(indices), circle):
        for j in range(circle):
            idx1 = indices[i + j]
            idx2 = indices[i + (j + 1) % circle]

            if idx1 > idx2:
                tmp = idx1
                idx1 = idx2
                idx2 = tmp

            graph['({},{})'.format(idx1, idx2)] = distance(np.array(pos_dict[idx1]), np.array(pos_dict[idx2]))
    return graph


def save_json(filename, dict_):
    with open(filename, 'w') as f:
        json.dump(dict_, f)
