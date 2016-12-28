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

## Read in graph file and build graph and weights dictionaries
script, filename = argv

main_graph = {}
main_weights = {}

with open(filename, 'r') as file:
    for line in file:
        if not line[0] == '#':    
            node_a, node_b, weight = re.split(',', line)
            for direction in [(node_a, node_b),(node_b, node_a)]:
                if not main_graph.has_key(direction[0]):
                    main_graph[direction[0]] = [direction[1]]
                else:
                    main_graph[direction[0]] += [direction[1]]
                main_weights[direction] = int(weight.strip())

print "graph: " + str(main_graph)
print "weights: " + str(main_weights)

longest = find_longest_trail(main_graph, main_weights)

print "Longest trail: " + str(longest[0])
print "Distance: " + str(longest[1])
