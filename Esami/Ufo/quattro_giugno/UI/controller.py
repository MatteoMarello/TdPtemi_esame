import flet as ft
from Esami.Ufo.quattro_giugno.model.model import Model
from Esami.Ufo.quattro_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

    def fillDDShapes(self, e):
        anno = self._view.ddyear.value
        self._view.ddshape.options.clear()
        if anno is not None:
            shapes = self._model.getShapesYear(anno)
            for s in shapes:
                self._view.ddshape.options.append(ft.dropdown.Option(s))

        self._view.update_page()


    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        year = self._view.ddyear.value
        shape = self._view.ddshape.value
        if year is None or shape is None:
            self._view.txt_result.controls.append(ft.Text("Devi scegliere un anno e una forma."))
            self._view.update_page()
            return

        res = self._model.buildGraph(year, shape)
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(F"Numero di vertici: {nN}"))
        self._view.txt_result.controls.append(ft.Text(F"Numero di archi: {nE}"))
        self._view.txt_result.controls.append(ft.Text(F""))
        for s in res:
            self._view.txt_result.controls.append(ft.Text(f"{s[0]}, somma pesi su archi = {s[1]}"))

        self._view.update_page()



    def handle_path(self, e):
        self._view.txtOut2.controls.clear()
        res, bestDist = self._model.getBestPath()
        self._view.txtOut2.controls.append(ft.Text(f"La distanza del percorso con archi sempre crescenti massimizzata è {bestDist} km."))
        for e in res:
            self._view.txtOut2.controls.append(ft.Text(F"{e[0]} --> {e[1]}. Weight: {e[2]}, Distance: {e[3]}"))

        self._view.update_page()