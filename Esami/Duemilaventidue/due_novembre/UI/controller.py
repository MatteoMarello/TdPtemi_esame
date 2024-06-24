import flet as ft
from Esami.Duemilaventidue.due_novembre.UI.view import View
from Esami.Duemilaventidue.due_novembre.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        generi = self._model.getGeneri()
        for g in generi:
            self._view.ddGenere.options.append(ft.dropdown.Option(g))

        self._view.update_page()


    def handleGrafo(self, e):
        self._view.txtOut.controls.clear()
        dMinS = self._view.txtInMin.value
        dMaxS = self._view.txtInMax.value
        genere = self._view.ddGenere.value
        try:
            intDMinS = int(dMinS)
            intDMaxS = int(dMaxS)

        except ValueError:
            self._view.txtOut.controls.append(ft.Text("La durata dei brani deve essere un intero!"))
            self._view.update_page()
            return

        if genere is None or genere == "":
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un genere dal dropdown!"))
            self._view.update_page()
            return


        dMinMs = intDMinS * 1000
        dMaxMs = intDMaxS * 1000

        connComp = self._model.buildGraph(genere, dMinMs, dMaxMs)
        nN,nE = self._model.graphDetails()
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))

        for comp in connComp:
            self._view.txtOut.controls.append(ft.Text(f"Componente con {comp[0]} vertici, inseriti in {comp[1]} playlist."))
        self._view.update_page()



    def handlePlaylist(self, e):
        self._view.txtOut.controls.clear()
        dTOT = self._view.txtInD.value
        try:
            intdTot = int(dTOT)

        except ValueError:
            self._view.txtOut.controls.append(ft.Text("Devi inserire un numero intero!"))
            self._view.update_page()
            return

        dTOTMs = intdTot * 1000
        playlist, durata = self._model.getPlaylist(dTOTMs)

        self._view.txtOut.controls.append(ft.Text(f"La durata della playlist è di {durata} secondi."))
        for p in playlist:
            self._view.txtOut.controls.append((ft.Text(f"{p}")))

        self._view.update_page()



