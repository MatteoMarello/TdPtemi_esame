import time

import flet as ft
from Esami.Duemilaventi.quattro_settembre.model.model import Model
from Esami.Duemilaventi.quattro_settembre.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.choiceFilm = None


    def handleCreaGrafo(self, e):
        self._view.txtOut.controls.clear()
        rank = self._view.txtInRank.value
        try:
            floatRank = float(rank)
        except ValueError:
            self._view.txtOut.controls.append(ft.Text("Il rank inserito deve essere un numero!"))
            self._view.update_page()
            return

        if floatRank < 0 or floatRank > 10:
            self._view.txtOut.controls.append(ft.Text("Il rank deve essere un numero compreso tra 0 e 10!"))
            self._view.update_page()
            return

        self._model.buildGraphV3(floatRank)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDDFilm()
        self._view.update_page()

    def fillDDFilm(self):
        films = self._model.getFilms()
        for f in films:
            self._view.ddFilm.options.append(ft.dropdown.Option(
                text=f.__str__(),
                data=f,
                on_click=self.readDDFilm
            ))

    def readDDFilm(self, e):
        if e.control.data is None:
            self.choiceFilm = None
        else:
            self.choiceFilm = e.control.data

    def handleFilmGradoMassimo(self, e):
        self._view.txtOut.controls.clear()
        film, grado = self._model.getFilmGradoMax()
        self._view.txtOut.controls.append(ft.Text(f"Film: {film}"))
        self._view.txtOut.controls.append(ft.Text(f"Grado: {grado}"))
        self._view.update_page()


    def handleCamminoIncremento(self, e):
        self._view.txtOut.controls.clear()
        start_time = time.time()
        camminoIncrementale = self._model.getCammino(self.choiceFilm)
        end_time = time.time()
        self._view.txtOut.controls.append(ft.Text(f"Elapsed time: {end_time-start_time}"))
        print(camminoIncrementale)
        for c in camminoIncrementale:
            self._view.txtOut.controls.append(ft.Text(f"{c[0]} -> {c[1]} -> Weight: {c[2]}"))

        self._view.update_page()
