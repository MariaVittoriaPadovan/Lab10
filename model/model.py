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

        self.G = nx.Graph() #reset del grafo

        self._nodes=DAO.readAllHub() #carico gli hub

        dizionario_hub={} #id_hub : oggetto Hub
        for nodo in self._nodes:
            dizionario_hub[nodo.id]=nodo

        #aggiungo i nodi
        for nodo in self._nodes:
            self.G.add_node(nodo)

        self._edges=DAO.get_all_spedizioni() #carico tutte le spedizioni

        #raggruppo tutte le spedizioni tra due archi in entrambe le direzioni(da A a B e da B ad A)
        # in un'unica tratta per poter calcolare il guadagno medio di una signola tratta
        tratte={} #la chiave è la tratta (ida,idb) : il valore è la lista dei valori_merce(di tutte le spedizioni tra quei due hub)
        for spedizione in self._edges:
            A = spedizione.id_hub_origine
            B = spedizione.id_hub_destinazione

            tratta = (min(A, B), max(A, B))

            if tratta not in tratte:
                tratte[tratta] = []
            tratte[tratta].append(spedizione.valore_merce)

        #creo gli archi
        #uso il metodo dizionario.items() che restituisce gli elementi del dizionario
        # come una lista di tuple (chiave, valore) su cui posso iterare
        for (ida, idb), valori in tratte.items(): #chiave=(ida,idb) : valori= lista dei valori_merce
            media = sum(valori) / len(valori)

            if media >= threshold:
                #uso il metodo dizionario.get() per accedere al valore associato alla chiave
                hubA = dizionario_hub.get(ida)
                hubB = dizionario_hub.get(idb)

                if hubA and hubB:
                    self.G.add_edge(hubA, hubB, weight=media) #aggiungo l'arco


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        lista_tratte = []
        for u, v, d in self.G.edges(data=True):
            # u e v sono gli oggetti Hub, d è un dizionario con gli attributi
            lista_tratte.append((u, v, d['weight']))
        return lista_tratte


