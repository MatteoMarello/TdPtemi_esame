from time import time
from functools import lru_cache
class Fibonacci:

    def __init__(self):
        # Effettuo il caching: inizializzo la lista con i due valori, validi quando n=0 o n=1.
        self.cache = {0: 0, 1: 1}

    def calcola_elemento(self, n):
        # Ci sono due condizioni terminali
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)


    def calcola_elemento_cache(self, n):
        # Con la cache la condizione terminale si verifica se n è un numero per cui ho già calcolato
        # la funzione ricorsiva e quindi ho salvato il risultato nella cache.
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2))
            return self.cache[n]

    @lru_cache(maxsize=None) # Con maxsize=None, la lru_cache si salva tutti i risultati, non solo gli ultimi.
    def calcola_elemento_lru(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.calcola_elemento_lru(n-1) + self.calcola_elemento_lru(n-2)


if __name__ == "__main__":
    N = 40
    fib = Fibonacci()
    start_time = time()
    elemento = fib.calcola_elemento(N)
    end_time = time()
    print(f"L'elemento {N} della sequenza è {elemento}")
    print(f"Elapsed time {end_time-start_time}s\n")


    start_time = time()
    elemento = fib.calcola_elemento_cache(N)
    end_time = time()
    print(f"L'elemento {N} della sequenza è {elemento}")
    print(f"Elapsed time with homemade cache {end_time-start_time}\n")

    start_time = time()
    elemento = fib.calcola_elemento_lru(N)
    end_time = time()
    print(f"L'elemento {N} della sequenza è {elemento}")
    print(f"Elapsed time with lru_cache {end_time-start_time}s")