class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        file = open(path, 'r')
        for line in file:
            self._dict.append(line.strip())
        return self._dict

    def printAll(self):
        print("Le parole contenute nel dizionario sono:\n")
        for element in self._dict:
            print(element)


    @property
    def dict(self):
        return self._dict