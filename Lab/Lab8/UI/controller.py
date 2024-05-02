import time

import flet as ft
from Lab.Lab8.model.model import Model
from Lab.Lab8.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        self._view._txtOut.controls.clear()
        nerc_value = self._view._ddNerc.value
        nerc = self._idMap.get(nerc_value)
        max_H = int(self._view._txtHours.value)
        max_Y = int(self._view._txtYears.value)
        start_time = time.time()
        soluzione, utenti_disservizio, ore_disservizio = self._model.worstCase(nerc, max_Y, max_H)
        end_time = time.time()
        self._view._txtOut.controls.append(ft.Text(f'People affected: {utenti_disservizio}'))
        self._view._txtOut.controls.append(ft.Text(f'Hours of outage: {ore_disservizio}'))
        for event in soluzione:
            self._view._txtOut.controls.append(ft.Text(event.__str__()))
        self._view._txtOut.controls.append(ft.Text(f'Elapsed time: {end_time-start_time}'))


        self._view.update_page()

    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
