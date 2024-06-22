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
        self._title = ft.Text("TdP 2024 - Esame 3/6/24", color="green", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.txtInGoal = ft.TextField(label="Goal fatti", width=300)
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([self.txtInGoal, self.btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER)

        self.btnTopPlayer = ft.ElevatedButton(text="Top Player", width=500, on_click=self._controller.handleToplPlayer)
        row2 = ft.Row([self.btnTopPlayer], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInGiocatori = ft.TextField(label="Giocatori", width=300)
        self.btnDreamTeam = ft.ElevatedButton(text="Dream Team", width=200, on_click=self._controller.handleDreamTeam)
        row3 = ft.Row([self.txtInGiocatori, self.btnDreamTeam], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, row3)


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
