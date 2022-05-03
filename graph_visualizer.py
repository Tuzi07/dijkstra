import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout


class GraphVisualizer:
    def __init__(self, graph):
        self.networkx_digraph = nx.DiGraph()
        self.add_edges_from_graph(graph)

    def add_edges_from_graph(self, graph):
        for node in graph.nodes:
            for neighbor in graph.nodes[node].neighbors:
                weight = graph.nodes[node].neighbors[neighbor].weight
                self.networkx_digraph.add_edge(node, neighbor, weight=weight)

    def visualize_graph_as(self, visualize_as):
        graphviz_program = "sfdp"

        if visualize_as == "tree":
            graphviz_program = "dot"

        graph = self.networkx_digraph
        nx.draw_networkx(graph, graphviz_layout(graph, prog=graphviz_program))
        plt.show()
