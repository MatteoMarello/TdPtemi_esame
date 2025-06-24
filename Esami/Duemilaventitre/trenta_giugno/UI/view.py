import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._page.theme_mode = ft.ThemeMode.LIGHT

        self._controller = None
        self._title = None

    def load_interface(self):
        self._title = ft.Text("TdP 2024 - Esame 30/6/23", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddSquadra = ft.Dropdown(label="Squadra", width=300)
        self._controller.fillDDTeams()
        self.btn_graph = ft.ElevatedButton(
            text="Crea Grafo",
            width=200,
            on_click=self._controller.handle_graph
        )
        row1 = ft.Row([self.ddSquadra, self.btn_graph], alignment=ft.MainAxisAlignment.CENTER)

        self.ddAnno = ft.Dropdown(label="Anno", width=300)
        self.btnDettagli = ft.ElevatedButton(
            text="Dettagli",
            width=200,
            on_click=self._controller.handleDettagli
        )
        row2 = ft.Row([self.ddAnno, self.btnDettagli], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)

        self.txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
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
