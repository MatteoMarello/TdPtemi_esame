import time

import flet as ft
from Lab.Lab14.model.model import Model
from Lab.Lab14.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        nN = self._model.getNumNodi()
        nE = self._model.getNumEdges()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.pesoMin, self.pesoMax = self._model.getArchiEstremi()
        self._view.txt_result.controls.append(ft.Text(f"Peso minimo sugli archi: {self.pesoMin}"))
        self._view.txt_result.controls.append(ft.Text(f"Peso massimo sugli archi: {self.pesoMax}"))
        self._view.update_page()


    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        soglia = self._view.txt_name.value
        try:
            intSoglia = int(soglia)
            if intSoglia < self.pesoMin or intSoglia > self.pesoMax:
                self._view.txt_result2.controls.append("La soglia deve essere un intero")
                self._view.update_page()
                return

            sottoSoglia, sopraSoglia = self._model.getSopraSottoSoglia(intSoglia)
            self._view.txt_result2.controls.append(ft.Text(f"Numero di archi con peso sopra la soglia: {sopraSoglia}"))
            self._view.txt_result2.controls.append(ft.Text(f"Numero di archi con peso sopra la soglia: {sottoSoglia}"))


        except ValueError:
            self._view.txt_result2.controls.append("La soglia deve essere un intero")

        self._view.update_page()


    def handle_search(self, e):
        self._view.txt_result3.controls.clear()
        soglia = self._view.txt_name.value
        if soglia == "" or soglia is None:
            self._view.txt_result3.controls.append(ft.Text("Devi inserire una soglia"))
            self._view.update_page()
            return

        try:
            intSoglia = int(soglia)
            if intSoglia > self.pesoMax:
                self._view.txt_result3.controls.append(ft.Text("La soglia è maggiore del peso massimo degli archi del grafo! Il cammino ottenuto è nullo!"))
                self._view.update_page()
                return

            start_time = time.time()
            pesoCamminoOttimo, edges = self._model.getPercorso(intSoglia)
            end_time = time.time()
            self._view.txt_result3.controls.append(ft.Text(
                f"Elapsed time: {end_time-start_time}"))
            self._view.txt_result3.controls.append(ft.Text(
                f"Peso cammino minimo: {pesoCamminoOttimo}"))
            for edge in edges:
                self._view.txt_result3.controls.append(ft.Text(f"{edge[0]} --> {edge[1]}. Peso: {edge[2]}"))

            self._view.update_page()



        except ValueError:
            self._view.txt_result3.controls.append(ft.Text("La soglia deve essere un intero"))
            self._view.update_page()
            return
