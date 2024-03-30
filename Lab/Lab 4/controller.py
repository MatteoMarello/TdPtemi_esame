import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = ""
        language = language.lower()
        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if parola.corretta == False:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


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


    def verifyLanguage(self,e):
        languages = ["Spanish", "Italian", "English"]
        language = self._view._langDD.value

        if language in languages:
            self._view._txtLanguage.visible = True
            self._view._txtLanguage.value = ""
            self._view._txtLanguage.value = f'You\'ve selected the {language} language!'
            self._view.update()
        else:
            self._view._txtLanguage.visible = True
            self._view._txtLanguage.value = ""
            self._view._txtLanguage.value = f'The selected language is not available!'
            self._view._txtLanguage.color = "red"
            self._view.update()

    def verifySearch(self,e):
        searchTypes = ['Default', 'Linear', 'Dichotomic']
        searchType = self._view._searchDD.value

        if searchType in searchTypes:
            self._view._txtSearch.visible = True
            self._view._txtSearch.value = ""
            self._view._txtSearch.value = f'You\'ve selected the {searchType} search type!'
            self._view.update()
        else:
            self._view._txtSearch.visible = True
            self._view._txtSearch.value = ""
            self._view._txtSearch.value = f'The selected search type is not available!'
            self._view._txtSearch.color = "red"
            self._view.update()

    def handleSpellCheck(self,e):
        language = self._view._langDD.value
        if language is None:
            self._view._txtError.visible = True
            self._view._txtError.value = ""
            self._view._txtError.value = f'You must choose a language!'
            self._view._txtError.color = "red"
            self._view.update()
            return
        else:
            self._view._txtError.visible = False
            self._view.update()

        searchType = self._view._searchDD.value
        if searchType is None:
            self._view._txtError.visible = True
            self._view._txtError.value = ""
            self._view._txtError.value = f'You must choose a search type!'
            self._view._txtError.color = "red"
            self._view.update()
            return
        else:
            self._view._txtError.visible = False
            self._view.update()

        txtInput = self._view._txtFieldSentence.value
        bad_words, time = self.handleSentence(txtInput, language, searchType)

        if len(self._view._lvOut.controls) != 0:
            self._view._lvOut.controls.append(ft.Text('----------------------------------------------------'))
        self._view._lvOut.controls.append(ft.Text(f'Your sentence: {txtInput}'))
        self._view._txtFieldSentence.value = ""
        self._view._lvOut.controls.append(ft.Text(f'Incorrect words: {bad_words}'))
        self._view._lvOut.controls.append(ft.Text(f'Time requested with the {searchType} research: {time}'))

        self._view.update()



def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text