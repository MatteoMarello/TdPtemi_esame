import flet as ft
from Esami.Duemilaventidue.quattordici_luglio.model.model import Model
from Esami.Duemilaventidue.quattordici_luglio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        self._borghi = self._model.getBorghi()
        for b in self._borghi:
            self._view.ddBorgo.options.append(ft.dropdown.Option(b))


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        borgo = self._view.ddBorgo.value
        if borgo is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un borgo!"))
            self._view.update_page()
            return

        self._model.buildGraph(borgo)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self._view.update_page()



    def handleAnalisiArchi(self, e):
        pesoMedio, listaArchi = self._model.analisiArchi()
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text(f"Peso medio degli archi: {pesoMedio}"))
        self._view.txtOut.controls.append(ft.Text(f"Archi con peso maggiore del peso medio: {len(listaArchi)}"))
        for e in listaArchi:
            self._view.txtOut.controls.append(ft.Text(f"{e[0]} -> {e[1]}. Peso: {e[2]['weight']}"))

        self._view.update_page()

