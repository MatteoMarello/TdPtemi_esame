import flet as ft

from Classroom.GestioneMeteo.UI.view import View
from Classroom.GestioneMeteo.model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        if self._mese == 0:
            self._view.create_alert("Selezionare un mese")
            return

        result = self._model.calcola_umidita_media(self._mese)
        print(result)
        self._view.lst_result.controls.clear()
        for element in result:
            self._view.lst_result.controls.append(ft.Text(f'{element[0]} -> {element[1]}'))

        self._view.update_page()

    def handle_sequenza(self, e):
        if self._mese == 0:
            self._view.create_alert("Selezionare un mese")
            return

        sequenza, costo = self._model.calcola_sequenza(self._mese)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f'Il costo della sequenza è {costo}'))
        for fermata in sequenza:
            self._view.lst_result.controls.append(ft.Text(fermata))

    def read_mese(self, e):
        self._mese = int(e.control.value)

