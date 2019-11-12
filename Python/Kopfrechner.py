import random #das Modul Random wird importiert. Dort ist der Befehl "shuffle" vorhanden um eine Liste durchzuwürfeln.
import time # hier wird das Modul Time importiert um die Möglichkeit zu haben, mit der Zeit zu arbeiten.

leben = 3#Variabel, wie viele Versuche man hat bis man verloren hat

lstEins = [] #Leere Liste wird erstellt 

#Liste wird gefüllt mit den Werten 0-100
for i in range (0,100):
    lstEins.append(i)

#Liste wird einmal durchgewürfelt, sodass alle Inhalte an einer anderen Position stehen
random.shuffle(lstEins)

#Lösung ist gleich die Addition von der 3ten und 60ten Stelle aus der Liste, welche oben erstellt wurde.

lösung = (lstEins[3]+lstEins[60])
Aufgabe = 1 #Variabel um die aktuelle Nummer der Aufgabe anzuzeigen.

#Hier werden mehrere Absätze erstellt, welche im Terminal angezeigt werden.
print("")
print("")
print("")
print("")

#Hier wird die Aufgabe initialisiert. Es wird ein String angezeigt mit unten stehendem Text und anschließend wird die Aufgaben NR und die Aufgabe angezeigt.
print ("Hallo, bitte geben Sie die Lösung ein, zu der Aufgabe:")
print("")
print ("Aufgabe Nr:",Aufgabe)
print (lstEins[3],"+",lstEins[60],"=",)

ts = time.time()#Startzeit wird gestartet

    

while leben != 0:  #Während das Leben ungleich 0 ist, werden folgende Sachen ausgeführt.
    
    
    lösung = (lstEins[3]+lstEins[60]) # Variabel Lösung wird deklariert.
    
   
    input1 = int(input())#Variabel Input1 wird deklariert. Hier wird eine Ganzzahl als Input verlangt.

    
    #Wenn der Input gleich der Lösung ist, wird zur Aufgaben Zahl eine 1 addiert.
    #Die Liste wird noch einmal durchgewürfelt und es wird eine neue Aufgabe gestellt.
    if input1 == lösung: 
       
        random.shuffle(lstEins)
        Aufgabe = (Aufgabe+1)
    
        print("Die richtige Antwort lautet:",lösung)
        print("sehr gut weiter geht es zur nächsten Aufgabe!")
        print("")
        print("Nächste Aufgabe!")
        print ("Aufgabe Nr:",Aufgabe)
        print (lstEins[3],"+",lstEins[60],"=",)
        
    #wenn der Input ungleich der Lösung ist, wird ein Leben abgezogen und die Aufgabe wiederholt.   
    else:       
        print ("Schade, leider falsch")
        leben = (leben -1 )
        print ("Leben übrig:",leben) 
        print("")
        print("")
        print("Neuer Versuch:")
        print("")
        print (lstEins[3],"+",lstEins[60],"=",)



#wenn man kein Leben mehr hat, wird einem unter die Nase gerieben, dass man verloren hat und das Programm beendet sich.
if leben == 0:
    print("Der Highscore beträgt: ", Aufgabe)
    print ("Leider verloren!")
    
    #Hier wird die Startzeit von der jetztigen Zeit abgezogen. Anschließend wird einem die gesamte Dauer des Programms angezeigt
    #Hier wird unterscheiden, ob es eine Sekunde, ein paar Sekunden oder eine Minute lief.
    td =(time.time() - ts)
    Sekunde = td.__round__(2)
    
    if Sekunde == 1:
        print("Das Programm lief:",Sekunde.__round__(),"Sekunde")
    elif Sekunde <= 60:
        print("Das Programm lief:",Sekunde.__round__(),"Sekunden")
    elif Sekunde >= 60:
        Minute = int(Sekunde/60)
        if Minute == 1:
            print("Das Programm lief:",Minute,"Minute")
        elif Minute >= 1:
            print ("Das Programm lief:",Minute,"Minuten")
    exit()
       

 
