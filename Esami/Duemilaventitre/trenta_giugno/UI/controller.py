import flet as ft
from Esami.Duemilaventitre.trenta_giugno.model.model import Model
from Esami.Duemilaventitre.trenta_giugno.UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._teamSelected= None

    def fillDDTeams(self):
        """Popola il dropdown con le squadre disponibili."""
        teams = self._model.get_teams()

        # Crea le opzioni del dropdown: text=nome, data=ID
        self._view.ddSquadra.options = [
            ft.dropdown.Option(text=str(team[1]), data=team[0])
            for team in teams
        ]

        # Configura il callback per la selezione
        self._view.ddSquadra.on_change = self.readDDTeamsValue
        self._view.update_page()

    def readDDTeamsValue(self, e):
        """Gestisce la selezione di una squadra dal dropdown."""
        if not e.control.value:
            return

        selected_text = e.control.value
        selected_team_id = None

        # Cerca l'ID della squadra selezionata
        for option in e.control.options:
            if option.text == selected_text:
                selected_team_id = option.data
                break

        if selected_team_id is not None:
            self._teamSelected = selected_team_id
            print(f"Squadra selezionata: {selected_text} (ID: {selected_team_id})")
        else:
            print(f"Errore: squadra '{selected_text}' non trovata")

    def handle_graph(self, e):
        if self._teamSelected is None:
            self.mostra_errore_selezione()
        self._model.build_graph(self._teamSelected)
        n, a = self._model.getGraphDetails()
        self._view.txtOut.controls.append(ft.Text(f"numero nodi:{n}, numero archi:{a}"))
        self._view.update_page()


    def handleDettagli(self):
        pass



    def mostra_errore_selezione(self):
        # Svuota la ListView
        self._view.txtOut.controls.clear()

        # Aggiunge un messaggio carino di errore
        self._view.txtOut.controls.append(
            ft.Text(
                "⚠️ Per favore, seleziona un opzione!",
                color="red",
                size=16,
                italic=True,
                weight=ft.FontWeight.BOLD
            )
        )

        # Aggiorna la pagina per riflettere i cambiamenti
        self._view.update_page()
