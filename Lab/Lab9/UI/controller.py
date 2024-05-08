import flet as ft
import networkx as nx

from Lab.Lab9.UI.view import View

class Controller:
    def __init__(self, view: View, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.controls.clear()
        distanza_min = (self._view._txtIn.value)
        if distanza_min == "" or distanza_min is None:
            self._view._txt_result.controls.append(ft.Text('Devi prima inserire una distanza minima nel campo apposito!'))
        else:
            graph: nx.Graph = self._model.buildGraph(int(distanza_min))
            num_nodi = len(graph.nodes)
            num_archi = len(graph.edges)
            self._view._txt_result.controls.append(
                ft.Text(f'Il grafo ha {num_nodi} nodi e {num_archi} archi'))

            for edge in graph.edges(data=True):
                print(graph.get_edge_data(edge[0],edge[1]))
                self._view._txt_result.controls.append(ft.Text(f'{edge[0]} -> {edge[1]} -- Distance: {round(edge[2]['distanza'], 2)} miles'))

        self._view.update_page()