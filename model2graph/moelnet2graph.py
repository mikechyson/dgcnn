import http.client
import argparse
import config.model2graph as config
import json
from utils import utils

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help='model file (.off)')
args = vars(parser.parse_args())

PREFIX = 'OFF'

file = open(args['file'])
