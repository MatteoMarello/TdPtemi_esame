import time

import flet as ft
from Esami.Genes.undici_giugno.model.model import Model
from Esami.Genes.undici_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self._model.buildGraph()
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nE}"))
        arcoPesoMax, arcoPesoMin = self._model.getArchiEstremi()
        self._view.txt_result.controls.append(ft.Text(f"L'arco con peso massimo è: {arcoPesoMax[0]} --> {arcoPesoMax[1]}. Peso: {arcoPesoMax[2]["weight"]}"))
        self._view.txt_result.controls.append(ft.Text(f"L'arco con peso minimo è: {arcoPesoMin[0]} --> {arcoPesoMin[1]}. Peso: {arcoPesoMin[2]["weight"]}"))


        self._view.update_page()



    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        soglia = self._view.txt_soglia.value
        try:
            intSoglia = int(soglia)

        except ValueError:
            self._view.txt_result2.controls.append(ft.Text("La soglia deve essere un intero!"))
            self._view.update_page()
            return

        arcoPesoMax, arcoPesoMin = self._model.getArchiEstremi()
        pesoArcoMax = arcoPesoMax[2]["weight"]
        pesoArcoMin = arcoPesoMin[2]["weight"]
        if intSoglia < pesoArcoMin or intSoglia > pesoArcoMax:
            self._view.txt_result2.controls.append(ft.Text(f"La soglia deve essere compreso tra l'arco di peso minimo {pesoArcoMin} e l'arco di peso massimo {pesoArcoMax}"))
            self._view.update_page()
            return

        pesoMaggiore, pesoMinore = self._model.getConfrontoSoglia(intSoglia)
        self._view.txt_result2.controls.append(ft.Text(f"Gli archi con un peso minore della soglia sono: {pesoMinore}"))
        self._view.txt_result2.controls.append(ft.Text(f"Gli archi con un peso maggiore della soglia sono: {pesoMaggiore}"))
        self._view.update_page()


    def handle_search(self, e):
        self._view.txt_result3.controls.clear()
        soglia = self._view.txt_soglia.value
        try:
            intS = int(soglia)
        except ValueError:
            self._view.txt_result3.controls.append(ft.Text(f"La soglia deve essere un intero!"))
            self._view.update_page()
            return

        start_time = time.time()
        res, bestLenght = self._model.getBestPath(intS)
        end_time = time.time()
        self._view.txt_result3.controls.append(ft.Text(f"Elapsed time: {end_time-start_time} secondi."))
        self._view.txt_result3.controls.append(ft.Text(f"Peso cammino massimo: {bestLenght}"))
        for e in res:
            self._view.txt_result3.controls.append(ft.Text(f"{e[0]} --> {e[1]}: {e[2]["weight"]}"))

        self._view.update_page()
