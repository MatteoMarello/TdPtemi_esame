class Dictionary:
    def __init__(self):
        self._dizionario = {}

    def addWord(self, parola_aliena, traduzioni):
        traduzioni_presenti = self._dizionario.get(parola_aliena)
        nuove_traduzioni = ""
        for traduzione in traduzioni:
            nuove_traduzioni += " " + traduzione
        print(nuove_traduzioni)
        traduzioni_da_inserire = traduzioni_presenti + nuove_traduzioni
        self._dizionario[parola_aliena] = traduzioni_da_inserire
        file = open("dictionary.txt", 'w')
        for key, value in self._dizionario.items():
            if key is not None and value is not None:
                string = key+" "+value
                file.write(string+"\n")
        file.close()
        pass

    def translate(self, query):
        return self._dizionario.get(query)
        # Il metodo .get(key) posso utilizzarlo sui dizionari. Gli passo una chiave come input e mi ritorna il valore associato
        # a quella chiave all'interno del dizionario. Se non esiste la chiave nel dizionario, restituisce None.

    def translateWordWildCard(self, query):
        tokens = list(query) # Applicare list() su una stringa mi permette di ottenere una lista di tutti i caratteri della lista
        numero_lettere = len(tokens)
        lista_traduzioni_possibili = []
        for key in self._dizionario.keys():
            caratteri = list(key)
            if len(caratteri) == numero_lettere:
                cnt = 0
                for i in range(0, numero_lettere):
                    if tokens[i] == caratteri[i]:
                        cnt += 1
                if cnt == numero_lettere-1:
                    lista_traduzioni_possibili.append(self._dizionario.get(key))
        return lista_traduzioni_possibili

    def contains_parola_aliena(self, parola_aliena):
        if self._dizionario.get(parola_aliena) != None:
            return True
        else:
            return False

    def creaDizionarioDaFile(self, parola_aliena, lista_traduzioni):
        string_traduzioni = ""
        for element in lista_traduzioni:
            if string_traduzioni=="":
                string_traduzioni = element
            else:
                string_traduzioni+= " " + element
        self._dizionario[parola_aliena] = string_traduzioni
        pass

