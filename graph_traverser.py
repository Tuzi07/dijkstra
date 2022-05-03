from collections import deque
from queue import PriorityQueue


class GraphTraverser:
    def traverse_graph_with_bfs_from_node(graph, source_node):
        queue = deque([])

        queue.append(source_node)
        graph.nodes[source_node].was_visited = True

        while queue:
            current = queue.popleft()

            for neighbor in graph.nodes[current].neighbors:
                if not graph.nodes[neighbor].was_visited:
                    graph.nodes[neighbor].was_visited = True
                    graph.nodes[neighbor].steps = graph.nodes[current].steps + 1
                    graph.nodes[neighbor].predecessor = current
                    queue.append(neighbor)

    def traverse_graph_with_dfs_recursion_from_node(graph, node):
        graph.nodes[node].was_visited = True
        for neighbor in graph.nodes[node].neighbors:
            if not graph.nodes[neighbor].was_visited:
                graph.nodes[neighbor].steps = graph.nodes[node].steps + 1
                graph.nodes[neighbor].predecessor = node
                GraphTraverser.traverse_graph_with_dfs_recursion_from_node(
                    graph, neighbor
                )

    def traverse_graph_with_dfs_stack_from_node(graph, source_node):
        stack = deque([])

        stack.append(source_node)

        while stack:
            current = stack.pop()
            if not graph.nodes[current].was_visited:
                graph.nodes[current].was_visited = True
                for neighbor in graph.nodes[current].neighbors:
                    if not graph.nodes[neighbor].was_visited:
                        stack.append(neighbor)
                        graph.nodes[neighbor].predecessor = current
                        graph.nodes[neighbor].steps = graph.nodes[current].steps + 1

    def traverse_graph_with_dijkstra_from_node(graph, source_node):
        priority_queue = PriorityQueue()
        priority = graph.nodes[source_node].distance
        priority_queue.put((priority, source_node))

        while not priority_queue.empty():
            distance, node = priority_queue.get()

            if not graph.nodes[node].was_visited:
                graph.nodes[node].was_visited = True
                GraphTraverser.put_neighbors_in_priority_queue_if_shorter_distance(
                    node, graph, priority_queue, distance
                )

    def put_neighbors_in_priority_queue_if_shorter_distance(
        node, graph, priority_queue, distance
    ):
        for neighbor in graph.nodes[node].neighbors:
            if not graph.nodes[neighbor].was_visited:
                new_distance = distance + graph.nodes[node].neighbors[neighbor].weight
                if new_distance < graph.nodes[neighbor].distance:
                    graph.nodes[neighbor].distance = new_distance
                    graph.nodes[neighbor].predecessor = node
                    priority_queue.put((new_distance, neighbor))
