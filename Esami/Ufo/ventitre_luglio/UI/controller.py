import flet as ft
from Esami.Ufo.ventitre_luglio.model.model import Model
from Esami.Ufo.ventitre_luglio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        try:
            anno = int(self._view.txtInAnno.value)
        except ValueError:
            self._view.txtOut.controls.append(ft.Text("L'anno indicato non è un numero intero!"))
            self._view.update_page()
            return

        try: giorni = int(self._view.txtInxG.value)
        except ValueError:
            self._view.txtOut.controls.append(ft.Text("Il numero di giorni indicato non è un numero intero!"))
            self._view.update_page()
            return

        if anno == "" or giorni == "" or anno < 1906 or anno > 2014 or giorni < 1 or giorni > 180:
            self._view.txtOut.controls.append(ft.Text("Devi inserire un anno compreso tra 1906 e 2014 e un numero"
                                                      "di giorni compreso tra 1 e 180."))
            self._view.update_page()
            return


        self._model.buildGraph(anno,giorni)
        nN, nE = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nN}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nE}"))
        self._view.update_page()

    def handle_analizza(self, e):
        pesoArchiAdiacenti = self._model.getPesoArchiAdiacenti()
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Ecco l'elenco degli stati con il peso degli archi adiacenti:"))
        for s in pesoArchiAdiacenti:
            self._view.txtOut.controls.append(ft.Text(f"{s[0]} -- {s[1]}"))

        self._view.update_page()


