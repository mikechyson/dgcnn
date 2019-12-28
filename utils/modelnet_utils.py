from config import model2graph as config
import numpy as np
from utils.utils import distance


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

            graph['({},{})'.format(idx1, idx2)] = distance(np.array(pos_dict[idx1]), np.array(pos_dict[idx2]))
    return graph
