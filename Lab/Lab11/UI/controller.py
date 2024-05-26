import time

import flet as ft

from Lab.Lab11.UI.view import View
from Lab.Lab11.model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []


    def fillDD(self):
        self._view._ddyear.options.append(ft.dropdown.Option("2015"))
        self._view._ddyear.options.append(ft.dropdown.Option("2016"))
        self._view._ddyear.options.append(ft.dropdown.Option("2017"))
        self._view._ddyear.options.append(ft.dropdown.Option("2018"))

        colors = self._model.getColors()
        for color in colors:
            self._view._ddcolor.options.append(ft.dropdown.Option(color))



    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        anno = self._view._ddyear.value
        color = self._view._ddcolor.value
        if anno is None or color is None:
            self._view.txtOut.controls.append(ft.Text("Devi selezionare un anno e un colore dal menù a tendina!"))
        else:
            self._model.buildGraph(anno, color)
            self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()}"))
            self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))
            first, sec, third = self._model.getThreeMostWeight()
            if first is None and sec is None and third is None:
                self._view.txtOut.controls.append(ft.Text(
                    f"Sono presenti meno di tre archi nel grafo :-("))
            else:
                self._view.txtOut.controls.append(ft.Text(f"Arco da {first[0].Product_number} a {first[1].Product_number}, peso: {first[2]["weight"]}"))
                self._view.txtOut.controls.append(
                    ft.Text(f"Arco da {sec[0].Product_number} a {sec[1].Product_number}, peso: {sec[2]["weight"]}"))
                self._view.txtOut.controls.append(
                    ft.Text(f"Arco da {third[0].Product_number} a {third[1].Product_number}, peso: {third[2]["weight"]}"))
                ripetuti = set()
                firstProduct = first[0].Product_number
                secProduct = first[1].Product_number
                lstFirstEdge = [firstProduct, secProduct]
                lstSecEdge = [sec[0].Product_number, sec[1].Product_number]
                lstThirdEdge = [third[0].Product_number, third[1].Product_number]
                for number in lstFirstEdge:
                    if number in lstThirdEdge or number in lstSecEdge:
                        ripetuti.add(number)
                for number in lstSecEdge:
                    if number in lstThirdEdge:
                        ripetuti.add(number)

                self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono {[num for num in ripetuti]}"))



        self.fillDDProduct()

        self._view.update_page()



    def fillDDProduct(self):
        self._view._ddnode.options.clear()
        for node in self._model._graph.nodes:
            self._view._ddnode.options.append(ft.dropdown.Option(text=node.Product_number,
                                                                 data=node,
                                                                 on_click=self.readProduct))



    def readProduct(self,e):
        if e.control.data is None:
            self._productDD = None
        else:
            self._productDD = e.control.data



    def handle_search(self, e):
        self._view.txtOut2.controls.clear()
        if self._productDD is None:
            self._view.txtOut2.controls.append(ft.Text("Devi prima selezionare un prodotto dal menù a tendina!"))
        else:
            start_time = time.time()
            lunghezzaPercorso = self._model.getPercorsoPiuLungo(self._productDD)
            end_time = time.time()
            self._view.txtOut2.controls.append(ft.Text(f'Numero archi percorso più lungo: {lunghezzaPercorso}'))
            self._view.txtOut2.controls.append(ft.Text(f'Elapsed time: {end_time-start_time}'))

        self._view.update_page()
