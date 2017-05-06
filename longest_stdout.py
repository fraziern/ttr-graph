###
# Provides interface between find_longest_trail and stdout, for node spawn
###

from longest4 import find_longest_trail
import sys, json

# read in graph description file from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    main_graph = {}

    # helps us add weights and edges in both directions
    def bidirections(nodes):
        return [(nodes[0], nodes[1]), (nodes[1], nodes[0])]

    lines = read_in()

    for route in lines['routes']:
        for direction in bidirections(route.values()):
            if not main_graph.has_key(direction[0]):
                main_graph[direction[0]] = [direction[1]]
            else:
                main_graph[direction[0]] += [direction[1]]

    # run algorithm, get response
    longest = find_longest_trail(main_graph)

    # send JSON to stdout
    json_output = { 'trail': longest[0], 'length': longest[1]}
    print json.dumps(json_output)

#start process
if __name__ == '__main__':
    main()
