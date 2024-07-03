import flet as ft
from Esami.Duemilaventitre.trenta_maggio.model.model import Model
from Esami.Duemilaventitre.trenta_maggio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def fillDDNazioni(self):
        countries = self._model.getCountries()
        for c in countries:
            self._view.ddNazione.options.append(ft.dropdown.Option(c))


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        anno = self._view.ddAnno.value
        nazione = self._view.ddNazione.value
        m = int(self._view.txtInProd.value)
        if anno is None or nazione is None or m == "":
            self._view.txtOut.controls.append(ft.Text("Devi indicare un anno, una nazione, e un numero minimo di prodotti!"))

        self._model.buildGraph(anno,nazione,m)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        nodes = self._model.getNodes()
        for n in nodes:
            self._view.ddRivenditore.options.append(ft.dropdown.Option(
                data=n,
                text=n,
                on_click=self.readDDRivenditore
            ))
            self._view.txtOut.controls.append(ft.Text(F"{n}"))

        edges = self._model.getEdges()
        for e in edges:
            self._view.txtOut.controls.append(ft.Text(F"{e[2]['weight']}: {e[0]}<->{e[1]}"))


        self._view.update_page()


    def readDDRivenditore(self, e):
        if e.control.data is None:
            self._chosenRivenditore = None
        else:
            self._chosenRivenditore = e.control.data


    def handleAnalizza(self, e):
        self._view.txtOut.controls.clear()
        if self._chosenRivenditore is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un rivenditore!"))
            self._view.update_page()
            return

        dimConn, pesoArchiConn = self._model.analizzaGrafo(self._chosenRivenditore)
        self._view.txtOut.controls.append(ft.Text(f"La componente connessa ha dimensione: {dimConn}"))
        self._view.txtOut.controls.append(ft.Text(f"La somma dei pesi degli archi della componente connessa è: {pesoArchiConn}"))
        self._view.update_page()



