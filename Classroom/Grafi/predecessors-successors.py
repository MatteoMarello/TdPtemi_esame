# Predecessors - Successors:

import networkx as nx

# Creiamo un digrafo
# N.B: i metodi .predecessors() e .succesors() ha senso utilizzare solo su un grafo orientato!
G = nx.DiGraph()
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
G.add_edges_from(edges)

# Nodo di interesse
node = 4

# Predecessori del nodo 4
predecessors = list(G.predecessors(node))
print(f"Predecessors of {node}: {predecessors}")

# Successori del nodo 4
successors = list(G.successors(node))
print(f"Successors of {node}: {successors}")

# Stampa predecessori e successori per ogni nodo
for node in G.nodes():
    predecessors = list(G.predecessors(node))
    successors = list(G.successors(node))
    print(f"Node {node}:")
    print(f"  Predecessors: {predecessors}")
    print(f"  Successors: {successors}")
    
    
# dfs/bfs_predecessors() - dfs/bfs_successors()

import networkx as nx

# Creiamo un grafo
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
G.add_edges_from(edges)

# Nodo di partenza
source = 1

# Predecessori BFS
bfs_pred = dict(nx.bfs_predecessors(G, source))
print("BFS Predecessors:", bfs_pred)

# Successori BFS
bfs_succ = dict(nx.bfs_successors(G, source))
print("BFS Successors:", bfs_succ)

# Predecessori DFS
dfs_pred = dict(nx.dfs_predecessors(G, source))
print("DFS Predecessors:", dfs_pred)

# Successori DFS
dfs_succ = dict(nx.dfs_successors(G, source))
print("DFS Successors:", dfs_succ)