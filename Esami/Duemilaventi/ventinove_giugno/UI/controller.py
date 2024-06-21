import time

import flet as ft
from Esami.Duemilaventi.ventinove_giugno.model.model import Model
from Esami.Duemilaventi.ventinove_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        directors = self._model.getDirectors()
        directors.sort(key=lambda x: x.id)
        for d in directors:
            self._view.ddRegisti.options.append(ft.dropdown.Option(
                text=d,
                data=d,
                on_click=self.readDDRegista
            ))


    def handleCreaGrafo(self, e):
        self._view.txtOut.controls.clear()
        year = int(self._view.ddyear.value)
        self._model.buildGraph(year)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDD()
        self._view.update_page()



    def handleRegistiAdiacenti(self, e):
        self._view.txtOut.controls.clear()
        regista = self.choiceRegista
        res = self._model.getRegistiAdiacenti(regista)
        self._view.txtOut.controls.append(ft.Text(f"Registi adiacenti a {self.choiceRegista}"))
        for r in res:
            self._view.txtOut.controls.append(ft.Text(f"{r[0]} -> Attori condivisi: {r[1]}"))

        self._view.update_page()


    def handleCercaRegisti(self, e):
        self._view.txtOut.controls.clear()
        lim = int(self._view.txtInAttoriCond.value)
        start_time = time.time()
        path, attoriCond = self._model.cercaRegistiAffini(lim, self.choiceRegista)
        end_time = time.time()
        self._view.txtOut.controls.append(ft.Text(f"Elapsed time: {end_time-start_time}"))
        self._view.txtOut.controls.append(ft.Text(f"Nel percorso vengono condivisi {attoriCond} attori."))
        for i in range(0, len(path)-1):
            self._view.txtOut.controls.append(ft.Text(f"{path[i]} --> {path[i+1]}"))

        self._view.update_page()

    def readDDRegista(self, e):
        if e.control.data is None:
            self.choiceRegista = None
        else:
            self.choiceRegista = e.control.data
