import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input()
        pass
    if int(txtIn) == 2:
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break
