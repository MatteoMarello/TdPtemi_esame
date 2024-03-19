from dictionary import Dictionary

class Translator:

    def __init__(self):
        self._dizionario = Dictionary()
        pass

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        file = open(dict, 'r')
        for line in file:
            tokens = line.strip().split(" ")
            parola_aliena = tokens[0]
            lista_traduzioni = tokens[1:]
            self._dizionario.creaDizionarioDaFile(parola_aliena, lista_traduzioni)

    def handleAdd(self, parola_aliena, lista_traduzioni):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        if self._dizionario.contains_parola_aliena(parola_aliena) == False:
            file_dizionario = open("dictionary.txt", 'a')
            string = ""
            for parola in lista_traduzioni:
                if string == "":
                    string += parola
                else:
                    string +=" "+parola
            file_dizionario.write(f'{parola_aliena} {string}\n')
            file_dizionario.close()
        else:
            self._dizionario.addWord(parola_aliena, lista_traduzioni)
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        parola_tradotta = self._dizionario.translate(query)
        return parola_tradotta

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        parole_tradotte = self._dizionario.translateWordWildCard(query)
        return parole_tradotte

    def getDictionaryString(self, nome_file):
        s = ""
        file = open(nome_file, 'r')
        for line in file:
            s+=line
        return s
