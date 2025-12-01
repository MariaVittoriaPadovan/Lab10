import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        # controllo il costo inserito
        try:
            threshold_str = self._view.guadagno_medio_minimo.value
            if not threshold_str:#se la stringa è vuota
                self._view.show_alert("Devi inserire un valore numerico per la soglia.")
                return

            threshold = float(threshold_str)
            if threshold < 0:
                self._view.show_alert("La soglia deve essere un valore non negativo.")
                return

        except ValueError:
            self._view.show_alert("Il valore inserito non è un numero valido.")
            return


        self._model.costruisci_grafo(threshold) #creo il grafo

        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()
        tratte = self._model.get_all_edges()  # lista di (HubA, HubB, peso)

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hubs: {num_nodi}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte: {num_archi}")
        )

        if not tratte:
            self._view.lista_visualizzazione.controls.append(
                ft.Text("Nessuna tratta ha superato la soglia di guadagno medio.")
            )

        for hub_a, hub_b, peso in tratte:
            testo = f"{hub_a.nome} -> {hub_b.nome} -- guadagno Medio per Spedizione: € {peso} "
            self._view.lista_visualizzazione.controls.append(ft.Text(testo))

        self._view.update()
