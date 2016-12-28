from sys import argv
import re

script, filename, start, end = argv

dict_x = {}

with open(filename, 'r') as file:
    for line in file:
        node, raw_destinations = re.split(':', line)
        destinations = re.split(',', raw_destinations.strip())
        print node + " -> " + ','.join(destinations)
        dict_x[node] = destinations

# print dict_x

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    best_path = []
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if best_path == [] or (
                len(newpath) > 0 and len(newpath) < len(best_path)):
                best_path = newpath
    return best_path

print find_shortest_path(dict_x, start, end)
