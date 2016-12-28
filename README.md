# ttr-graph
## Python graph algorithms based on the board game "Ticket To Ride"

This houses my experiments with graph algorithms in Python, inspired by the board game "Ticket To Ride" (or "TTR").

Contents:
---------

*Longest Continuous Trail* (`ttr_longest_trail.py`)
This Python script accepts one command line argument - the filename for a graph definition file. It outputs the longest continuous "trail" (where no edge can be repeated, per TTR rules) found in the input graph.

*Graph Definition File* (sample included at `weighted_graph.txt`)
This file defines a undirected weighted graph, with the following format:

 1. Each line defines one edge
 2. An edge is defined using the syntax `node1,node2,weight`
 3. Lines starting with a `#` are considered comments and are ignored


