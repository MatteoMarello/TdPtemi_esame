class QuickSort():

    def sort(self, sequenza):
        if len(sequenza) <= 1:
            return sequenza
        else:
            # 1) Scegliere pivot
            pivot = sequenza[0] # scelgo il primo elemento della lista come pivot

            # 2) Dividere la lista in sottoliste
            sequenza_smaller = []
            for i in range(1, len(sequenza)):
                if sequenza[i] < pivot:
                    sequenza_smaller.append(sequenza[i])

            sequenza_pivot = [n for n in sequenza if n == pivot]

            sequenza_larger = [n for n in sequenza if n > pivot]

            # 3) Fare il sort delle sottoliste e appendere i risultati

            return (self.sort(sequenza_smaller) +
                    sequenza_pivot +
                    self.sort(sequenza_larger))



if __name__ == "__main__":
    quicksort = QuickSort()
    sequenza = [3, 5, 0, 2, 11 ,31, 4, 7]
    sequenza_ordinata = quicksort.sort(sequenza)
    print(f'Sequenza non ordinata: {sequenza}')
    print(f'Sequenza ordinata : {sequenza_ordinata}')

