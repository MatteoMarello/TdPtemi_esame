import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        # Row 1
        self._dd = ft.Dropdown(width=550, label="Seleziona un corso")
        self._controller.aggiungiCorsi(self._dd)

        self._btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handleCercaIscritti)

        self._row1 = ft.Row([self._dd, self._btnCercaIscritti], alignment=ft.MainAxisAlignment.CENTER)

        # Row 2

        self._textFieldMatricola = ft.TextField(label="Matricola", width=180)
        self._textFieldNome = ft.TextField(label="Nome", read_only=True, width=270)
        self._textFieldCognome = ft.TextField(label="Cognome", read_only=True, width=270)

        self._row2 = ft.Row([self._textFieldMatricola, self._textFieldNome, self._textFieldCognome], alignment=ft.MainAxisAlignment.CENTER)

        # Row 3

        self._btnCercaStudente =ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handleCercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handleCercaCorsi)
        self._btnIscriviStudente = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handeIscrizione)

        self._row3 = ft.Row(controls=[self._btnCercaStudente, self._btnCercaCorsi, self._btnIscriviStudente], alignment=ft.MainAxisAlignment.CENTER)

        # Row 4

        self._lv = ft.ListView(expand=1, spacing=10, padding=20)


        self._page.add(self._title, self._row1, self._row2, self._row3, self._lv)


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()


