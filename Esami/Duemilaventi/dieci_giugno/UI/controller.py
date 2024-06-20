import flet as ft
from Esami.Duemilaventi.dieci_giugno.UI.view import View
from Esami.Duemilaventi.dieci_giugno.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.choiceActor = None


    def fillDDGenere(self):
        generi = self._model.getGeneri()
        for g in generi:
            self._view.ddGenere.options.append(ft.dropdown.Option(g))
        self._view.update_page()


    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        g = self._view.ddGenere.value
        if g is None or g == "":
            self._view.txt_result.controls.append(ft.Text("Devi selezionare un genere!"))
            self._view.update_page()
            return

        self._model.buildGraph(g)
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDDActors()
        self._view.btnAttoriSimili.disabled = False
        self._view.update_page()



    def handleAttoriSimili(self, e):
        self._view.txt_result.controls.clear()
        if self.choiceActor is None:
            self._view.txt_result.controls.append(ft.Text("Devi prima selezionare un attore!"))
            self._view.update_page()
            return

        attoriSimili = self._model.getAttoriSimili(self.choiceActor)
        self._view.txt_result.controls.append(ft.Text(f"Attori simili a {self.choiceActor}"))
        for a in attoriSimili:
            if a != self.choiceActor:
                self._view.txt_result.controls.append(ft.Text(f"{a}"))

        self._view.btnSimulazione.disabled = False
        self._view.update_page()


    def handleSimulazione(self, e):
        pass

    def fillDDActors(self):
        actors = self._model.getActorsNodes()
        actors.sort(key=lambda x: x.last_name)
        for a in actors:
            self._view.ddAttore.options.append(ft.dropdown.Option(
                text=a,
                data = a,
                on_click=self.readDDActor
            ))

    def readDDActor(self, e):
        if e.control.data is None:
            self.choiceActor = None
        else:
            self.choiceActor = e.control.data

