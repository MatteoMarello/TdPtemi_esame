import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multiDictionary = md.MultiDictionary()


    def handleSentence(self, txtIn, language):
        start_time = time.time()
        sentence = txtIn.split(" ")
        correct_sentence = []
        for word in sentence:
            word_lower = word.lower()
            word_correct = replaceChars(word_lower)
            correct_sentence.append(word_correct)

        richWords = self._multiDictionary.searchWord(correct_sentence, language)
        errors = [rw for rw in richWords if rw.corretta is False]
        print(f'La tua frase contiene {len(errors)} errori!')
        if len(errors)>0:
            print(f'Gli errori contenuti nella tua frase sono:')
            for err in errors:
                print(err)
        end_time = time.time()
        total_time = end_time-start_time
        print(f'Tempo di esecuzione: {total_time} secondi.')

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def creaDizionario(self, path, language):
        self._multiDictionary.add_Dizionario(path, language)

    def printDic(self,language):
        self._multiDictionary.printDic(language)


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%?^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text