import flet as ft
from Esami.Duemilaventidue.diciotto_gennaio.model.model import Model
from Esami.Duemilaventidue.diciotto_gennaio.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.opzione_selected = None
        self.distanza_sel = None


    def fillDDProvider(self):
        elementi = self._model.get_provider()  # Recupera lista di elementi

        # Converte ciascun anno in una Option (occhio: map() da un iteratore, meglio usare list)
        listOfOptions = [
            ft.dropdown.Option(text=el, data=el)
            for el in elementi
        ]

        self._view.ddProvider.options = listOfOptions  # Assegna le opzioni al dropdown
        self._view.ddProvider.on_change = self.readDDValue  # Imposta il metodo da chiamare al cambio selezione
        self._view.update_page()

    def readDDValue(self, e):
        selected = e.control.value  # Prende il valore selezionato dal dropdown (es. "2003")
        self.opzione_selected = selected
        print(f"Hai selezionato l'anno: {selected}")




    def fillDDLocalita(self):
        pass

    def handle_graph(self, e):
        distanza_selezionata = self._view.txtInDistnza.value
        try:
            self.distanza_sel = float(distanza_selezionata)
            print(f"Hai selezionato distanza: {distanza_selezionata}")
        except:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("errore", color="blue"))
            self._view.update_page()
        self._model.build_graph(self.opzione_selected, self.distanza_sel)
        n, a = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"i nodi sono: {n}, gli archi sono{a}"))
        self._view.update_page()



    def handle_analisi(self, e):
        listaVicini = self._model.getVerticiParticolari()
        self._view.txtOut.controls.append(
            ft.Text(f"Dettagli : {'\n '.join(str(d) for d in listaVicini)}")
        )
        self._view.update_page()




    def handlePercorso(self, e):
        pass


    def readDDLoc(self, e):
        pass
