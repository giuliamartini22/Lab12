import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._listCountry = self._model.getCountries()
        print(self._listCountry)
        for c in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(c[0]))
        self._view.update_page()

    def read_country(self, e):
        if e.control.value == "None":
            self._country = None
        else:
            self._country = e.control.value

    def populate_dd_anno(self):
        """methodo che popola la tendina con tutti gli anni in cui ci sono state vendite,
        prendendo le informazioni dal database"""
        self._listYear = self._model.getYears()
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def read_anno(self, e):
        """event handler che legge l'anno scelto dal menu a tendina ogniqualvolta viene cambiata
        la scelta, e lo memorizza in una variabile di instanza. L'anno è un intero, se si tratta di un anno,
        oppure un None se viene scelta l'opzione nessun filtro sull'anno"""
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value


    def handle_graph(self, e):
        country = self._view.ddcountry.value
        anno = self._view.ddyear.value
        try:
            countryIns = str(country)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Country non inserito"))
            self._view.update_page()
        try:
            annoIns = int(anno)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Anno non inserito"))
            self._view.update_page()

        self._model.buildGraph(countryIns, annoIns)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))
        self._view.update_page()




    def handle_volume(self, e):
        vicini = self._model.calcolaVolumeVendita()
        for v in vicini:
            self._view.txtOut2.controls.append(ft.Text(f"{v[0]} --> {v[1]}"))
        self._view.update_page()


    def handle_path(self, e):
        pass
