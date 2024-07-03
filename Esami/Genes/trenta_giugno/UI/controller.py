import flet as ft
from Esami.Genes.trenta_giugno.model.model import Model
from Esami.Genes.trenta_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        loc = self._model.getLocalizzazioni()
        loc.sort()
        for l in loc:
            self._view.ddLocalizzazione.options.append(ft.dropdown.Option(l))


    def handleStatistiche(self, e):
        self._view.txtOut.controls.clear()
        locChosen = self._view.ddLocalizzazione.value
        if locChosen is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare una localizzazione dal menù a tendina!"))
            self._view.update_page()
            return
        nN , nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {nN} vertici."))
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {nE} archi."))
        stats = self._model.getStatistiche(locChosen)
        for l in stats:
            self._view.txtOut.controls.append(ft.Text(f"{l[0]} --> {l[1]}"))
        self._view.update_page()

    def handle_path(self, e):
        self._view.txtOut.controls.clear()
        locChosen = self._view.ddLocalizzazione.value
        if locChosen is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare una localizzazione dal menù a tendina!"))
            self._view.update_page()
            return

        bestPath, bestLenght = self._model.getBestPath(locChosen)

        self._view.txtOut.controls.append(ft.Text(F"La lunghezza del percorso migliore è: {bestLenght}"))
        for i in range(0, len(bestPath)-1):
            self._view.txtOut.controls.append(ft.Text(f"{bestPath[i]} --> {bestPath[i+1]}"))

        self._view.update_page()
