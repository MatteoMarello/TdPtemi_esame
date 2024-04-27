import flet as ft

from Lab.Lab7.UI.view import View
from Lab.Lab7.model.model import Model


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
            self._view.create_alert("Devi prima selezionare un mese!")
            return
        else:
            umidita_media_citta = self._model.getUmiditaMedia(self._mese)

        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("L'umidità media nel mese selezionato è:"))
        for key in umidita_media_citta.keys():
            self._view.lst_result.controls.append(ft.Text(f"{key}: {umidita_media_citta[key]}"))

        self._view.update_page()

    def handle_sequenza(self, e):
        if self._mese == 0:
            self._view.create_alert("Devi prima selezionare un mese!")
            return
        else:
            sequenza, costo = self._model.getSequenza(self._mese)
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text(f"La sequenza ottimale ha costo {costo}"))
            for situazione in sequenza:
                self._view.lst_result.controls.append((ft.Text(situazione.__str__())))
        self._view.update_page()

    def read_mese(self, e):
        self._mese = int(e.control.value)

