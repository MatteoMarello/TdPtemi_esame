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
        self._title = ft.Text("TdP 2024 - Esame 2/11/2022", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddGenere = ft.Dropdown(label="Genere", width=500)
        self._controller.fillDD()
        row1 = ft.Row([self.ddGenere], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInMin = ft.TextField(label="Min", width=250)
        self.txtInMax = ft.TextField(label="Max", width=250)
        row2 = ft.Row([self.txtInMin, self.txtInMax], alignment=ft.MainAxisAlignment.CENTER)

        self.btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", width=500, on_click=self._controller.handleGrafo)
        row3 = ft.Row([self.btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInD = ft.TextField(label="dTOT", width=250)
        self.btnPlaylist = ft.ElevatedButton(text="La mia Playlist", width=250, on_click=self._controller.handlePlaylist)
        row4 = ft.Row([self.txtInD, self.btnPlaylist], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, row3, row4)



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
