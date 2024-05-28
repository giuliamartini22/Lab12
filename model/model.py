import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._listYears = []
        self._listCountries = []
        self._idMap = {}
        self._grafo = nx.Graph()

    def buildGraph(self, country, year):
        self._grafo.edges.clear()
        self._nodi = DAO.getAllRetailers(country)
        print(len(self._nodi))
        for r in self._nodi:
            self._idMap[r.Retailer_code] = r
        #print(self._idMap)
        self._grafo.add_nodes_from(self._nodi)
    def getYears(self):
        self._listYears = DAO.getAllYears()
        return self._listYears

    def getCountries(self):
        self._listCountries = DAO.getAllCountries()
        return self._listCountries