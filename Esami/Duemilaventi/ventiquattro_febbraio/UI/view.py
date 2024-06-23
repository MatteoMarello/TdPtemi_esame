import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None


    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Esame 24/2/21", color="red", size=24)
        self._page.controls.append(self._title)

        self.ddMatch = ft.Dropdown(label="Match", width=300)
        self._controller.fillDD()
        self.btnGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handleGrafo)
        row1=ft.Row([self.ddMatch, self.btnGrafo], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        row2=ft.Row([ft.Container(width=300), ft.ElevatedButton(text="Giocatore Migliore", width=200, on_click=self._controller.handleGiocatoreMigliore)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self.txtOut= ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut)
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
