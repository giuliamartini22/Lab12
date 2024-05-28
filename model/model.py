import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._listYears = []
        self._listCountries = []
        self._idMap = {}
        self._grafo = nx.Graph()

    def buildGraph(self, country, year):
        #self._grafo.edges.clear()
        self._nodi = DAO.getAllRetailers(country)
        print(len(self._nodi))
        for r in self._nodi:
            self._idMap[r.Retailer_code] = r
        #print(self._idMap)
        self._grafo.add_nodes_from(self._nodi)
        self._addEdges(country, year)
        self.printGraphDetails()

    def _addEdges(self, country, year):
        allConnessioni = DAO.getAllEdges(country, year, self._idMap)
        for c in allConnessioni:
            v1 = c.R1
            v2 = c.R2
            peso = c.N
            if v1 in self._grafo and v2 in self._grafo:
                self._grafo.add_edge(v1, v2, weight=peso)

    def calcolaVolumeVendita(self):
        elencoVolumiVendita = []
        for v in self._grafo.nodes():
            elencoVolumiVendita = self.getVolumeVendita(v)
        return elencoVolumiVendita


    def getVolumeVendita(self, v0):
        vicini = self._grafo.neighbors(v0)
        #vicini = self._grafo.edges(v0)
        volumeVendita = 0
        viciniTuple = []
        for v in vicini:
            volumeVendita = volumeVendita + self._grafo[v0][v]["weight"]
            viciniTuple.append((v, volumeVendita))
        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple


    def printGraphDetails(self):
        print(f"Num Nodi: {len(self._grafo.nodes)}")
        print(f"Num archi: {len(self._grafo.edges)}")

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def getYears(self):
        self._listYears = DAO.getAllYears()
        return self._listYears

    def getCountries(self):
        self._listCountries = DAO.getAllCountries()
        return self._listCountries