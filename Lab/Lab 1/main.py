import random
class Domanda:
    def __init__(self, testo, livello, rispostaCorretta, rispostaSbagliata1, rispostaSbagliata2, rispostaSbagliata3):
        self.testo = testo
        self.livello = livello
        self.rispostaCorretta = rispostaCorretta
        self.rispostaSbagliata1 = rispostaSbagliata1
        self.rispostaSbagliata2 = rispostaSbagliata2
        self.rispostaSbagliata3 = rispostaSbagliata3

    def __str__(self):
        return f"Testo: {self.testo}\nLivello: {self.livello}\nRispostaCorretta: {self.rispostaCorretta}\nRispostaSbagliata1: {self.rispostaSbagliata1}\nRispostaSbagliata2: {self.rispostaSbagliata2}\nRispostaSbagliata3: {self.rispostaSbagliata3}\n"

class Player:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

class Game:
    def __init__(self, listaDomande):
        self.listaDomande = listaDomande

    def gioco(self):
        lvlMAX = 0
        for domanda in lista_domande:
            if int(domanda.livello) > lvlMAX:
                lvlMAX = int(domanda.livello)

        lvlAttuale = 0
        for i in range(0, lvlMAX+1):
            listaDomandeLivelloAttuale = self.getListaDomandeLivello(lvlAttuale)
            random.shuffle(listaDomandeLivelloAttuale)
            domanda = listaDomandeLivelloAttuale[0]
            lista_risposte = [domanda.rispostaCorretta, domanda.rispostaSbagliata3, domanda.rispostaSbagliata2, domanda.rispostaSbagliata1]
            random.shuffle(lista_risposte)
            print(f"Livello {lvlAttuale}) {domanda.testo}")
            cnt = 1
            for risposta in lista_risposte:
                print(f"        {cnt}) {risposta}")
                cnt+=1

            risposta_inserita = int(input("Inserisci la risposta: "))

            index_risposta_corretta = lista_risposte.index(domanda.rispostaCorretta)
            if risposta_inserita == (index_risposta_corretta+1):
                print("Risposta corretta!\n")
                lvlAttuale+=1
                continue
            else:
                print(f"Risposta sbagliata! La risposta corretta era {(index_risposta_corretta+1)}.")
                print(f"Hai totalizzato {lvlAttuale} punti!")
                nickname = input("Inserisci il tuo nickname: ")
                return nickname, lvlAttuale


        print(f"Hai totalizzato {lvlAttuale-1} punti!")
        nickname = input("Inserisci il tuo nickname: ")
        return nickname, (lvlAttuale-1)


    def getListaDomandeLivello(self, lvlAttuale):
        lista = []
        for domanda in lista_domande:
            if int(domanda.livello) == lvlAttuale:
                lista.append(domanda)
        return lista


lista_domande = []
nome_file = "domande.txt"
file = open(nome_file, "r")

cnt = 1
for line in file:
    if line == '':
        raise IOError

    if cnt == 7:
        cnt = 1
        continue

    if cnt == 1:
        testo = line.strip()  # Rimuovi eventuali spazi o caratteri di newline
    elif cnt == 2:
        if int(line.strip()) >= 0:
            livello = line.strip()
    elif cnt == 3:
        rispostaCorretta = line.strip()
    elif cnt == 4:
        rispostaSbagliata1 = line.strip()
    elif cnt == 5:
        rispostaSbagliata2 = line.strip()
    elif cnt == 6:
        rispostaSbagliata3 = line.strip()
        domanda = Domanda(testo, livello, rispostaCorretta, rispostaSbagliata1, rispostaSbagliata2, rispostaSbagliata3)
        lista_domande.append(domanda)

    cnt += 1

file.close()

ancora = True
while ancora:
    scelta = input("\nVuoi giocare? ")
    if scelta == "si":
        game = Game(lista_domande)
        (nickname, points) = game.gioco()
        print(f"Bravo {nickname}, hai totalizzato {points} punti!")
    else:
        print("fanculo")
        ancora = False