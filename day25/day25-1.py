import networkx as nx
file_path = 'day25.txt'

with open(file_path, 'r') as file:
    wireGraph = nx.Graph()
    productSize = 1
    
    for line in file:
        sourceToDest = line.strip().split(":")
        wireSource = sourceToDest[0]
        wireDestArray = sourceToDest[1].strip().split()
        for wireDest in wireDestArray:
            wireGraph.add_edge(wireSource, wireDest)

    minEdgeToCut = nx.minimum_edge_cut(wireGraph)
    wireGraph.remove_edges_from(minEdgeToCut)
    connectedGraph = nx.connected_components(wireGraph)
    
    for graph in connectedGraph:
        productSize *= len(graph)
    
    print(productSize)
