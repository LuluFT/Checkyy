import random #das Modul Random wird importiert. Dort ist der Befehl "shuffle" vorhanden um eine Liste durchzuwürfeln.

#Variabel, wie viele Versuche man hat bis man verloren hat
leben = 3


#Leere Liste wird erstellt 
lstEins = []
#Liste wird gefüllt mit den Werten 0-100
for i in range (0,100):
    lstEins.append(i)

#Liste wird einmal durchgewürfelt, sodass alle Inhalte an einer anderen Position stehen
random.shuffle(lstEins)
#Lösung ist gleich die Addition von der 3ten und 60ten Stelle aus der Liste


Aufgabe = 1 #Nr der Aufgabe
lösung = (lstEins[3]+lstEins[60])
#Solange das Leben nicht unter 0 fällt, wiederholen sich die Aufgaben
print ("Hallo, bitte geben Sie die Lösung ein, zu der Aufgabe:")
print("")
print ("Aufgabe Nr:",Aufgabe)
print (lstEins[3],"+",lstEins[60],"=",)



while leben != 0:  
    
    
    lösung = (lstEins[3]+lstEins[60])
    
    #die Konsole verlangt einen Input als Int
    input1 = int(input())
    
    #wenn der Input den gleichen Wert wie die Lösung hat, wird eine neue Aufgabe gestellt.
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
        print("Nächster Versuch:")
        print("")
    #wenn man kein Leben mehr hat, wird einem unter die Nase gerieben, dass man verloren hat und das Programm beendet sich.
    if leben == 0:
        print ("Leider verloren!")
    


    
