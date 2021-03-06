from networkx import Graph, shortest_path

...

def build_graph(ways):
    graph = Graph()
    for way, tags in ways:
        for segment in nwise(way.coords):
            weight = length(segment) * coef(tags)
            graph.add_edge(segment[0], segment[1],
                           weight=weight)
    return graph

shortest_path(graph, source, dest)
