import http.client
import argparse
import config.model2graph as config
import json
from utils import utils

# commandline argument
parse = argparse.ArgumentParser()
parse.add_argument('-k', '--key', required=True, help='component key')
args = vars(parse.parse_args())

# get the http connection
conn = http.client.HTTPSConnection(config.bos_url)
headers = {
    'cache-control': "no-cache",
    'devcode': config.devcode,
}

# request the geometry content according to the component key
conn.request("GET", "/components/{}/geometry".format(args['key']), headers=headers)

res = conn.getresponse()
data = res.read()

json_string = data.decode(config.encoding)
json_obj = json.loads(json_string, encoding=config.encoding)
# print(len(json_obj[config.positions]))
# print(len(json_obj[config.indices]))

positions = json_obj[config.positions]
indices = json_obj[config.indices]

# get a directory, the key is the index from 0
# the value is the spatial point
pos_dict = utils.index_position(positions, config.dimension)
# print(pos_dict)

graph = utils.indices2graph(pos_dict, indices, config.circle)

utils.save_json('../data/graph.json', graph)
utils.save_json('../data/position.json', pos_dict)
utils.save_json('../data/geometry.json', json_obj)
