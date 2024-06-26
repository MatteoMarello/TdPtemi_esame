import flet as ft
from Esami.Duemilaventidue.diciotto_gennaio.model.model import Model
from Esami.Duemilaventidue.diciotto_gennaio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDProvider(self):
        providers = self._model.getProviders()
        for p in providers:
            self._view.ddProvider.options.append(ft.dropdown.Option(p))


    def fillDDLocalita(self):
        localita = self._model.getLocalita()
        for l in localita:
            self._view.ddTarget.options.append(
                ft.dropdown.Option(
                    data=l,
                    text=l,
                    on_click=self.readDDLoc
                )
            )

    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        km = float(self._view.txtInDistnza.value)
        provider = self._view.ddProvider.value
        self._model.buildGraph(provider, km)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi {nE}"))
        self.fillDDLocalita()
        self._view.update_page()



    def handle_analisi(self, e):
        self._view.txtOut.controls.clear()
        listaNodiMostVicini = self._model.getNodiMostVicini()
        self._view.txtOut.controls.append(ft.Text("Lista di località con più vicini: "))
        for l in listaNodiMostVicini:
            self._view.txtOut.controls.append(ft.Text(f"{l[0]} --> {l[1]}"))

        self._view.update_page()




    def handlePercorso(self, e):
        self._view.txtOut.controls.clear()
        string = self._view.txtInStringa.value
        percorso = self._model.getPercorso(string, self.chosenLoc)
        if percorso is None:
            self._view.txtOut.controls.append(ft.Text(f"Non esiste un percorso tra le due località scelte!"))
            self._view.update_page()
            return

        self._view.txtOut.controls.append(ft.Text("Percorso ottimo trovato!"))
        for l in percorso:
            self._view.txtOut.controls.append(ft.Text(f"{l}"))



    def readDDLoc(self, e):
        if e.control.data is None:
            self.chosenLoc = None
        else:
            self.chosenLoc = e.control.data