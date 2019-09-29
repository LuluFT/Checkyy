summe = 0
reiskorn = 0
feld = 0

for feld in range (64):
    reiskorn = 2**feld
    summe += reiskorn
    if summe == (1):
        print ("Feld 1 = {:>31} Reiskorn und damit insgesamt {:>31} Reiskorn".format("1", "1"))

    else:
    
        print ("Feld {} = {:>30,} Reiskörner und damit insgesamt {:>30,} Reiskörner".format(feld+1, reiskorn, summe))
        

gewicht = summe * 0.02 / 1000 / 1000
print ()
print ("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten Reiskörner {:,.0f} Tonnen".format(gewicht))
