import numpy as np, os

def insert_dati(cognome) : # inserimento dati di ogni studente, ognuno viene associato ad un dizionario
    last_name = cognome
    student = {  
        "cognome" : last_name,
        "voti" : {} # dizionario annidato che conterrà le coppie materia-voto
    }

    for materia in materie : # per ogni materia inserisco il voto preso all'esame
        voto = int(input(f"Quanto ha preso in {materia}? "))
        student["voti"].update({materia : voto}) # aggiungo ogni coppia a "voti" 
        
    studenti.append(student)

def medie_studenti () : # calcolo della media totale (tra tutte le materie) di ogni studente
    medie = {} # dizionario in cui verrà aggiunta la coppia cognome-media

    for studente in studenti :       
        media = [] # lista in cui verranno aggiunti i voti di uno studente e su cui verra calcolata la media

        for materia in materie :
            media.append(studente["voti"][materia])

        media_arr = np.array(media)  
        mean_tot = np.mean(media_arr)
        medie.update({studente["cognome"] : mean_tot}) # aggiungo ogni coppia a medie

    print("Le medie generali degli studenti sono: ")
    for item in medie.items() :
        print(*item, sep= " = ")

def top_bottom_grade(materia) : # scelta una materia, vengono restituiti lo studente migliore e quello peggiore
    subj = materia
    top = 0
    bottom = 101

    for studente in studenti : # ogni voto della materia scelta viene confrontato con quello degli altri studenti
        if studente["voti"][subj] > top :    
            top = studente["voti"][subj]

        if studente["voti"][subj] < bottom :
            bottom = studente["voti"][subj]

    migliore = [studente["cognome"] for studente in studenti if studente["voti"][subj] == top]
    peggiore = [studente["cognome"] for studente in studenti if studente["voti"][subj] == bottom]

    print(f"Lo studente che ha preso il voto più alto ({top}) in {subj} è {migliore[0]}.")
    print(f"Lo studente che ha preso il voto più basso ({bottom}) in {subj} è {peggiore[0]}.")

def filtro_soglia(soglia, materia) : # definiti materia e voto-soglia restituisce studenti con almeno un voto > ad esso
    studenti_soglia = set(())
    voto_soglia = soglia
    materia_soglia = materia

    for studente in studenti : 
        check = False
    
        if studente["voti"][materia_soglia] > voto_soglia : # se il voto è > alla soglia il cognome viene salvato
               check = True
        if check == True :
            studenti_soglia.add(studente["cognome"])

    if len(studenti_soglia) == 0 :
        print(f"Non ci sono studenti che hanno più di {voto_soglia} in {materia_soglia}.")
    else :
        print(f"Gli studenti che hanno più di {voto_soglia} in {materia_soglia} sono: ")
        for studente in studenti_soglia :
            print(studente)

def visualization() :
    for studente in studenti : # per ogni dizionario nella lista studenti
        for chiave in studente : # per ogni chiave del dizionario (studente)
            if chiave == "cognome" : # visualizzazione diversa in base al tipo di dato
                print(chiave, ":", studente[chiave])
            else :
                print(chiave, ":")
                for key in studente[chiave] :
                    print(key, "=", studente[chiave][key])
        print("")

def controllo_materia(materia) : # presenza o meno dell'input dentro la lista materie
    subj = materia
    while True :
        if subj in materie :
           break
        else :
           subj = str(input("Materia inesistente. Dimmi un'altra materia: ")) 

    return subj
#------------------------------------------------------------------------------------------------------------------------------------

materie = ["italiano", "matematica", "fisica", "storia", "inglese"]
print("Le materie sono:")
print(*materie, sep = ", ")

while True : # possibilità di aggiungere materie in più rispetto a quelle di default
    print("Vuoi aggiungere un'altra materia?")
    aggiunta = int(input("Premi 1 per aggiungere una materia o premi 0 per andare avanti: " ))

    if aggiunta == 0 :
        os.system('cls')
        break

    else:
        new_materia = str(input("Che materia vuoi aggiungere? "))
        materie.append(new_materia)
        print("Operazione andata a buon fine!")
        os.system('cls')

studenti = []  # lista in cui verranno aggiunti tutti gli studenti, ognuno con i supi dati      
all_studenti = int(input("Quanti studenti ci sono? "))
while all_studenti < 1  : # non può esserci meno di uno studente
    all_studenti = int(input("Quanti studenti ci sono? "))
  
os.system('cls') # pulizia terminale
i = 0
while i < all_studenti : # inserimento dati di ogni studente
            cognome = str(input("Dimmi il cognome dello studente: "))
            insert_dati(cognome) # guardare funzione
            i += 1

os.system('cls')
functs = "1. Calcolo medie  2. Voto massimo e minimo  3. Filtro per soglia  4. Visualizzazione dati  5. Termina programma"  
print(functs) # le funzioni possibili resteranno sempre visibili a terminale durante l'esecuzione del programma
scelta_funzione = int(input("Seleziona una funzione: "))

while scelta_funzione != 5 :
    if scelta_funzione == 1 : # calcolo della media totale (tra tutte le materie) di ogni studente
        os.system('cls')
        print(functs)
        print("-- CALCOLO MEDIE --") 
        medie_studenti() # guardare funzione
        
        scelta_funzione = int(input("Seleziona una funzione: "))
    
    elif scelta_funzione == 2 : # scelta una materia, vengono restituiti lo studente migliore e quello peggiore
        os.system('cls')
        print(functs)
        print("-- VOTO MASSIMO E MINIMO --")
        scelta_materia = str(input("Di quale materia vuoi sapere lo studente peggiore e quello migliore? "))
        x = controllo_materia(scelta_materia)
        top_bottom_grade(x) # guardare funzione

        scelta_funzione = int(input("Seleziona una funzione: "))

    elif scelta_funzione == 3 : # definiti materia e voto-soglia restituisce studenti con almeno un voto > ad esso
        os.system('cls')
        print(functs)
        print("-- FILTRO PER SOGLIA --")
        scelta_materia = str(input("Per quale materia vuoi filtrare? "))
        y = controllo_materia(scelta_materia)
        soglia = int(input("Qual'è il voto sopra il quale vuoi filtrare? "))
        filtro_soglia(soglia, y) # guardare funzione

        scelta_funzione = int(input("Seleziona una funzione: "))
    
    else: # visualizzazione di tutti i dati di ogni studente
        os.system('cls')
        print(functs)
        print("-- VISUALIZZAZIONE DATI --")
        visualization() # guardare funzione

        scelta_funzione = int(input("Seleziona una funzione: "))


print("Sessione terminata!")