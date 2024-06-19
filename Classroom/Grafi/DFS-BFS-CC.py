import networkx as nx

# Creiamo un grafo
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]
G.add_edges_from(edges)

# Generiamo l'albero di DFS
dfs_tree = nx.dfs_tree(G, source=1)
print("DFS Tree Nodes:", len(dfs_tree.nodes()))  # Numero di nodi
print("DFS Tree Edges:", len(dfs_tree.edges()))  # Numero di archi
print("DFS Tree Edge List:", list(dfs_tree.edges()))  # Lista degli archi

# Generiamo l'albero di BFS
bfs_tree = nx.bfs_tree(G, source=1)
print("BFS Tree Nodes:", len(bfs_tree.nodes()))  # Numero di nodi
print("BFS Tree Edges:", len(bfs_tree.edges()))  # Numero di archi
print("BFS Tree Edge List:", list(bfs_tree.edges()))  # Lista degli archi

# Troviamo la componente connessa contenente il nodo 1
component = nx.node_connected_component(G, 1)
print("Connected Component Size:", len(component))  # Numero di nodi
print("Connected Component Nodes:", component)

"""
Numero di nodi
Il numero di nodi che ottieni da un albero DFS (len(dfs_tree.nodes())) o BFS (len(bfs_tree.nodes())) è uguale al numero di nodi nella componente connessa che include il nodo di partenza. Questo perché sia l’albero DFS che l’albero BFS esplorano tutti i nodi raggiungibili dal nodo di partenza.

Numero di archi
Il numero di archi in un albero di attraversamento (DFS o BFS) è sempre esattamente uno in meno rispetto al numero di nodi, poiché un albero con n nodi ha n-1 archi.

Differenza negli archi
Gli archi stessi possono differire tra l’albero DFS e l’albero BFS, poiché i due algoritmi esplorano il grafo in modi diversi:
"""