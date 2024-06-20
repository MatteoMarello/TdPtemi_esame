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
        self._title = ft.Text("TdP 2024 - Esame 04/09/2020", color="red", size=24)
        self._page.controls.append(self._title)

        self.txtInRank = ft.TextField(label="Rank", width=300)
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([self.txtInRank, self.btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1)
        self._page.add(ft.Row([ft.ElevatedButton(text="Film di Grado Massimo", width=500, on_click=self._controller.handleFilmGradoMassimo)], alignment=ft.MainAxisAlignment.CENTER))

        self.ddFilm = ft.Dropdown(label="Film", width=300)
        self.btnCamminoIncremento = ft.ElevatedButton(text="Cammino Incremento", width=200, on_click=self._controller.handleCamminoIncremento)
        row3 = ft.Row([self.ddFilm, self.btnCamminoIncremento], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

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
