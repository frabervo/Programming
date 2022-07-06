#from importlib.metadata import files
import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
# pip install pyPDF2

def merge_pdfs(result_name):  # resultname --> Der Name der Ausgabe-Datei
    root = tkinter.Tk()         # Ein Tkinter- Fenster erzeugen
    files= filedialog.askopenfilenames(parent=root, title='PDFs auswählen')
    # File Dialog erzeugen, um die Dateien auszuwählen. Diese Files werden in der Variable files
    # gespeichert. Um das Ergebnis wird in einer Liste gespeichert und kann iteriert werden.
    # Der Parameter parent ist das zuvor erzeugte Tkinter-Fenster und optional ein Titel für das Finster
    iterator = 1
    pdf_Merger = PdfFileMerger()
    for file_name in root.tk.splitlist(files):
        # input_file = open(file, "rb")
        # print(type(input_file))
        input_file = PdfFileReader(file_name, strict=False)
        # with open(file=file_name, mode="rb") as input_file:
        #    pdf_Merger.append(input_file)
        pdf_Merger.append(input_file)
        iterator += 2
    print('PDFs zusammengefügt')
    with open(result_name, "wb") as output:
        pdf_Merger.write(output)   # Den PDF ausgeben
    print('PDF-Datei erfolgreich erstellt.')
    pdf_Merger.close()

merge_pdfs("C:\\Users\\E1376231\\Downloads\\Deutschlandstipendium\\Weitere\\pdf_merge.pdf")
