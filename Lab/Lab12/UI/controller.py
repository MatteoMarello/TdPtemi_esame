import time

import flet as ft
from Lab.Lab12.UI.view import View
from Lab.Lab12.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._view.ddyear.options.append(ft.dropdown.Option("2015"))
        self._view.ddyear.options.append(ft.dropdown.Option("2016"))
        self._view.ddyear.options.append(ft.dropdown.Option("2017"))
        self._view.ddyear.options.append(ft.dropdown.Option("2018"))

        countries = self._model.getCountries()
        for country in countries:
            self._view.ddcountry.options.append(ft.dropdown.Option(country))



    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        try:
            year = int(self._view.ddyear.value)
            country = self._view.ddcountry.value
            nodi, archi = self._model.createGraph(year, country)
            self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nodi}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {archi}"))
            self._view.btn_volume.disabled = False

        except ValueError:
            self._view.txt_result.controls.append(ft.Text("L'anno selezionato non risulta valido!"))

        self._view.update_page()



    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        volumi = self._model.getVolumi()
        for v in volumi:
            self._view.txtOut2.controls.append(ft.Text(f"{v[0]} --> {v[1]}"))

        self._view.update_page()



    def handle_path(self, e):
        lun = self._view.txtN.value
        try:
            intLun = int(lun)
            if intLun < 2:
                self._view.txtOut3.controls.append(ft.Text("Devi inserire un numero almeno pari a 2!"))
            else:
                start_time = time.time()
                self._model.getPercorso(intLun)
                end_time = time.time()
                self._view.txtOut3.controls.append(ft.Text(f"Elapsed time: {round(end_time-start_time,2)} secondi"))

        except ValueError:
            self._view.txtOut3.controls.append(ft.Text("Devi inserire un numero intero!"))


        self._view.update_page()