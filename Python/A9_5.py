# Grundzahlen
R_D={ "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

eingabe= input()
vorzahl=0
sum=0

# Zuerst wird die akltuelle Zahl gespeichert und die vorherige Zahl auf null gesetzt und in der nächste Iteration wird überprüft ob die Zahl
# größer als die vorherige Zahl ist
# wenn ja wird die vorherige Zahl aus der Zahl substrahiert
# wenn nein wird die vorherige Zahl in die Zahl addiert

for index in eingabe:                   # erste X       #zweite V      #dritte I           #vierte I
    if index in R_D:                    # ja            # ja           # ja                # ja
        if R_D[index] > vorzahl:        # 10 > 0        # 5>10         # 1>5               # 1>1
            sum -= vorzahl              # sum= 0        #                                  
        else: 
            sum += vorzahl                              #sum= 10       # sum=10 +5         # sum=16
    vorzahl= R_D[index]                 # VZ=10         # VZ=5         # VZ= 1             # VZ= 1

print(vorzahl)
print(sum)    
sum +=vorzahl                                                                                           # sum= 17                         

print("Ergebnis: "+ str(sum))
    

 
        