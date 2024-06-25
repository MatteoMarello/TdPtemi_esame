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

        self.ddyear = None
        self.ddcountry = None
        self.txtN = None

        self.btn_graph = None
        self.btn_volume = None
        self.btn_path = None

        self.txt_result = None
        self.txtOut2 = None
        self.txtOut3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Lab12: Prova tema d'esame", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.txtInNCanzoni = ft.TextField(label="Canzoni", width=300)
        self.btnGrafo = ft.ElevatedButton(text="Crea Grafo", width=200, on_click=self._controller.handleGrafo)
        row1 = ft.Row([self.txtInNCanzoni, self.btnGrafo], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        self.ddA1 = ft.Dropdown(label="Album a1", width=300)
        self.btnAdiacenze = ft.ElevatedButton(text="Stampa Adiacenze", width=200, on_click=self._controller.handleStampaAdiacenze)
        row2=ft.Row([self.ddA1, self.btnAdiacenze], alignment=ft.MainAxisAlignment.CENTER)

        self.ddA2 = ft.Dropdown(label="Album a2", width=300)
        self.btnPercorso = ft.ElevatedButton(text="Calcola Percorso", width=200, on_click=self._controller.handlePercorso)
        row3 = ft.Row([self.ddA2, self.btnPercorso], alignment=ft.MainAxisAlignment.CENTER)

        self.txtInSoglia = ft.TextField(label="Soglia", width=500)
        row4 = ft.Row([self.txtInSoglia], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row2,row3,row4)

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
