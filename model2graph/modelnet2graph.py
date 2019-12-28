import argparse

from chyson.io import json as my_json

import config.model2graph as config
from utils import modelnet_utils

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help='model file (.off)')
args = vars(parser.parse_args())

PREFIX = 'OFF'

fh = None
fh = open(args['file'], 'r', encoding=config.encoding)

lines = fh.read().rstrip().split('\n')

# vertices faces edges
vfe = lines[1].rstrip()
num_vertices = int(vfe.split(config.off_sep)[0])

vertices = lines[config.vertex_start:config.vertex_start + num_vertices]
pos_dict = modelnet_utils.index_position(vertices, config.off_sep)
# print(pos_dict)

faces = lines[config.vertex_start + num_vertices:]
# print(faces)
# print(len(faces))

graph = modelnet_utils.faces2graph(pos_dict, faces)
# print(graph)
# print(len(graph.keys()))

my_json.save('modelnet_table.json', graph)
