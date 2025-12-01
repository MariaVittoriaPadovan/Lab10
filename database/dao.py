from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def readAllHub():
        conn = DBConnect.get_connection()
        risultato = []
        query = ('''
        SELECT * 
        FROM hub
        ''')
        cursore = conn.cursor(dictionary=True)
        cursore.execute(query)
        for riga in cursore:
            hub = Hub(
                riga["id"],
                riga["codice"],
                riga["nome"],
                riga["citta"],
                riga["stato"],
                riga["latitudine"],
                riga["longitudine"])
            risultato.append(hub)
        cursore.close()
        conn.close()
        return risultato # Restituisco lista di oggetti Hub (DTO)

    @staticmethod
    def get_all_spedizioni():
        conn = DBConnect.get_connection()
        risultato = []
        query = "SELECT * FROM spedizione"
        cursore = conn.cursor(dictionary=True)
        cursore.execute(query)

        for riga in cursore:
            spedizione = Spedizione(
                riga["id"],
                riga["id_compagnia"],
                riga["numero_tracking"],
                riga["id_hub_origine"],
                riga["id_hub_destinazione"],
                riga["data_ritiro_programmata"],
                riga["distanza"],
                riga["data_consegna"],
                riga["valore_merce"]
            )
            risultato.append(spedizione)

        cursore.close()
        conn.close()
        return risultato

    @staticmethod
    def esisteConnessioneTra(u: Hub, v: Hub):
        # Verifica se esista una connessione tra nodo u e v
        conn = DBConnect.get_connection()
        risultato = []
        query = (''' 
        SELECT * 
        FROM spedizione s  
        WHERE s.id_hub_origine = %s AND s.id_hub_destinazione = %s
        ''')
        cursore = conn.cursor(dictionary=True)
        cursore.execute(query, (u.id, v.id))  # Parametri

        for riga in cursore:
            risultato.append(riga)

        cursore.close()
        conn.close()
        return risultato

    @staticmethod
    def cercaViciniAHub(u: Hub):
        # Cerco gli Hub collegati a quello passato come parametro, vedo tutte le spedizioni in uscita da un hub
        conn = DBConnect.get_connection()
        risultato = []
        query = '''
        SELECT * 
        FROM spedizione s 
        WHERE s.id_hub_origine = %s
        '''

        cursore = conn.cursor(dictionary=True)
        cursore.execute(query, (u.id,))  # Parametro con (, )
        for riga in cursore:
            spedizione = Spedizione(
                riga["id"],
                riga["id_compagnia"],
                riga["id_hub_origine"],
                riga["id_hub_destinazione"],
                riga["data_ritiro_programmata"],
                riga["distanza"],
                riga["data_consegna"],
                riga["valore_merce"]
            )
            risultato.append(spedizione)

        cursore.close()
        conn.close()
        return risultato