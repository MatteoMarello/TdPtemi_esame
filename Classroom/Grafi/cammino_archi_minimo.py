import networkx as nx
# Per trovare un cammino minimo in un grafo ho diversi modi

# 1. Se voglio ottenere il cammino minimo in termini di peso degli archi, posso usare i metodi di nx che implementano l'algoritmo di Djikstra.

# 2. Se voglio ottenere il cammino minimo in termine di numero di archi posso utilizzare il metodo di networkX shortes_path()


# Creiamo un grafo non pesato
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 5), (6, 7)]
G.add_edges_from(edges)

# Nodo sorgente e nodo di destinazione
source = 1
target = 5

# Troviamo la lunghezza del percorso più breve usando BFS
length = nx.shortest_path_length(G, source=source, target=target)
print(f"Shortest path length from {source} to {target}: {length}")

# Troviamo il percorso più breve usando BFS
path = nx.shortest_path(G, source=source, target=target)
print(f"Shortest path from {source} to {target}: {path}")

# 3. Se voglio ottenere il cammino minimo in termine di numero di archi posso utilizzare al posto di shortest_path()
# il metodo bfs_tree() e a partire dall'albero di esplorazione bfs posso ottenere il cammino minimo da un nodo source a uno target in questo modo.
# DA IMPARARE A MEMORIA !!!

# Creiamo un grafo non pesato
G = nx.Graph()
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
G.add_edges_from(edges)
# Nodo sorgente
source = 1
# Generiamo l'albero BFS a partire dal nodo sorgente
bfs_tree = nx.bfs_tree(G, source)
# Nodo di destinazione
target = 5
# Funzione per trovare il cammino dall'albero BFS senza usare shortest_path()
def find_path_from_bfs_tree(bfs_tree, source, target):
    path = []
    current = target

    while current != source:
        path.append(current)
        predecessors = list(bfs_tree.predecessors(current))
        if not predecessors:
            return None  # Non c'è un percorso valido
        current = predecessors[0]

    path.append(source)
    path.reverse()
    return path


# Troviamo il cammino dal nodo sorgente al nodo di destinazione
path = find_path_from_bfs_tree(bfs_tree, source, target)
print(f"Shortest path from {source} to {target} in the BFS tree: {path}")

# Potrei utilizzare anche l'algoritmo DFS per ottenere un cammino tra un nodo source e un nodo target, ma non avrei la certezza
# che si tratti del cammino più breve possibile in termine di numero di archi. Con BFS, invece, ho questa garanzia..