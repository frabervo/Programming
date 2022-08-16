# <p style="text-align:center">Entwicklung einer To-List Anwendung</p>
Quelle:  [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-make-a-todo-list-cli-application-using-python/)
Letzter Zugriff: 16.08.2022

## Voraussetzungen 
+ Das laufende Betriebssystem: Windows
+ Python3 ist installiert

## Funktionalitäten der Anwendung 
+ Eine neue Aufgabe hinzüfgen
+ Eine Aufgabe löschen 
+ Eine Aufgabe ändern 
+ Die To-Do-Liste anzeigen 

## Werkzeuge 
Die Anwendung wurde mit der Programmiersprache Python entwickelt. Aus diesem Grund wird eine Datei todolist.py benötigt. Zusätzlich wird ein Script todolist.bat gebraucht, um den Python Script auszuführn.

### todolist.bat

    @echo off
    python3 todolist.py %1 %2

### einen symbolischen Link für ausführbare Datei erstellen
    mklink todolist todolist.bat
:memo: Dieser Befehl muss mit administrationsrechte ausgeführt werden.

### Ausführliche Beschreibung des Quellcodes
#### Module
a. sys-Modul
Dieses Modul bietet Zugriff auf einige Variablen, die vom Interpreter verwendet oder verwaltet werden, und auf Funktionen, die stark mit dem Interpreter interagieren. Es ist immer verfügbar.

Um Daten von/zu den Standardstreams zu schreiben oder zu lesen verwenden Sie das zugrunde ligende Pufferobjekt. Um zum Beispiel Bytes in stdout zu schreiben, vrewenden Sie: sys.stdout.buffer.write(b'abc').