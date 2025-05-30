import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    #popolo i DD
    def fillDD(self):
        # popolo il DD Year
        year = self._model.getAllYear()
        for y in year:
            self._view.ddyear.options.append(
                ft.dropdown.Option(
                    text=y
                ))
            self._view.update_page()

        # popolo il DD colore
        nazioni = self._model.getAllNazioni()
        for c in nazioni:
            self._view.ddcountry.options.append(
                ft.dropdown.Option(
                    text=c
                ))
            self._view.update_page()

    #creo il grafo
    def handle_graph(self, e):
        nazione = self._view.ddcountry.value
        if nazione is None:
            self._view.txt_result.controls.append(ft.Text("il campo non può essere vuoto"))
            self._view.update_page()
            return

        anno = self._view.ddyear.value
        if anno is None:
            self._view.txt_result.controls.append(ft.Text("il campo non può essere vuoto"))
            self._view.update_page()
            return

        # creo il grafo e stampa i suoi dati
        self._model.creaGrafo(nazione,anno)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"grafico creato"))
        nN, nE = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {nN} nodi e {nE} archi"))
        self._view.update_page()



    def handle_analizza(self, e):
        pass



    def handle_path(self, e):
        pass
