from graph import Graph
from graph_visualizer import GraphVisualizer


def print_shortest_path_tree(graph, source_node):
    print("Dijkstra from node", source_node)
    shortest_path_tree = graph.traversed_graph_with_algorith_from_node(
        "dijkstra", source_node
    )
    shortest_path_tree.print_graph()
    shortest_path_tree.print_distances()

    graph_visualizer = GraphVisualizer(shortest_path_tree)
    graph_visualizer.visualize_graph_as("tree")


print("Grafo")
graph = Graph("nodes2.csv", "edges2.csv")
graph.print_graph()
print()
for source_node in graph.nodes:
    print_shortest_path_tree(graph, source_node)
print()
