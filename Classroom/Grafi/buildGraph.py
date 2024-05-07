import networkx as nx
import flet as ft

def creaGrafo():
    myGraph = nx.Graph()
    myGraph.add_node(1)  # .add_node() aggiunge un nodo al grafo
    myGraph.add_node("a")
    myGraph.add_node(ft.Text())
    # Posso aggiungere qualsiasi tipo di oggetto come nodo del grafo, l'importante è che sia un oggetto hashable!
    mynodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Posso anche aggiungere più nodi tutti assieme, ad esempio da una lista con .add_nodes_from()!
    myGraph.add_nodes_from(mynodes)

    # Anch e gli archi posso aggiungerli uno per volta come tuple con .add_edge()
    # Altrimenti se ho una lista di tuple posso aggiungere più archi contemporaneamente con .add_edges_from()
    edgeList = [(1,2), (1,3), (3,4), (2,5), (5,6)]
    myGraph.add_edges_from(edgeList)

    # Metodo per aggiungere un arco pesato fra due nodi! Il terzo parametro è il "peso" o "costo" di quell'arco.
    myGraph.add_edge(1, 2, weight = 5)

    print(1 in myGraph) # Restituisce True/F alse a seconda se è presente il nodo passato in input all'interno del grafo.

    # Ciclo su tutti i nodi del grafo
    for v in myGraph:
        print(v)

    # Ciclo su tutti i nodi raggiungibili dal nodo 1
    for v in myGraph[1]:
        print(v)



    # Metodo per stampare le informazioni sul grafo (numero di nodi e di archi)
    print(myGraph)
    # Metodo per stampare i nodi di un grafo
    print(f'Nodes: {myGraph.nodes}')
    # Metodo per stampare gli archi di un grafo
    print(f'Edges: {myGraph.edges}')

    # Con .DiGraph() costruisco un grafo diretto! Gli archi saranno unidirezionali.
    myDiGraph = nx.DiGraph()
    myDiGraph.add_nodes_from(mynodes)
    myDiGraph.add_edges_from(edgeList)

    # Metodo per stampare gli archi entranti in un nodo
    print(myDiGraph.in_edges(1))
    # Metodo per stampare gli archi uscenti da un nodo
    print(myDiGraph.out_edges(1))

    # Posso anche costruire multigrafi
    multiGraph = nx.MultiDiGraph()
    multiGraph.add_nodes_from(mynodes)
    multiGraph.add_edges_from(edgeList)
    # Quello che cambia con i multi grafi rispetto agli altri grafi e che posso aggiungere più di un arco tra due stessi nodi.
    # I diversi archi che collegano i due nodi possono essere caratterizzate per esempio da attributi / pesi diversi.
    multiGraph.add_edge(1, 2, attr = "foo")
    print(multiGraph.in_edges(1))
    print(multiGraph.out_edges(1))
    # Con il print sotto noto che ci sono due archi che collegano il nodo 1 al nodo 2. Uno è senza attributo, l'altro ha attributo 'foo'.
    print(multiGraph[1])

if __name__ == "__main__":
    creaGrafo()