from sys import argv
from timer import Timer
import json
import re

def edge_has_been_visited(path, edge):
    """
    Given a path array (e.g. ['A','B','C']) and an edge array (e.g. ['B','A'])
    return true if the edge has been visited, false otherwise
    """
    assert len(edge) == 2
    last_index = len(path) - 1
    for idx, node in enumerate(path):
        if node == edge[0]:
            if idx > 0 and path[idx-1] == edge[1]:
                return True
            elif idx < last_index and path[idx+1] == edge[1]:
                return True
    return False

def trail_distance(trail, weights):
    distance = 0
    for idx in range(0,len(trail)-1):
        edge = (trail[idx],trail[idx+1])
        assert weights.has_key(edge)
        distance += weights[edge]
    return distance

def find_long_trail(graph, weights, start, path=[]):
    path = path + [start]
    if not graph.has_key(start):
        return None
    longest_newpath = []
    longest_newpath_distance = 0
    for node in graph[start]:
        if not edge_has_been_visited(path, [start, node]):
            newpath = find_long_trail(graph, weights, node, path)
            if newpath:
                newpath_distance = trail_distance(newpath, weights)
                if newpath_distance > longest_newpath_distance:
                    longest_newpath = newpath
                    longest_newpath_distance = newpath_distance
    if longest_newpath_distance == 0:
        return path
    return longest_newpath


def find_longest_trail(graph, weights):
    longest_trail = []
    longest_trail_distance = 0
    for node in graph.keys():
        newtrail = find_long_trail(graph, weights, node)
        if newtrail:
            newtrail_distance = trail_distance(newtrail, weights)
            if newtrail_distance > longest_trail_distance:
                longest_trail = newtrail
                longest_trail_distance = newtrail_distance
    return (longest_trail, longest_trail_distance)

def bidirections(nodes):
    return [(nodes[0], nodes[1]), (nodes[1], nodes[0])]

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
###

script, weights_file, graph_file = argv

main_graph = {}
main_weights = {}

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

# run algorithm
with Timer() as t:
    longest = find_longest_trail(main_graph, main_weights)

print "Longest trail: " + str([city.encode('utf-8') for city in longest[0]])
print "Distance: " + str(longest[1])
print "Calculated in {} s".format(t.secs)
