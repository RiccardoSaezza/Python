#Programmazione ad oggetti
#Classi nella programmazione ad oggetti 

class Studente:                     #La classe unisce  funzioni,variabili ecc in modo logico, con questo metodo posso ad esempio creare più entità senza dover ogni volta riscrvere tutto 
    
    ore_settimanali=36
    corpo_studentesco=0
    
    def __init__(self, nome, cognome, cosrso_di_studi) :           #Sto inizializzando una funzione "METODO" , in questo caso iniit, quando lo faccio tra parentesi devo mettere la parola "self"
        self.nome=nome
        self.cognome=cognome
        self.corso_di_studi=cosrso_di_studi                         #Al self. corrisponde l'istanza quindi ciascun oggetto creato dalla classe
        Studente.corpo_studentesco +=1

    def scheda_personale(self) :
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di studi:{self.corso_di_studi}\n Ore settimanali:{self.ore_settimanali}"              #Per accedere alle ore settimanali posso sia richiamare la funzione (Studente.), oppure uso il self.


studente_uno=Studente("Py","Mike","Programmazione")
studente_due=Studente("Marta","Stannis","Scienze politiche")

studente_uno.ore_settimanali+=4                              #Incremento le ore settimanali solo del primo studente 
print(studente_uno.scheda_personale())                      #!!!RICORDARSI LE PARENTESI TONDE DOPO LA FUNZIONE PERCHE RICHIAMO LA FUNZIONE
print(studente_due.scheda_personale())
print(Studente.corpo_studentesco)
#le variabili di classe vengono condivise da tutte le istanze 


#l'ereditarietà permette di creare classi "figlie" che erditano variabili dalle calssi "madri" lasciando invariate le madri 

class Persona :
    def __init__(self, nome, cognome, età, residenza) :                                 #metodo
        self.nome=nome
        self.cognome=cognome
        self.età=età
        self.residenza=residenza

    def scheda_personale(self):                                                         #metodo
        scheda=f"Nome: {self.nome} \nCognome: {self.cognome} \nEtà: {self.età} \nResidenza: {self.residenza}"
        return scheda 

    def modifica_scheda(self):
        print("Modifica scheda: \n1 = Nome \n2 = Cognome \n3 = Età \n4 = Residenza ")
        scelta=int(input("Scegli cosa vuoi modificare"))
        if scelta==1 : 
            self.nome=input("Nuovo Nome--> ")                                                       #Con queste istruzioni cambio il valore delle variabili 
        if scelta==2:
            self.cognome=input("Nuovo Cognome--> ")
        if scelta==3 :
            self.età=input("Nuova Età--> ")
        if scelta==4:
            self.residenza=input("Nuova Residenza--> ")


class Studente(Persona):               #Scrivendo così la nuova classe studente erediterà gli attributi della classe persona
    pass                                #Serve per non dare l'errore 


class Insegnante(Persona):              #Scrivendo così la nuova classe insegnante erediterà gli attributi della classe persona 
    pass


studente_uno=Studente("Py","Mike",23, "Casa dello studente")
Insegnante_uno=Insegnante("Mario", "Rossi",33, "Viale roma 32")
print(studente_uno.scheda_personale())
print(Insegnante_uno.scheda_personale())

#print(help(Studente))               #La funzione help serve a capire che attributi vengon passati o cosa viene ereditato 