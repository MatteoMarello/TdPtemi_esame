import flet as ft
from Esami.Duemilaventidue.ventiquattro_maggio.model.model import Model
from Esami.Duemilaventidue.ventiquattro_maggio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def fillDDGeneri(self):
        generi = self._model.getGeneri()
        for g in generi:
            self._view.ddGenere.options.append(ft.dropdown.Option(g))



    def handleGrafo(self, e):
        self._view.txtOut.controls.clear()
        g = self._view.ddGenere.value
        self._model.buildGraph(g)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {nN} vertici."))
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {nE} archi."))
        self.fillDDTracks()
        self._view.update_page()


    def fillDDTracks(self):
        tracks = self._model.getTracks()
        for t in tracks:
            self._view.ddCanzoni.options.append(ft.dropdown.Option(
                data=t,
                text=t,
                on_click=self.readDDTrack
            ))

    def readDDTrack(self, e):
        if e.control.data is None:
            self.chosenTrack = None
        else:
            self.chosenTrack = e.control.data


    def handleDeltaMax(self, e):
        self._view.txtOut.controls.clear()
        deltaMax = self._model.getDeltaMax()
        self._view.txtOut.controls.append(ft.Text("Canzoni con Delta massimo:"))

        for edge in deltaMax:
            self._view.txtOut.controls.append(ft.Text(f"{edge[0]} --> {edge[1]}. Delta: {edge[2]["weight"]}"))

        self._view.update_page()


    def handleLista(self, e):
        memoriaMax = int(self._view.txtInMemoria.value)
        lista, memoria = self._model.getLista(self.chosenTrack, memoriaMax)
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text(f"La lista di canzoni trovata occuperà una memoria di {memoria} bytes."))
        for t in lista:
            self._view.txtOut.controls.append(ft.Text(f"{t}"))

        self._view.update_page()
