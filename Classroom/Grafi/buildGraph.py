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

    print(1 in myGraph) # Restituisce True/False a seconda se è presente il nodo passato in input all'interno del grafo.

    # Ciclo su tutti i nodi del grafo
    for v in myGraph:
        print(v)

    # Ciclo su tutti i nodi raggiungibili dal nodo 1
    for v in myGraph[1]:
        print(v)

    # Dato che con .Graph() costruiso un grafo semplice e non orientato, se nel mio grafo è già presente l'arco tra due nodi,
    # ad esempio (1,2) che ho aggiunto sopra, e provo ad aggiungere l'arco (2,1), non cambierà nulla nel mio grafo perchè i
    # due nodi risulteranno già connessi!
    myGraph.add_edge(2,1)

    # In questo caso io non ho mai aggiunto un arco (2,1), ma dato che ho aggiunto l'arco (1,2) e dato che il mio grafo
    # è semplice e non orientato, l'arco (1,2) equivale all'arco (2,1) pertanto il metodo sottostante mi restituisce True.
    print(myGraph.has_edge(2,1))


    # Metodo per stampare le informazioni sul grafo (numero di nodi e di archi)
    print(myGraph)
    # Metodo per stampare i nodi di un grafo
    print(f'Nodes: {myGraph.nodes}')
    # Metodo per stampare gli archi di un grafo
    print(f'Edges: {myGraph.edges}')

    myGraph.edges(data=True)
    # In questo modo, con data=True, .edges mi restituisce non solo una lista di tuple formate da due elementi in cui vengono
    # indicati i nodi tra cui è presente un arco, ma all'interno delle tuple ci sono tanti altri argomenti quanti sono gli attributi
    # di quell'arco sotto forma di dizionari. Quindi se scrivo .add_edge(1,2,weight=10), quando mi prendo gli edges del grafo con data=True,
    # oltre ad avere (1,2), avrò (1,2,{'weight':10}).
    # Un'altra opzione che posso avere dato i nodi di un arco per ottenere gli attributi associati all'arco, è utilizzare
    # il metodo .get_edge_data(), a cui passo come parametri i due nodi e mi restituisce un dizionario con tutti gli attributi
    # e i valori associati a quegli attributi dell'arco.

    print("------------------------------------------------------")
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

    print("------------------------------------------------------")
    print("SUBGRAPH")
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

    # Creazione di un sottoinsieme del grafo includendo i nodi 1 e 2
    subgraph = G.subgraph([1, 2])

    # Stampa dei nodi e degli archi del sottoinsieme
    print("Nodi del sottoinsieme:", subgraph.nodes())
    print("Archi del sottoinsieme:", subgraph.edges())

    print("------------------------------------------------------")
    print("DISJOINT_UNION")
    # Creazione dei grafi G1 e G2
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (2, 3)])

    G2 = nx.Graph()
    G2.add_edges_from([(3, 4), (4, 5)])

    # Unione dei due grafi
    union_graph = nx.disjoint_union(G1, G2)

    # Stampa dei nodi e degli archi del grafo unione
    print("Nodi del grafo unione:", union_graph.nodes())
    print("Archi del grafo unione:", union_graph.edges())


    print("------------------------------------------------------")
    print("COMPOSE")
    # Con .compose() i nodi dei due grafi si uniscono singolarmente all'interno di un unico grafo, e tutti gli archi
    # presenti nei due grafi vengono copiate nel grafo risultante.
    # Creazione dei grafi G1 e G2
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (2, 3), (3, 4)])

    G2 = nx.Graph()
    G2.add_edges_from([(3, 4), (4, 5), (5, 6)])

    # Composizione dei due grafi
    composed_graph = nx.compose(G1, G2)

    # Stampa dei nodi e degli archi del grafo composto
    print("Nodi del grafo composto:", composed_graph.nodes())
    print("Archi del grafo composto:", composed_graph.edges())

    print("------------------------------------------------------")
    print("COMPLEMENT")
    # .complement() mi restituisce un grafo complementare a quello fornito in input. Ciò significa che avrà gli stessi nodi
    # del grafo in input, ma archi completamente diversi: i nodi che nel grafo di partenza sono connessi da un arco, non
    # saranno più connessi nel grafo risultante, e i nodi che inizialmente non erano connessi nel grafo di partenza, ora
    # saranno connessi da un arco.
    complementGraph = nx.complement(G1)
    print("Nodi del grafo complementare:", complementGraph.nodes())
    print("Archi del grafo complementare:", complementGraph.edges())



if __name__ == "__main__":
    creaGrafo()