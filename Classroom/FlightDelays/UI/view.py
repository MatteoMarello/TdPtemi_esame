import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP Flights Manager 2024", color="blue", size=24)
        self._page.controls.append(self._title)

        self._txtInNumC = ft.TextField(label="Numeri compagnie", width=250)
        self._btnAnalizza = ft.ElevatedButton(on_click=self._controller.handleAnalizza, text="Analizza Aeroporti")
        self._btnConnessi = ft.ElevatedButton(text="Aeroporti Connessi", on_click=self._controller.handleConnessi)

        row1 = ft.Row(controls=[self._txtInNumC, self._btnAnalizza, self._btnConnessi], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1)

        self._ddAeroportoP = ft.Dropdown(label="Partenza")
        self._ddAeroportoA = ft.Dropdown(label="Arrivo")
        row2 = ft.Row(controls=[self._ddAeroportoP, self._ddAeroportoA], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self._txtInNumTratte = ft.TextField(label="Numero tratte Max", width=250)
        self._btnTestConnessione = ft.ElevatedButton(text="Test Connessione", on_click=self._controller.handleTestConnessione)
        self._btnCercaItinerario = ft.ElevatedButton(text='Cerca Itinerario', on_click=self._controller.handleCercaItinerario)

        row3 = ft.Row(controls=[self._txtInNumTratte, self._btnTestConnessione, self._btnCercaItinerario], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self._txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
