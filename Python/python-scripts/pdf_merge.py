#from importlib.metadata import files
import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter
# pip install pyPDF2

def merge_pdfs(result_name):  # resultname --> Der Name der Ausgabe-Datei
    pdf_writer = PdfFileWriter() # Objekt PdfFileWriter erzeugen
    root = tkinter.Tk()         # Ein Tkinter- Fenster erzeugen
    files= filedialog.askopenfilenames(parent= root, title= 'PDFs auswählen')
    # File Dialog erzeugen, um die Dateien auszuwählen. Diese Files werden in der Variable files
    # gespeichert. Um das Ergebnis wird in einer Liste gespeichert und kann iteriert werden.
    # Der Parameter parent ist das zuvor erzeugte Tkinter-Fenster und optional ein Titel für das Finster

    for file in root.tk.splitlist(files):
        #root.tk.splitlist(files) enthält eine liste zu den Pfaden der Dateien in der variable files
        pdf_reader = PdfFileReader(file, strict=False) # Die Dateien nacheinander einlesen
        for page in range(pdf_reader.getNumPages()):
            # Die Seiten in der jeweiliegen Datei iterieren und sie direkt zu Begin der PDF in pdf_writer  einfügen
            pdf_writer.addPage(pdf_reader.getPage(page))
    print('PDFs zusammengefügt')
    with open(result_name,'wb') as out: # out ist der Name des finale PDF für die weiterverarbeitung
        pdf_writer.write(out)   # Den PDF ausgeben
        print('PDF-Datei erfolgreich erstellt.')

merge_pdfs("C:\\Users\\E1376231\\Downloads\\Deutschlandstipendium\\Weitere\\pdf_merge.pdf")
