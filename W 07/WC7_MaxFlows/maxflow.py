import networkx as nx

def _dfs(graph, source, sink):
    """
    Depth-First Search (DFS) function to find a path from the source to the sink in the graph.
    """
    stack, visited = [(source, [source])], {source}

    while stack:
        u, path = stack.pop()
        if u == sink:
            return path
        for v in graph[u]:
            if v not in visited and graph[u][v]['capacity'] > 0:
                visited.add(v)
                stack.append((v, path + [v]))
    return []


class MaxFlow:
    def __init__(self, file) -> None:
        """
        Initialize the MaxFlow class with a flow network provided in the given file.
        """
        self.graph = nx.DiGraph()
        self._read_flow_network(file)
        self.residual_graph = self.graph.copy()  # Create a copy of the graph for the residual network

    def _read_flow_network(self, file):
        """
        Read the flow network from the file and populate the graph.
        """
        for line in file:
            u, v, capacity = line.split()
            self.graph.add_edge(u, v, capacity=int(capacity))

    def get_value(self):
        """
        Compute the maximum flow in the flow network using the Ford-Fulkerson algorithm.
        """
        source, sink, max_flow = 's', 't', 0

        path = _dfs(self.graph, source, sink)

        while path:
            bottleneck_capacity = float('inf')

            # Find the bottleneck capacity along the augmenting path
            for index in range(len(path) - 1):
                u, v = path[index], path[index + 1]
                capacity = self.residual_graph[u][v]['capacity']
                bottleneck_capacity = min(bottleneck_capacity, capacity)

            # Update the residual capacities and augment the flow along the path
            for index in range(len(path) - 1):
                u, v = path[index], path[index + 1]
                residual_capacity = self.residual_graph[u][v]['capacity'] - bottleneck_capacity

                # Update the residual capacities in the residual graph
                if not residual_capacity:
                    self.residual_graph.remove_edge(u, v)
                else:
                    self.residual_graph[u][v]['capacity'] = residual_capacity

                # Add reverse edges and update their capacities
                if not self.residual_graph.has_edge(v, u):
                    self.residual_graph.add_edge(v, u, capacity=0)
                self.residual_graph[v][u]['capacity'] += bottleneck_capacity

            # Update the maximum flow
            max_flow += bottleneck_capacity

            # Find the next augmenting path
            path = _dfs(self.residual_graph, source, sink)

        return max_flow

    def get_flow(self):
        """
        Compute the flow on each edge in the flow network.
        """
        flow_dict = {}
        for u, v in self.graph.edges():
            if self.residual_graph.has_edge(u, v):
                # Calculate flow by subtracting residual capacity from original capacity
                flow = self.graph[u][v]['capacity'] - self.residual_graph[u][v]['capacity']
            else:
                flow = self.graph[u][v]['capacity']

            # Add non-zero flows to the dictionary
            if flow > 0:
                flow_dict[(u, v)] = flow
        return flow_dict
