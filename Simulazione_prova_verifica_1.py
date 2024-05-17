import numpy as np
#Ho importato Pandas per allenarmi un po ad utilizzare le sue funzioni
import pandas as pd

#Stampa l'elenco delle possibilità da fare
def elenco():
    print("\n1)Inserire i dati")
    print("2)Calcolo media")
    print("3)Max e Min")
    print("4)Voti sopra la soglia")
    print("5)Visualizza")
    print("0)ESCI")
#Semplice controllo sulla scelta
def controllo_scelta(scelta):
    while scelta < 0 or scelta > 5:
        scelta = int(input("Valore Errato. Inserisci un numero: "))
    return scelta
#Prima funzione: aggiungere
def aggiungi(database):
    nome=str(input("Dammi il nome dello studente: "))
    a = 0
    #determino i vari indici che sono le materie, così ho in una lista i vari nomi delle materie, è più facile utilizzarle essendo ora indicizzate in una lista
    indici = list(database["Luca"].keys())
    cont=[]
    while a!=4:
        b = 0
        voti = []
        while b !=5:
            voto = int(input(f"Inserisci il {b+1}° voto della materia {indici[a]}: "))
            while voto < 0 or voto > 10:
                voto = int(input(f"Valore troppo alto o troppo piccolo. Inserisci il {b + 1}° voto della materia {indici[a]}: "))
            voti.append(voto)
            b+=1
        voti = tuple(voti)
        cont.append(voti)
        a+=1
    database[nome]= {"Italiano" : cont[0], "Matematica" : cont[1], "Storia" : cont[2], "Geografia" : cont[3]}
    return database
#Seconda funzione: calcolare la media 
def media(database):
    #ho creato due liste con all'interno i vari nomi e le materie, essendo le chiavi del dizionario
    indici_nomi = list(database.keys())
    indici_materie = list(database["Luca"].keys())
    a = 0
    k=0
    cont = []
    while a != len(database):
        b = 0
        medie = []
        while b != 4:
            #utilizzo numpy: creo un array e la media me la calcola lui
            array = np.array(database[indici_nomi[a]][indici_materie[b]])
            media = np.mean(array)
            medie.append(media)
            k+=1
            b+=1
        cont.append(medie)
        a+=1
    a = 0
    while a != len(database):
        print(f"\nLo studente {indici_nomi[a]} ha le seguenti medie: ")
        print(f"La materia italiano è pari a {cont[a][0]}")
        print(f"La materia matematica è pari a {cont[a][1]}")
        print(f"La materia storia è pari a {cont[a][2]}")
        print(f"La materia geografia è pari a {cont[a][3]}")
        a+=1
#Terza funzione: trovare il massimo e il minimo per ogni materia
def max_min(database):
    b = 0
    nome_max = ""
    materia_max = ""
    nome_min = ""
    materia_min = ""
    indici_nomi = list(database.keys())
    indici_materie = list(database["Luca"].keys())
    while b != 4:
        max = 0
        min = 11
        a = 0
        while a != len(database):
            c = 0
            while c != 5:
                if database[indici_nomi[a]][indici_materie[b]][c] > max:
                    #una volta scoperto il max vado a salvarmi i dati generali (nome, materia e max)
                    nome_max = indici_nomi[a]
                    max = database[indici_nomi[a]][indici_materie[b]][c]
                if database[indici_nomi[a]][indici_materie[b]][c] < min:
                    # una volta scoperto il min vado a salvarmi i dati generali (nome, materia e min)
                    nome_min = indici_nomi[a]
                    min = database[indici_nomi[a]][indici_materie[b]][c]
                c+=1
            a+=1
        print(f"Per la materia {indici_materie[b]}, lo studente {nome_max} ha ottenuto il voto massimo, cioè {max}")
        print(f"Per la materia {indici_materie[b]}, lo studente {nome_min} ha ottenuto il voto massimo, cioè {min}")
        b+=1
#Quarta funzione: Sopra la soglia
def sopra_soglia(database):
    soglia = int(input("Inserisci la soglia dei voti: "))
    a = 0
    indici_nomi = list(database.keys())
    indici_materie = list(database["Luca"].keys())
    while a != len(database):
        b = 0
        while b != 4:
            c = 0
            k = 0
            while c != 5 and k == 0:
                if database[indici_nomi[a]][indici_materie[b]][c] < soglia:
                    #nel caso lo studente abbia anche un solo voto sotto la soglia non viene considerato. utilizzo una variabile k 
                    k = 1
                c+=1
            if k == 0:
                print(f"Lo studente {indici_nomi[a]} ha tutti i voti della materia {indici_materie[b]} sopra la soglia che è {soglia}")
            b+=1
        a+=1
#Quinta funzione: Visualizza
def visualizza(database):
    indici_nomi = list(database.keys())
    indici_materie = list(database["Luca"].keys())
    i = 0
    while i<1 or i>2:
        i = int(input("Vuoi vederlo con Pandas.\n1)Si\n2)No\nInserisci il numero: "))
    #Utilizzo Pandas, è facoltativo e volevo un po esercitarmi
    if i == 1:
        a = 0
        while a != len(database):
            print(indici_nomi[a], ":")
            #utilizzo i DataFrame
            tabella = pd.DataFrame(database[indici_nomi[a]])
            print(tabella)
            a += 1
    else :
        a = 0
        while a != len(database):
            print(f"\n\nLo studente {indici_nomi[a]} ha i seguenti voti nelle seguenti materie: ")
            b = 0
            while b != 4:
                print("\n", indici_materie[b])
                c = 0
                while c != 5:
                    print("  ",database[indici_nomi[a]][indici_materie[b]][c], end="")
                    c+=1
                b+=1
            a+=1
database = {
    "Luca" : {
        "Italiano" : (8, 7, 4, 9, 10), "Matematica" : (8, 5, 8, 9, 7), "Storia" : (7, 7, 7, 5, 2), "Geografia" : (5, 5, 2, 9, 7)
    },
    "Alessandro" : {
        "Italiano" : (7, 7, 3, 9, 1), "Matematica" : (9, 5, 7, 9, 6), "Storia" : (4, 7, 1, 8, 9), "Geografia" : (5, 5, 10, 7, 7)
    },
    "Tommaso" : {
        "Italiano" : (9, 7, 5, 9, 10), "Matematica" : (8, 6, 8, 10, 7), "Storia" : (1, 7, 7, 5, 2), "Geografia" : (6, 6, 2, 9, 7)
    },
    "Giulio" : {
        "Italiano" : (10, 7, 4, 8, 10), "Matematica" : (8, 6, 8, 7, 7), "Storia" : (7, 8, 7, 8, 2), "Geografia" : (4, 5, 2, 10, 7)
    },
    "Irene" : {
        "Italiano" : (8, 8, 8, 9, 10), "Matematica" : (8, 5, 3, 9, 7), "Storia" : (7, 1, 7, 5, 2), "Geografia" : (5, 5, 5, 9, 7)
    }
}
print("Buongiorno")
scelta = 1
while scelta != 0:
    elenco()
    scelta = int(input("Inserisci un numero: "))
    controllo_scelta(scelta)
    if scelta == 1:
        aggiungi(database)
    elif scelta == 2:
        media(database)
    elif scelta == 3:
        max_min(database)
    elif scelta == 4:
        sopra_soglia(database)
    elif scelta == 5:
        visualizza(database)
    elif scelta == 0:
        print("Grazie per averci usato")
print("Fine Programma")