import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")
    print("\nCosa vorresti fare?")
    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        pattern_corretto = False
        print("Ok, quale parola devo aggiungere?")
        parola_aliena = ""
        traduzioni_italiano = []
        while not pattern_corretto:
            parola_da_inserire = input()
            parola_traduzione = parola_da_inserire.split(" ")
            parola_aliena = parola_traduzione[0].lower()
            traduzioni_italiano = parola_traduzione[1:]
            if not parola_aliena.isalpha():
                print("Il pattern seguito è sbagliato! Devi inserire la parola aliena a la/e traduzione/i in italiano, separate da una spazio!")
            else:
                pattern_corretto = True
            for parola in traduzioni_italiano:
                if parola.isalpha() == False:
                    print("Il pattern seguito è sbagliato! Devi inserire la parola aliena a la/e traduzione/i in italiano, separate da una spazio!")
                    pattern_corretto = False

        t.handleAdd(parola_aliena, traduzioni_italiano)
        print("Parola inserita con successo!")
        pass

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        parola_da_cercare = input().lower()
        if parola_da_cercare.isalpha():
            # .isalpha() è un metodo che restituisce True se la stringa sulla quale lo applico contiene solamente lettere (senza numeri!)
            parola_tradotta = t.handleTranslate(parola_da_cercare)
            if parola_tradotta is None:
                print("Non esiste una traduzione per la parola cercata!")
            else:
                print(f'La traduzione di {parola_da_cercare} è {parola_tradotta}!\n')
        else:
            print("Puoi inserire solamente parole contenente lettere, e non numeri!")
        pass

    if int(txtIn) == 3:
        print("Inserisci una parola con una wildcard: un solo ? è permesso per parola!\n")
        parola_aliena = input().lower()
        parole_tradotte = t.handleWildCard(parola_aliena)
        if len(parole_tradotte) == 1:
            print(f'La traduzione della parola cercata sembrerebbe essere {parole_tradotte[0]}')
        else:
            num_trad = len(parole_tradotte)
            print(f'Le possibili traduzioni per la parola cercata sono:')
            for i in range(0,num_trad):
                print(f'{i+1}) {parole_tradotte[i]}')

        print()
        pass

    if int(txtIn) == 4:
        print("Ecco a te il dizionario completo, con tutte le parole aliene e la rispettiva traduzione in italiano!")
        string = t.getDictionaryString("dictionary.txt")
        print(string)
        print()
        pass

    if int(txtIn) == 5:
        break
