import copy
from time import time
from functools import lru_cache

class Model:
    def __init__(self):
        self.anagrammi = set()
        self.anagrammi_list = []

    def calcola_anagrammi(self, parola):
        self.anagrammi = set()
        self.ricorsione("", "".join(sorted(parola)))
        return self.anagrammi

    def calcola_anagrammi_list(self, parola):
        self.anagrammi = set()
        self.ricorsione_list([], parola)
        return self.anagrammi_list

    @lru_cache(maxsize=None)
    # La cache mi aiuta se la parola ha tante lettere uguali tra loro, altrimenti, se ad esempio è formata da tutte
    # lettere diverse, l'efficienza del metodo ricorsivo con l'utilizzo o meno della cache sarà la medesima!
    def ricorsione(self, parziale, lettere_rimanenti):
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self.anagrammi.add(parziale)
            return
        else:
            # Caso non terminale: dobbiamo provare ad aggiungere
            # una lettera per volta, e andare avanti nella ricorsione
            for i in range(0,len(lettere_rimanenti)):
                parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.ricorsione(parziale, nuove_lettere_rimanenti)
                parziale = parziale[:-1]

    def ricorsione_list(self, parziale: list, lettere_rimanenti):
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self.anagrammi_list.append(copy.deepcopy(parziale))
            return
        else:
            # Caso non terminale: dobbiamo provare ad aggiungere
            # una lettera per volta, e andare avanti nella ricorsione
            for i in range(0, len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.ricorsione_list(parziale, nuove_lettere_rimanenti)
                parziale.pop()

if __name__ == "__main__":
    model = Model()
    start_time = time()
    print(model.calcola_anagrammi("casas"))
    end_time = time()
    print(f'Elapsed time: {end_time-start_time}s')


    print(model.calcola_anagrammi_list("casa"))