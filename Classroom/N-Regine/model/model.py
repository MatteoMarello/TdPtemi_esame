import copy
from time import time
class Model:
    def __init__(self):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []

    def risolvi_n_regine(self, N):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []
        parziale = []
        self._ricorsione(parziale, N)


    def _ricorsione(self, parziale, N):
        self.N_iterazioni += 1
        # Condizione terminale
        if len(parziale) == N:
            if self._soluzione_nuova(parziale):
                print(parziale)
                self.N_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
        # Caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row, col))
                    if self._regina_ammissibile(parziale):
                        # Ora passo alla ricorsione di livello 2.
                        self._ricorsione(parziale, N)
                    # Bisogna fare il backtracking.
                    parziale.pop() # il .pop() rimuove l'ultimo elemento della lista


    def _regina_ammissibile(self, parziale):
        if len(parziale)==1:
            return True
        else:
            ultima_regina = parziale[-1]
            for regina in parziale[:len(parziale)-1]:
                # controllo righe
                if ultima_regina[0] == regina[0]:
                    return False

                # controllo colonne
                if ultima_regina[1] == regina[1]:
                    return False

                # controllo diagonali
                if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                    return False
                if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                    return False
                # Modo per controllare se sono presenti altre regine sulle diagonali.
                # Per vedere se vale questa cosa sulle diagonali verso il basso, uso la prima condizione, in cui la differenza
                # tra la riga e la colonna delle due regine è uguale. Se invece voglio verficare la presenza di altre regine
                # sulle diagonali "negative", verso l'alto, dovrò verificare se la somma tra gli indici di riga e colonna delle
                # due regine è uguale.
        return True


    def _soluzione_nuova(self, soluzione_nuova):
        # controllo tutte le soluzioni precedenti
        for soluzione in self.soluzioni:
            # per ogni regina della nuova soluzione, controllo se è una
            # configurazione vecchia o no
            for regina in soluzione_nuova:
                if regina in soluzione:
                    return False
        return True


if __name__ == "__main__":
    model = Model()
    start_time = time()
    model.risolvi_n_regine(5)
    end_time = time()
    print(f"L'algoritmo ha trovato {model.N_soluzioni} soluzioni")
    print(f"L'algoritmo ha chiamato la funzione ricorsiva {model.N_iterazioni} volte")
    print(f"L'algoritmo ha impiegato {end_time-start_time} secondi")