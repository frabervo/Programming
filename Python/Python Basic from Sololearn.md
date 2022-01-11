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

22. Lists Operationen:
+ in - Operator: ist auch verwendet, um zu wissen, ob ein String ein anderes String enthält.
    words = ["spam", "egg", "spam", "sausage"]
    print("spam" in words) ---> True
    print("egg" in words) ---> True 
    print("tomato" in words) ---> False 

+ not - Operator: 
    words = ["spam", "egg", "spam", "sausage"]
    print(not "tomato" in words) ---> True
    print( "tomato" not in words)---> True

23. for loop

+ Elements eines Array ausgeben
    words = ["hello", "world", "spam", "eggs"]
    for index in words: 
        print(index)
        --> hello
            world
            spam
            eggs

+ Elements eines Strings ausgeben
    str="testing for loops"
    
    for index in str:
        if(x=='t')
            print(x)
    NB: **stop** und **continue** können hier verwendet werden

24. **range(n)** : gibt die Zahlen von 0 bis n-1
    Die Funktion list() kann die Rückgabewerte als Array ausgeben lassen.--> list(range(n))--> [0,1,2,...,n-1]

    **range(zahl1, zahl2)**: gibt die zahlen von zahl1 bis (zahl2-1) zurück.

    **range(zahl1, zahl2, schritt)**: gibt die zahlen von zahl1 bis (zahl2-1) in den angegebenen Schritt zurück.
    NB: Wenn **zahl1>zahl2 muss schritt <0** 

    **for i in range(n):**
        Anweisungen
    --> Die Anweisungen werden n-Mal durchgeführt.

25. **lists slices**
    squares=[0,1,4,9,16,25,36,49,64,81]
    print(squares[zahl1:n]) --> gibt die Elemente zahl1 bis (n-1) vom Feld squares zurück.
    print(squares[:n]) --> gibt die Elemente 0 bis (n-1) vom Feld squares zurück. 
    print(squares[:]) --> gibt alle Elemente vom Feld squares zurück.
    print(squares[zahl1:n:schritt]) --> gibt die Elemente zahl1 bis (n-1) vom Feld squares in den vorgegebenen Schritt zurück.
    print(squares[2:-4]) --> [4, 9, 16, 25]
    print(squares[::-1]) --> reverse the list

## Funktionen

26. Funktionen zu Felder/Arrays: 
nums=[1,2,3]
+ len(array_name) -->3:  Gibt die länge eines Arrays zurück.
+ nums.append(4) --> Füngt die Zahl 4 als Element zu dem Array nums hinzu.
+ nums.insert(index,element) --> Fügt ein Element in der vorgegebenen Stelle(index).
+ nums.index(element) --> Gibt den index vom element, wo es zum ersten Mal aufgetaucht ist.
+ max(nums)--> gibt der maximale Wert von nums zurück.
+ min(nums)--> gibt der minimale Wert von nums zurück.
+ nums.count(element) --> Gibt zurück, wie oft element in nums aufgetaucht ist.
+ nums.remove(item) --> Löscht element in nums.
+ nums.reverse(): Invertiert daas Feld nums.

26. Funktionen zu strings:

+ format(): 
    nums =[4,5,6]
    msg = "Numbers: {0} {1} {2}".format(nums[0],nums[1], nums[2])
    print(msg) --> Numbers: 4,5,6: {0} entspricht der Paltzhalter für das Element mit dem Index 0

    Der Paltzhalter kann bennant werden
    a="{x}, {y}".format(x=5, y=12)

str1="
+ ",".**join**(["spam","eggs","ham"]) --> "spam,eggs,ham"
+ "Hello ME".**replace**("ME","world") --> "Hello world"
+ "This is a sentence.".**startswith(**"This") --> True
+ "This is a sentence.".**endswith**("sentence.") --> True
+ "This is a sentence.".**upper**() --> "THIS IS A SENTENCE."
+ "AN ALL CAPS SENTENCE".**lower**() --> "an all caps sentence."
+ "spam, eggs, ham".**split**(", ") --> "['spam', 'eggs', 'ham']"

27. Funktion-Deklaration: 

def my_func(parameter1, parameter2): 
    Anweisungen
    return ...
Aufruf: my_func()

28. Comment: mit #. Python hat keine mehrzeilige Linienkommentar
29. Docstrings: Ein Text zum Beschreiben einer Funktion
Beispiel: 

    def shout(word):
        """
        print a word with an exclamation mark following it.
        """
        print(word +"!")
    shout("spam")