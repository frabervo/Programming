# Python-Grundlagen

![Sololearn](https://www.google.com/imgres?imgurl=https%3A%2F%2Ficonape.com%2Fwp-content%2Fpng_logo_vector%2Fsololearn-logo.png&imgrefurl=https%3A%2F%2Ficonape.com%2Fsololearn-logo-logo-icon-svg-png.html&tbnid=Nllni-XPSCn9NM&vet=12ahUKEwjMm4ikoKf1AhVF-4UKHejZBFAQMygQegUIARDLAQ..i&docid=vCW52Xsn0aWufM&w=600&h=600&itg=1&q=Sololearn&ved=2ahUKEwjMm4ikoKf1AhVF-4UKHejZBFAQMygQegUIARDLAQ)

Dieses Verzeichnis ist für die Programmierungssprache Python. Zuerst möchte ich die Grundlagen durchgehen, die ich in [Sololearn](https://www.sololearn.com/learning/1157) gelernt habe.

1. Hello World
2. Einfache Operationen:            +; -; /; //
3. Datentypen
4. Exponentation:                   print(2**5)--> 2^5
5. Quotient(//) und Rest(%)
6. Zeichenkette:                    " " and ''
7. Zeilenumbrüche:                  \n und """ """
8. Zeichenkette-Operationen:        "string"*3 und "string1" + "string2"
9. variablen-Deklarationen:         Variablenname = Wert
10. Mit Variabelen arbeiten:        Datentyp(input())
11. User-Eingabe:                   input()
12. Mit input() arbeiten
13. In-Place-Operatoren:            x+=3

## Kontrollstruktur

14. Booleen (True und False) und Operatoren:         ==, != , >, >=, =<, < Für Zahlen und Zeichenkette und print(4==5) --> False
15. if- Kontrollstruktur
if Bedingung:
   Anweiseungen

Die Einrückung vor den Anweisung ermöglicht die Bearbeitung des Codes in Blöcken
16. if-else
if Bedingung: 
    Anweisungen 
else:
    Anweisungen 
Eine Else-Kontrollstruktur kann nur eine if-Anweisung enthalten.

if Bedingung: 
    Anweisungen 
elif Bedingung:
    Anweisungen
else:
    Anweisung

17. Boolean Operatoren:                              and, or, not 
18. While-loops

while Bedingung: 
    Anweisungen
    Kontroll-Variable zb. inkrementieren oder dekrementieren

19. Break und continue

while true: 
    Anweisungen
    Kontroll-Variable zb. inkrementieren oder dekrementieren
    variable_überprüfen
    break --> Geht von der Schleife raus

 while true: 
    Anweisung1
    Kontroll-Variable zb. inkrementieren oder dekrementieren
    variable_überprüfen
    continue    --> Die Anweisung zwei wird an dieser Stelle nicht ausgeführt  
    Anweisung2

## Lists
20. Lists Deklaration

words = ["Hello", "world", "!"]  

Auf die Elemente durch deren Index in dem Feld: words[0], words[1], words[2]. Erstes Elements begin bei 0

Feld-Zwei Dimensionen 

21. String as Lists
str="Python"
print(str[1]) --> y
nums = [1, 2, 3]
print(nums + [4, 5, 6])  --> [1, 2, 3, 4, 5, 6]
print(nums * 3) --> [1, 2, 3, 1, 2, 3, 1, 2, 3]

22. 