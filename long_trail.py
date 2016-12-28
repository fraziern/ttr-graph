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

def find_long_trail(graph, start, path=[]):
    # In this call we first add our current node to the current path
    path = path + [start]
    # If the current node does not exist, there's a problem. Return nothing
    if not graph.has_key(start):
        return None
    longest_newpath = []
    for node in graph[start]:
        if not edge_has_been_visited(path, [start, node]):
            # go off on the next node, see where it leads
            newpath = find_long_trail(graph, node, path)
            # if its the longest path we have so far, save it
            if newpath and len(newpath) > len(longest_newpath):
                longest_newpath = newpath
    # if dead_end:
    if longest_newpath == []:
        return path
    return longest_newpath

def find_longest_trail(graph):
    # go through each node in graph, check each trail, return them
    longest_trail = []
    for node in graph.keys():
        newtrail = find_long_trail(graph, node)
        if newtrail and len(newtrail) > len(longest_trail):
            longest_trail = newtrail
    return longest_trail

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

print find_longest_trail(graph)
