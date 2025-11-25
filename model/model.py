from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO

        self._grafo = nx.Graph()
        for nodo in self._nodes:
            self._grafo.add_node(nodo)
''' vista dal prof ma come funziona?
        # SECONDO MODO, CON 619 QUERY A CERCARE I NODI VICINI
        conta = 0
        for u in self._grafo:
            connessioniAVicini = DAO.cercaViciniAHub(u)
            for spedizione in connessioniAVicini:
                HubArrivo = self._dizionario_fermate[spedizione.id_hub_origine]
                self._grafo.add_edge(u, fermataArrivo)
                print(f"Aggiunto arco tra {u} e {fermataArrivo}")
                print(len(self._grafo.edges()))

        print(self._grafo)
'''
    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO

