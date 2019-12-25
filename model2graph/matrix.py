import json
import http.client
import argparse
import config.model2graph as config

# commandline argument
parse = argparse.ArgumentParser()
parse.add_argument('-k', '--key', required=True, help='component key')
args = vars(parse.parse_args())

conn = http.client.HTTPSConnection(config.bos_url)

headers = {
    'devcode': config.devcode,
    'cache-control': "no-cache",
}

conn.request("GET", "/components/{}/primary".format(args['key']), headers=headers)

res = conn.getresponse()
data = res.read()

json_string = data.decode(config.encoding)
json_obj = json.loads(json_string, encoding=config.encoding)

# affine matrix of the 3D component
matrix = json_obj['data'][config.matrix]
print(matrix)
