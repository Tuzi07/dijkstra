import csv
from graph_traverser import GraphTraverser
from node import Node
from edge import Edge


class Graph:
    def __init__(self, nodes_filepath, edges_filepath):
        self.nodes = {}
        self.number_of_nodes = 0
        self.number_of_edges = 0
        self.nodes_filepath = nodes_filepath
        self.add_nodes_from_csv(nodes_filepath)
        self.add_edges_from_csv(edges_filepath)

    def add_nodes_from_csv(self, nodes_filepath):
        with open(nodes_filepath, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.add_node(row[0])

    def add_node(self, node):
        if node in self.nodes:
            print("This node already exists")
        else:
            self.nodes[node] = Node()
            self.number_of_nodes += 1

    def add_edges_from_csv(self, edges_filepath):
        with open(edges_filepath, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # self.add_edge(origin=row[0], destiny=row[1], weight=row[2])
                self.add_directed_edge(origin=row[0], destiny=row[1], weight=row[2])

    def add_edge(self, origin, destiny, weight):
        if origin not in self.nodes or destiny not in self.nodes:
            print("Node does not exist")
        else:
            self.nodes[origin].neighbors[destiny] = Edge(weight=int(weight))
            self.nodes[destiny].neighbors[origin] = Edge(weight=int(weight))
            self.number_of_edges += 1

    def add_directed_edge(self, origin, destiny, weight):
        if origin not in self.nodes or destiny not in self.nodes:
            print("Node does not exist")
        else:
            self.nodes[origin].neighbors[destiny] = Edge(weight=int(weight))
            self.number_of_edges += 1

    def print_graph(self):
        for node in self.nodes:
            if len(self.nodes[node].neighbors) > 0:
                print(node, "-> ", end="")
                self.nodes[node].print_edges()
        print()

    def has_edge(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            return False
        if node1 == node2:
            return True
        return self.nodes[node1].is_adjacent(node2)

    def remove_edge(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            print("Node does not exist")
        else:
            self.nodes[node1].neighbors.pop(node2)
            self.nodes[node2].neighbors.pop(node1)
            self.number_of_edges -= 1

    def is_complete(self):
        from math import comb

        return self.number_of_edges == comb(self.number_of_nodes, 2)

    def dfs_count_from_node(self, node):
        visited_nodes = 1
        self.nodes[node].was_visited = True
        for neighbor in self.nodes[node].neighbors:
            if not self.nodes[neighbor].was_visited:
                visited_nodes += self.dfs_count_from_node(neighbor)
        return visited_nodes

    def traversed_graph_with_algorith_from_node(self, algorithm, source_node):
        self.traverse_with_algorithm_from_node(algorithm, source_node)
        traversed_graph = self.traversed_graph()
        return traversed_graph

    def traverse_with_algorithm_from_node(self, algorithm, source_node):
        self.reset_traversal()
        self.nodes[source_node].steps = 0
        self.nodes[source_node].distance = 0

        if algorithm == "bfs":
            GraphTraverser.traverse_graph_with_bfs_from_node(self, source_node)

        if algorithm == "dfs_recursion":
            GraphTraverser.traverse_graph_with_dfs_recursion_from_node(
                self, source_node
            )

        if algorithm == "dfs_stack":
            GraphTraverser.traverse_graph_with_dfs_stack_from_node(self, source_node)

        if algorithm == "dijkstra":
            GraphTraverser.traverse_graph_with_dijkstra_from_node(self, source_node)

    def reset_traversal(self):
        for node in self.nodes:
            self.nodes[node].reset_node()

    def traversed_graph(self):
        traversed_graph = self.empty_graph()
        for node in self.nodes:
            traversed_graph.nodes[node].distance = self.nodes[node].distance
            predecessor = self.nodes[node].predecessor
            if predecessor:
                traversed_graph.add_directed_edge(
                    predecessor,
                    node,
                    weight=self.nodes[predecessor].neighbors[node].weight,
                )
        return traversed_graph

    def empty_graph(self):
        return Graph(self.nodes_filepath, "no_edges.csv")

    def print_distances(self):
        print("Distance from source")
        for node in self.nodes:
            print(node, "->", self.nodes[node].distance)
        print()
