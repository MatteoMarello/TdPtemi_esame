from view import View
from voto import Libretto, Voto
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Libretto()
        self.startupLibretto()
        self._model.stampa()


    def startupLibretto(self):
        self._model.append(Voto("Analisi I", 10, 25, False, '2020-01-01'))
        self._model.append(Voto("Chimica", 8, 30, False, '2020-01-02'))
        self._model.append(Voto("Informatica", 8, 30, True, '2020-01-03'))
        self._model.append(Voto("Algebra Lineare", 10, 24, False, '2020-06-01'))
        self._model.append(Voto("Fisica I", 10, 18, False, '2020-01-01'))

    def handleAdd(self, e):
        nomeEsame = self._view._txtIn.value
        if nomeEsame == "":
            self._view._lvOut.controls.append(ft.Text("Il campo nome non può essere vuoto!", color="red"))
            self._view.update()
            return

        strCfu = self._view._txtCFU.value
        try:
            intCfu = int(strCfu)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il campo CFU deve essere un intero.", color="red"))
            self._view.update()
            return

        punteggio = self._view._ddVoto.value

        if punteggio is None:
            self._view._lvOut.controls.append(ft.Text("Il campo punteggio va selezionato!", color="red"))
            self._view.update()
            return

        if punteggio == "30L":
            punteggio = 30
            lode = True
        else:
            punteggio = int(punteggio)
            lode = False

        data = self._view._datePicker.value
        if data is None:
            self._view._lvOut.controls.append(ft.Text("Il campo data va selezionato!", color="red"))
            self._view.update()
            return

        self._model.append(Voto(nomeEsame, intCfu, punteggio, lode, f'{data.year}-{data.month}-{data.day}'))
        self._view._lvOut.controls.append(ft.Text("Voto correttamente aggiunto!", color="green"))
        self._view.update()

    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for elem in outList:
            self._view._lvOut.controls.append(ft.Text(elem))

        self._view.update()