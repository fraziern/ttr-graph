from longest3 import find_long_trail
import multiprocessing
from sys import argv
from timer import Timer
import json
import re

# TODO: Add Queue to make this work and use functions instead of running every-
#  thing in main

# def find_long_trail_closure(graph, weights):
#     def inner(node):
#         return find_long_trail(graph, weights, node)
#     return inner
#
# def find_longest_trail_multi(graph, weights):
#     find_node_trails = find_long_trail_closure(graph, weights)
#     pool = multiprocessing.Pool(processes=4)
#     trails = pool.map(find_node_trails, graph.keys())
#     return max(trails, key=lambda x: x[1])

###
# MAIN
###

if __name__ == "__main__":

    script, weights_file, graph_file = argv

    main_graph = {}
    main_weights = {}

    # helps us add weights and edges in both directions
    def bidirections(nodes):
        return [(nodes[0], nodes[1]), (nodes[1], nodes[0])]

    # Read files, build weights and graph dicts
    # Todo - make weights a JSON file too for consistency
    with open(weights_file, 'r') as file:
        for line in file:
            if not line[0] == '#':
                node_a, node_b, weight = re.split(',', line)
                for direction in bidirections([node_a, node_b]):
                    main_weights[direction] = int(weight.strip())

    with open(graph_file, 'r') as file:
        json_graph = json.loads(file.read())

    for route in json_graph['routes']:
        for direction in bidirections(route.values()):
            if not main_graph.has_key(direction[0]):
                main_graph[direction[0]] = [direction[1]]
            else:
                main_graph[direction[0]] += [direction[1]]

    # call find_long_trail with single argument using globals
    def find_trail_from_node(node):
        return find_long_trail(main_graph, main_weights, node)

    # run algorithm
    with Timer() as t:
        pool = multiprocessing.Pool(processes=4)
        trails = pool.map(find_trail_from_node, main_graph.keys())
        longest = max(trails, key=lambda x: x[1])

    print "Longest trail: " + str([city.encode('utf-8') for city in longest[0]])
    print "Distance: " + str(longest[1])
    print "Calculated in {} s".format(t.secs)
