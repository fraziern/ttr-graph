# ttr-graph
## Python graph algorithms based on the board game "Ticket To Ride"

This houses my experiments with graph algorithms in Python, inspired by the board game "Ticket To Ride" (or "TTR").

Contents:
---------

*Longest Continuous Trail* (`ttr_longest_trail.py`)
This Python script accepts one command line argument - the filename for a graph definition file. It outputs the longest continuous "trail" (where no edge can be repeated, per TTR rules) found in the input graph.

This uses a brute-force algorithm, as the longest path/trail problem is NP-hard for non-Eulerian graphs (as I understand it).

To run:

`$ python ttr_longest_trail.py weights.txt my_routes.json`

*Graph Definition File* (sample included at `my_routes.json`)
This file defines the edges of the graph to analyze, and must be a subgraph of the graph defined in the weights file. In other words, it should be a valid set of TTR routes. This is a JSON file of the format (for example):

```
{
    "routes": [
        {"node1": "Los Angeles", "node2": "Phoenix"},
        {"node1": "El Paso", "node2": "Phoenix"},
        {"node1": "El Paso", "node2": "Los Angeles"},
        {"node1": "El Paso", "node2": "Santa Fe"},
        {"node1": "Denver", "node2": "Santa Fe"}
    ]
}
```

*Weights Definition File* (`weights.txt`)
This file defines a undirected weighted graph, with the following format:

 1. Each line defines one edge
 2. An edge is defined using the syntax `node1,node2,weight`
 3. Lines starting with a `#` are considered comments and are ignored

The current iteration of `graph.txt` contains *all* the edges in TTR.

Everything else right now is an experimental test or a utility.

Roadmap:
--------

Short term/long term goals:

- [x] Accept JSON list of edges (without weights) as input. Weights are pre-stored since they never change.
- [ ] Create a Flask API for the algorithms
- [ ] Create a front-end site UI that allows graphical path selection and display
- [ ] Add shortest path algorithm(s)
- [ ] Add score calculator (i.e. input your routes and get your TTR score)
- [ ] Optimize longest trail algorithm using multithreading, memoization, etc
