import flet as ft


class View():
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
        self._title = ft.Text("TdP 2024 - Esame 18/01/2022", color="purple", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls

        self.ddProvider = ft.Dropdown(label="Provider", width=300)
        self._controller.fillDDProvider()
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo",width=200, on_click=self._controller.handle_graph)
        row1=ft.Row([self.ddProvider, self.btn_graph], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInDistnza = ft.TextField(label="Distanza", width=300)
        self.btnAnalisiGrafo = ft.ElevatedButton(text="Analisi Grafo", width=200, on_click=self._controller.handle_analisi)
        row2=ft.Row([self.txtInDistnza, self.btnAnalisiGrafo], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInStringa = ft.TextField(label="Stringa", width=300)
        self._btnPercorso = ft.ElevatedButton(text="Calcola Percorso", width=200, on_click=self._controller.handlePercorso)
        row3=ft.Row([self.txtInStringa, self._btnPercorso], alignment=ft.MainAxisAlignment.CENTER)

        self.ddTarget = ft.Dropdown(label="Target", width=300)
        row4 = ft.Row([self.ddTarget, ft.Container(width=200)], ft.MainAxisAlignment.CENTER)

        self._page.add(row1,row2,row3,row4)

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
