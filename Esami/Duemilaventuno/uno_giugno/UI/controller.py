import flet as ft
from Esami.Duemilaventuno.uno_giugno.model.model import Model
from Esami.Duemilaventuno.uno_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        pass


    def handleCreaGrafo(self, e):
        self._view.txtOut.controls.clear()
        self._model.buildGraph()
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        genes = self._model.getGenes()
        for g in genes:
            self._view.ddGene.options.append(ft.dropdown.Option(g))
        self._view.update_page()



    def handleGeniAdiacenti(self, e):
        gene = self._view.ddGene.value

        geniAdiacenti = self._model.getGeniAdiacenti(gene)
        self._view.txtOut.controls.append(ft.Text(f"\nGeni adiacenti a {gene}"))
        for g in geniAdiacenti:
            self._view.txtOut.controls.append(ft.Text(f"{g[0]} {g[1]}"))

        self._view.update_page()


