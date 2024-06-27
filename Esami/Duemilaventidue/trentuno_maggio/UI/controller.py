import flet as ft
from Esami.Duemilaventidue.trentuno_maggio.model.model import Model
from Esami.Duemilaventidue.trentuno_maggio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDProvider(self):
        self._view.ddProvider.options = []
        providers = self._model.getProviders()
        for p in providers:
            self._view.ddProvider.options.append(ft.dropdown.Option(p))


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        provider = self._view.ddProvider.value
        if provider is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un provider!"))
            self._view.update_page()
            return

        self._model.buildGraph(provider)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self.fillDDQuartieri()
        self._view.update_page()

    def fillDDQuartieri(self):
        self._view.ddQuartiere.options = []
        quartieri = self._model.getCities()
        quartieri.sort(key=lambda q: q.City)
        for q in quartieri:
            self._view.ddQuartiere.options.append(ft.dropdown.Option(
                data=q,
                text=q,
                on_click=self.readDDQ
            ))

    def handleQuartieri(self, e):
        self._view.txtOut.controls.clear()
        if self.chosenCity is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un quartiere!"))
            self._view.update_page()
            return

        quartieriAdiacenti = self._model.getQuartieriAdiacenti(self.chosenCity)
        for q in quartieriAdiacenti:
            self._view.txtOut.controls.append(ft.Text(f"{q[0]} --> {q[1]}"))

        self._view.update_page()
    def readDDQ(self, e):
        if e.control.data is None:
            self.chosenCity = None
        else:
            self.chosenCity = e.control.data


