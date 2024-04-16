import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab 6 - Analizza Vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btnTopVendite = None
        self.btnAnalizzaVendite = None
        self.lv = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self.dd_anno = ft.Dropdown(width=200, label="Anno", options=[ft.dropdown.Option("Nessun filtro")])
        self.controller.loadYears(self.dd_anno)

        self.dd_brand = ft.Dropdown(width=200, label="Brand", options=[ft.dropdown.Option("Nessun filtro")])
        self.controller.loadBrands(self.dd_brand)

        self.dd_retailer = ft.Dropdown(width=350, label="Retailer", options=[ft.dropdown.Option("Nessun filtro")])
        self.controller.loadRetailers(self.dd_retailer)

        self.row1 = ft.Row(controls=[self.dd_anno, self.dd_brand, self.dd_retailer], alignment=ft.MainAxisAlignment.CENTER)

        self.btnTopVendite = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handleTopVendite)
        self.btnAnalizzaVendite = ft.ElevatedButton(text="Analizza Vendite", on_click=self.controller.handleAnalizzaVendite)
        self.row2 = ft.Row(controls=[self.btnTopVendite, self.btnAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)

        self.lv = ft.ListView()
        self._page.add(self._title, self.row1, self.row2, self.lv)
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
