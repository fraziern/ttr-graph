from sys import argv
from timer import Timer
import json
import re
import weights

def _edge_has_been_visited(path, edge):
    # assert len(edge) == 2
    last_index = len(path) - 1
    for idx, node in enumerate(path):
        if node == edge[0]:
            if idx > 0 and path[idx-1] == edge[1]:
                return True
            elif idx < last_index and path[idx+1] == edge[1]:
                return True
    return False

def _max_distance(newpath_data, longest_newpath_data):
    if newpath_data:
        if newpath_data[1] > longest_newpath_data[1]:
            return newpath_data
    return longest_newpath_data

def trail_distance(trail, weights):
    distance = 0
    for idx in range(0,len(trail)-1):
        edge = (trail[idx],trail[idx+1])
        # assert weights.has_key(edge)
        distance += weights[edge]
    return distance

def find_long_trail(graph, weights, start, path=()):
    """
    This is a recursive function, which traverses a graph and returns the
    heaviest edge-simple trail (or one of the heaviest, if some are equivalent).
    It requires a starting node.

    weights: a dict of the form {('a','b'): 5, ('b','a'): 5}. In an undirected
    graph each direction should be listed.

    graph: a dict of the form {'a': ['b'], 'b': ['a']}. In an undirected graph
    each direction should be listed.

    This version returns a tuple (trail, precomputed_distance).
    """
    path = path + (start,)
    if not graph.has_key(start):
        return None
    longest_newpath_data = ((),0)   # path and distance
    for node in graph[start]:
        if not _edge_has_been_visited(path, [start, node]):
            newpath_data = find_long_trail(graph, weights, node, path)
            longest_newpath_data = _max_distance(
                newpath_data, longest_newpath_data)
    if longest_newpath_data == ((),0):
        return path, trail_distance(path, weights)
    return longest_newpath_data


def find_longest_trail(graph, weights=weights.weights):
    longest_trail_data = ((),0)  # path and distance
    for node in graph.keys():
        newtrail_data = find_long_trail(graph, weights, node)
        longest_trail_data = _max_distance(
            newtrail_data, longest_trail_data)
    return longest_trail_data

###
# TESTS
###

# def test_find_longest_trail(graph, weights):
#     longest_trail = []
#     longest_trail_distance = 0
#     newtrail = find_long_trail(graph, weights, 'A')
#     return (newtrail, trail_distance(newtrail, weights))

# def test_trail_distance():
#     assert trail_distance(['A','B','C','F'], weights) is 10

###
# MAIN
#   graph_file: json graph description file name. See example.
###

def main(graph_file):

    main_graph = {}

    # helps us add weights and edges in both directions
    def bidirections(nodes):
        return [(nodes[0], nodes[1]), (nodes[1], nodes[0])]

    # Read file, build graph dict
    with open(graph_file, 'r') as file:
        json_graph = json.loads(file.read())

    for route in json_graph['routes']:
        for direction in bidirections(route.values()):
            if not main_graph.has_key(direction[0]):
                main_graph[direction[0]] = [direction[1]]
            else:
                main_graph[direction[0]] += [direction[1]]

    # run algorithm
    with Timer() as t:
        longest = find_longest_trail(main_graph)

    print "Longest trail: " + str([city.encode('utf-8') for city in longest[0]])
    print "Distance: " + str(longest[1])
    print "Calculated in {} s".format(t.secs)

if __name__ == "__main__":
    main(argv[1])
