import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self._listaDizionari = {}


    def printDic(self, language):
        for element in self._listaDizionari[language]:
            print(element)
        pass

    def searchWord(self, words, language):
        richWords = []
        dizionario = self.getDizionario(language)
        for word in words:
            richword = rw.RichWord(word)
            if word in dizionario:
                richword.corretta = True
            else:
                richword.corretta = False
            richWords.append(richword)
        return richWords

    def searchWordLinear(self, words, language):
        richWords = []
        dizionario = self.getDizionario(language)
        for word in words:
            richword = rw.RichWord(word)
            corretta = False
            for element in dizionario:
                if word == element:
                    richword.corretta = True
                    richWords.append(richword)
                    corretta = True
                    break
            if not corretta:
                richword.corretta = False
                richWords.append(richword)
        return richWords

    def searchWordDichotomic(self, words, language):
        richWords = []
        dizionario = self.getDizionario(language)
        if len(dizionario) % 2 == 0:
            indiceMetaDizionario = int(len(dizionario)/2)
        else:
            indiceMetaDizionario = int((len(dizionario) + 1) / 2)
        for word in words:
            richword = rw.RichWord(word)
            corretta = False
            if word == dizionario[indiceMetaDizionario]:
                corretta = True
            else:
                if word < dizionario[indiceMetaDizionario]:
                    for i in range(0, indiceMetaDizionario):
                        if word == dizionario[i]:
                            corretta = True
                            richword.corretta = True
                            richWords.append(richword)
                            break
                else:
                    for j in range(indiceMetaDizionario+1, len(dizionario)):
                        if word == dizionario[j]:
                            corretta = True
                            richword.corretta = True
                            richWords.append(richword)
                            break
            if not corretta:
                richword.corretta = False
                richWords.append(richword)

        return richWords


    def add_Dizionario(self, path, language):
        dict = d.Dictionary()
        lista_dict = dict.loadDictionary(path)
        self._listaDizionari[language] = lista_dict

    def getDizionario(self, language):
        return self._listaDizionari.get(language)

