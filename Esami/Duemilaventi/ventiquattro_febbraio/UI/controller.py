import flet as ft
from Esami.Duemilaventi.ventiquattro_febbraio.model.model import Model
from Esami.Duemilaventi.ventiquattro_febbraio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.chosenMatch = None


    def fillDD(self):
        matches = self._model.getMatches()
        matches.sort(key=lambda m: m.id)
        for m in matches:
            self._view.ddMatch.options.append(ft.dropdown.Option(
                text=m,
                data=m,
                on_click=self.readChoiceMatch
            ))


    def readChoiceMatch(self, e):
        if e.control.data is None:
            self.chosenMatch = None
        else:
            self.chosenMatch = e.control.data


    def handleGrafo(self, e):
        self._view.txtOut.controls.clear()
        if self.chosenMatch is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un partita!"))
            self._view.update_page()
            return

        self._model.buildGraph(self.chosenMatch.id)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))

        self._view.update_page()




    def handleGiocatoreMigliore(self, e):
        self._view.txtOut.controls.clear()
        bestPlayer, score = self._model.getBestPlayer()
        self._view.txtOut.controls.append(ft.Text(f"Giocatore migliore: {bestPlayer}"))
        self._view.txtOut.controls.append(ft.Text(f"Score {score}"))
        self._view.update_page()



