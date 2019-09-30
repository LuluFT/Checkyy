import matplotlib.pyplot as plt 
#Deklarieren
summe = 0
reiskorn = 0
feld = 0
#Leere Liste [] erstellen
feldListe = []

#Ausrechner der Reiskörner pro Feld
for feld in range (64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    if summe == (1):
        print (f"Feld 1 = {1:>31} Reiskorn und damit insgesamt {1:>31} Reiskorn")

    else:
    
        print (f"Feld {feld+1} = {reiskorn:>30,} Reiskörner und damit insgesamt {summe:>30,} Reiskörner")
        
#Gewicht der Reiskörner ausrechnen
gewicht = summe * 0.02 / 1000 / 1000
print ()
print (f"Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten Reiskörner {gewicht:,.0f} Tonnen")

#Liste darstellen
plt.title ("Reiskorngraph")
plt.plot(feldListe)
plt.show()
exit()