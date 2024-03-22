import spellchecker


sc = spellchecker.SpellChecker()
sc.creaDizionario(f'resources/English.txt', 'english')
sc.creaDizionario(f'resources/Spanish.txt', 'spanish')
sc.creaDizionario(f'resources/Italian.txt', 'italian')


while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        print("------------------------------------------------")
        print("Using Contains")
        sc.handleSentence(txtIn,"italian")
        print("------------------------------------------------")
        print("Using Linear Research")
        sc.handleSentenceLinear(txtIn, "italian")
        print("------------------------------------------------")

        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        print("------------------------------------------------")
        print("Using Contains")
        sc.handleSentence(txtIn,"english")
        print("------------------------------------------------")
        print("Using Linear Research")
        sc.handleSentenceLinear(txtIn, "english")
        print("------------------------------------------------")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        print("------------------------------------------------")
        print("Using Contains")
        sc.handleSentence(txtIn,"spanish")
        print("------------------------------------------------")
        print("Using Linear Research")
        sc.handleSentenceLinear(txtIn, "spanish")
        print("------------------------------------------------")
        continue

    if int(txtIn) == 4:
        break


