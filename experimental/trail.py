from sys import argv
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

# test_path = ['A','B','D','C']
# test_edge_1 = ['D','B']
# assert edge_has_been_visited(test_path, test_edge_1) is True
# test_edge_2 = ['A','B']
# assert edge_has_been_visited(test_path, test_edge_2) is True
# test_edge_3 = ['A','D']
# assert edge_has_been_visited(test_path, test_edge_3) is False

def find_trails(graph, start, path=[]):
    path = path + [start]
    if not graph.has_key(start):
        return None
    paths = []
    for node in graph[start]:
        if not edge_has_been_visited(path, [start, node]):
            newpaths = find_trails(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    # if dead_end:
    if paths == []:
        return [path]
    return paths

def find_all_trails(graph):
    # go through each node in graph, check each trail, return them
    trails = []
    for node in graph.keys():
        newtrails = find_trails(graph, node)
        if newtrails:
            trails = trails + newtrails
    return trails

# MAIN #
########
script, filename = argv

graph = {}

# read graph file and create graph
with open(filename, 'r') as file:
    for line in file:
        node, raw_destinations = re.split(':', line)
        destinations = re.split(',', raw_destinations.strip())
        # print node + " -> " + ','.join(destinations)
        graph[node] = destinations

print find_all_trails(graph)
