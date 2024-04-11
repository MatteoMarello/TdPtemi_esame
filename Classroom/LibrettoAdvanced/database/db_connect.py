import mysql.connector
import pathlib
# pathlib è una libreria di Python che ci permette di trovare il file di configurazione in modo programmatico e assoluto.

class DBConnect:
    def __init__(self):
        pass

    def get_connection(self):
        try:
            # Nell'option_files devo mettere il percorso da seguire rispetto alla posizione del main.
            # Dato che il file config.cnf si trova all'interno della cartella (package) database, e il package
            # database si trova nella stessa posizione del main.py, basterà scrivere "./database/config.cnf"

            # Il modo descritto sopra sarebbe hard-coded, e se runnassi il programma non dal main ma da un'altra cartella
            # potrebbe non funzionare. Il modo per farlo funzionare è utilizzare un path assoluto. Per creare il path assoluto
            # utilizzo la libreria Python pathlib, e scrivo la riga di codice qua sotto! In questo modo da qualunque file
            # runnassi il programma, non avrò problemi e mi troverà il file config.cnf!

            cnx = mysql.connector.connect(option_files=f'{pathlib.Path(__file__).resolve().parent}/config.cnf')
            return cnx
        except mysql.connector.Error as err:
            print(err)
            return None
