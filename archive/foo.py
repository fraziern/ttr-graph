from sys import argv
import re

script, weights_file = argv

with open(weights_file, 'r') as file:
    for line in file:
        if not line[0] == '#':
            node_a, node_b, weight = re.split(',', line)
            print("({}, {}): {},".format(node_a, node_b, weight.strip()))
            print("({}, {}): {},".format(node_b, node_a, weight.strip()))
