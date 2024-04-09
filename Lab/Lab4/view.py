import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        # Row 1
        self._txtLanguage = ft.Text("", color="green", visible=False)
        self._langDD = ft.Dropdown(
            label="Select language",
            hint_text="Which language would you like to try?",
            options=[
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Spanish"),
            ],
            autofocus=True,
            width=760,
            on_change=self.__controller.verifyLanguage
        )

        self._row1 = ft.Row([self._langDD])

        # Row 2
        self._txtSearch = ft.Text("", color="green", visible=False)
        self._searchDD = ft.Dropdown(
            label="Search modality",
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic"),
            ],
            autofocus=True,
            width=180,
            on_change=self.__controller.verifySearch
        )

        self._txtFieldSentence = ft.TextField(label="Write your sentence",
                                              width=450)

        self._btnSpellcheck = ft.ElevatedButton(text="Spellcheck",
                                                on_click=self.__controller.handleSpellCheck)

        self._row2 = ft.Row([self._searchDD, self._txtFieldSentence, self._btnSpellcheck])

        # Row 3
        self._txtError = ft.Text(visible=False)

        # Row 4
        self._lvOut = ft.ListView(expand=1,spacing=10,padding=20,auto_scroll=True)


        self.page.add(self._row1, self._txtLanguage, self._row2, self._txtSearch, self._txtError, self._lvOut)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
