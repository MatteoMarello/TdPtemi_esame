import time

import flet as ft
from Lab.Lab13.model.model import Model
from Lab.Lab13.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        self._listYear = self._model.getYears()
        for y in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(y))

        self._listShape = self._model.getShapes()
        for s in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))

        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        year = int(self._view.ddyear.value)
        shape = self._view.ddshape.value
        if year is None or shape is None:
            self._view.txt_result.controls.append(ft.Text("Devi indicare un anno e una forma dal menù a tendina!"))
            self._view.update_page()
            return

        self._model.buildGraph(year, shape)
        nN, nE = self._model.getGraphSizes()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nN}. Numero di archi: {nE}"))
        graphDetails = self._model.getGraphDetails()
        for element in graphDetails:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {element[0]} --> somma pesi su archi: {element[1]}"))


        self._view.update_page()

    def handle_path(self, e):
        self._view.txtOut2.controls.clear()
        start_time = time.time()
        percorso, dist = self._model.getPercorso()
        end_time = time.time()
        self._view.txtOut2.controls.append(ft.Text(f"Elapsed time: {round(end_time-start_time, 2)} secondi"))
        self._view.txtOut2.controls.append(ft.Text(f"Distanza cammino migliore: {dist}"))
        for el in percorso:
            self._view.txtOut2.controls.append(ft.Text(f"{el[0]} --> {el[1]}. Peso: {el[2]}. Distanza: {el[3]}"))

        self._view.update_page()
